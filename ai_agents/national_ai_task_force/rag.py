"""
Vector Search over National AI Task Force PDF Document

This script creates a FAISS vector store from the National AI Task Force PDF document
and provides functionality to search through it using semantic similarity.
The vector store is saved locally for reuse in future sessions.
"""

import os
import logging
from typing import List, Dict, Any
import time
import traceback
import uuid

# LangChain imports for document loading and processing
from langchain_pymupdf4llm import PyMuPDF4LLMLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_astradb import AstraDBVectorStore
from langchain.schema import Document

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
PDF_PATH = os.path.join("docs", "National-Artificial-Intelligence-Task-Force-Policy-Recommendations-Final-1.pdf")
CHUNK_SIZE = 2000
CHUNK_OVERLAP = 200
EMBEDDING_MODEL = "BAAI/bge-base-en-v1.5"

# AstraDB Configuration
ASTRA_DB_API_ENDPOINT = os.getenv("ASTRADB_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRADB_TOKEN")
ASTRA_DB_COLLECTION_NAME = "national_ai_task_force3"

class NationalAITaskForceVectorStore:
    """
    A class to handle the creation and querying of an AstraDB vector store
    from the National AI Task Force PDF document.
    """
    
    def __init__(self, pdf_path: str = PDF_PATH, embedding_model: str = EMBEDDING_MODEL):
        """
        Initialize the vector store with the PDF document.
        
        Args:
            pdf_path: Path to the PDF document
            embedding_model: HuggingFace model to use for embeddings
        """
        logger.info("=" * 50)
        logger.info("INITIALIZING NATIONAL AI TASK FORCE VECTOR STORE")
        logger.info("=" * 50)
        
        self.pdf_path = pdf_path
        logger.info(f"Initializing with PDF path: {self.pdf_path}")
        
        # Check if the PDF file exists
        if not os.path.exists(self.pdf_path):
            logger.error(f"PDF file not found at {self.pdf_path}")
            raise FileNotFoundError(f"PDF file not found at {self.pdf_path}. Please ensure the file exists at the specified location.")
        else:
            file_size = os.path.getsize(self.pdf_path)
            logger.info(f"Found existing PDF file with size: {file_size / 1024:.2f} KB")
        
        # Initialize embeddings
        logger.info(f"Loading HuggingFace embedding model: {embedding_model}")
        start_time = time.time()
        self.embeddings = HuggingFaceEmbeddings(model_name=embedding_model)
        embedding_load_time = time.time() - start_time
        logger.info(f"Embedding model loaded in {embedding_load_time:.2f} seconds")
        
        # Initialize vector store
        self.vector_store = None
        
        # Check AstraDB credentials
        if not ASTRA_DB_API_ENDPOINT or not ASTRA_DB_APPLICATION_TOKEN:
            logger.error("AstraDB credentials not found. Please set ASTRADB_ENDPOINT and ASTRADB_TOKEN environment variables.")
            raise ValueError("AstraDB credentials not found. Please set ASTRADB_ENDPOINT and ASTRADB_TOKEN environment variables.")
        
        # Connect to AstraDB and check if documents need to be added
        self._connect_or_create_vector_store()
    
    def _connect_or_create_vector_store(self) -> None:
        """
        Connect to AstraDB vector store and check if documents need to be added.
        """
        try:
            logger.info(f"Connecting to AstraDB collection: {ASTRA_DB_COLLECTION_NAME}")
            self.vector_store = AstraDBVectorStore(
                embedding=self.embeddings,
                collection_name=ASTRA_DB_COLLECTION_NAME,
                api_endpoint=ASTRA_DB_API_ENDPOINT,
                token=ASTRA_DB_APPLICATION_TOKEN
            )
            logger.info(f"Successfully connected to AstraDB collection: {ASTRA_DB_COLLECTION_NAME}")
            
            # Check if the collection has documents
            doc_count = self.get_document_count()
            logger.info(f"Collection has {doc_count} documents")
            
            # If the collection is empty, add documents
            if doc_count == 0:
                logger.info("Collection is empty, adding documents...")
                self.create_vector_store()
            else:
                logger.info(f"Using existing collection with {doc_count} documents")
                
        except Exception as e:
            logger.error(f"Error connecting to AstraDB: {e}")
            logger.error(f"Exception type: {type(e).__name__}")
            logger.error(f"Exception traceback: {traceback.format_exc()}")
            raise RuntimeError(f"Failed to initialize vector store: {e}")
    
    def load_and_split_document(self) -> List[Document]:
        """
        Load the PDF document and split it into chunks.
        
        Returns:
            List of document chunks
        """
        try:
            logger.info(f"Loading PDF from {self.pdf_path}...")
            
            # Verify the PDF file exists and has content
            if not os.path.exists(self.pdf_path):
                logger.error(f"PDF file not found at {self.pdf_path}")
                raise FileNotFoundError(f"PDF file not found at {self.pdf_path}")
                
            file_size = os.path.getsize(self.pdf_path)
            logger.info(f"PDF file size: {file_size / 1024:.2f} KB")
            
            if file_size == 0:
                logger.error("PDF file exists but has zero size")
                raise ValueError("PDF file exists but has zero size")
            
            # Load the PDF using PyMuPDF4LLMLoader (by page)
            start_time = time.time()
            loader = PyMuPDF4LLMLoader(self.pdf_path)
            documents = loader.load()
            load_time = time.time() - start_time
            
            logger.info(f"Loaded {len(documents)} pages from PDF in {load_time:.2f} seconds")
            
            # Log some information about the documents
            if documents:
                total_chars = sum(len(doc.page_content) for doc in documents)
                avg_chars = total_chars / len(documents)
                logger.info(f"Total characters in document: {total_chars}")
                logger.info(f"Average characters per page: {avg_chars:.2f}")
                
                # Log metadata from the first document as an example
                if documents[0].metadata:
                    logger.info(f"Document metadata example: {documents[0].metadata}")
            else:
                logger.warning("PDF loaded but contains no pages")
            
            # Split documents into chunks
            logger.info(f"Splitting documents with chunk size {CHUNK_SIZE} and overlap {CHUNK_OVERLAP}")
            start_time = time.time()
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=CHUNK_SIZE,
                chunk_overlap=CHUNK_OVERLAP,
                length_function=len,
            )
            
            chunks = text_splitter.split_documents(documents)
            split_time = time.time() - start_time
            logger.info(f"Split into {len(chunks)} chunks in {split_time:.2f} seconds")
            
            # Log information about the chunks
            if chunks:
                chunk_sizes = [len(chunk.page_content) for chunk in chunks]
                avg_chunk_size = sum(chunk_sizes) / len(chunks)
                min_chunk_size = min(chunk_sizes)
                max_chunk_size = max(chunk_sizes)
                logger.info(f"Average chunk size: {avg_chunk_size:.2f} characters")
                logger.info(f"Min chunk size: {min_chunk_size} characters")
                logger.info(f"Max chunk size: {max_chunk_size} characters")
            else:
                logger.warning("Document splitting produced no chunks")
            
            return chunks
        except Exception as e:
            logger.error(f"Error loading or splitting document: {e}")
            logger.error(f"Exception type: {type(e).__name__}")
            logger.error(f"Exception traceback: {traceback.format_exc()}")
            
            # Provide a more helpful error message
            if "is not a valid file or url" in str(e) or "No such file or directory" in str(e):
                logger.error(f"PDF file not found or invalid at {self.pdf_path}")
                raise FileNotFoundError(f"PDF file not found or invalid at {self.pdf_path}. Please ensure the file exists and is a valid PDF.")
            
            # Re-raise the original exception
            raise
    
    def create_vector_store(self) -> None:
        """
        Create an AstraDB vector store from the document chunks.
        """
        try:
            logger.info("=" * 50)
            logger.info("CREATING ASTRADB VECTOR STORE")
            logger.info("=" * 50)
            
            # Load and split document
            logger.info("Loading and splitting document...")
            start_time = time.time()
            chunks = self.load_and_split_document()
            doc_processing_time = time.time() - start_time
            logger.info(f"Document loaded and split in {doc_processing_time:.2f} seconds")
            
            if not chunks:
                logger.error("No document chunks to create vector store from")
                raise ValueError("No document chunks to create vector store from")
                
            logger.info(f"Adding {len(chunks)} document chunks to AstraDB collection...")
            
            # Generate UUIDs for each document
            doc_ids = [str(uuid.uuid4()) for _ in range(len(chunks))]
            logger.info(f"Generated {len(doc_ids)} UUIDs for documents")
            
            # Add documents to the existing vector store
            start_time = time.time()
            
            # If we already have a vector store connection, use add_documents
            if self.vector_store:
                logger.info("Using existing vector store connection to add documents")
                # Use the add_documents method with explicit IDs
                self.vector_store.add_documents(documents=chunks, ids=doc_ids)
            else:
                # Create a new vector store from documents
                logger.info("Creating new vector store from documents")
                self.vector_store = AstraDBVectorStore.from_documents(
                    documents=chunks,
                    embedding=self.embeddings,
                    collection_name=ASTRA_DB_COLLECTION_NAME,
                    api_endpoint=ASTRA_DB_API_ENDPOINT,
                    token=ASTRA_DB_APPLICATION_TOKEN,
                    namespace="",
                    ids=doc_ids
                )
            
            creation_time = time.time() - start_time
            logger.info(f"Added documents to AstraDB vector store in {creation_time:.2f} seconds")
            
            # Verify the vector store was created correctly
            try:
                doc_count = self.get_document_count()
                logger.info(f"Vector store now contains {doc_count} documents")
            except Exception as count_error:
                logger.warning(f"Could not get document count: {count_error}")
            
        except Exception as e:
            logger.error(f"Error creating AstraDB vector store: {e}")
            logger.error(f"Exception type: {type(e).__name__}")
            logger.error(f"Exception traceback: {traceback.format_exc()}")
            raise
    
    def search(self, query: str, k: int = 10) -> List[Dict[str, Any]]:
        """
        Search the vector store for documents similar to the query.
        
        Args:
            query: The search query
            k: Number of results to return
            
        Returns:
            List of documents with their similarity scores
        """
        logger.info("=" * 50)
        logger.info(f"SEARCH QUERY: '{query}'")
        logger.info("=" * 50)
        
        if self.vector_store is None:
            logger.warning("Vector store not initialized, attempting to connect or create...")
            try:
                start_time = time.time()
                self._connect_or_create_vector_store()
                init_time = time.time() - start_time
                logger.info(f"Vector store initialized in {init_time:.2f} seconds")
            except Exception as e:
                logger.error(f"Error initializing vector store: {e}")
                logger.error(f"Exception type: {type(e).__name__}")
                return [{"error": f"Vector store initialization failed: {str(e)}"}]
            
            if self.vector_store is None:
                logger.error("Failed to initialize vector store after attempt")
                return [{"error": "Vector store initialization failed"}]
        
        logger.info(f"Searching for: '{query}' with k={k}")
        
        try:
            # Check if the collection has documents
            doc_count = self.get_document_count()
            logger.info(f"Collection has {doc_count} documents before search")
            
            if doc_count == 0:
                logger.warning("Collection is empty, no search results possible")
                return [{"error": "Vector store is empty, please add documents first"}]
            
            # Search for similar documents
            start_time = time.time()
            results = self.vector_store.similarity_search_with_score(query, k=k)
            search_time = time.time() - start_time
            logger.info(f"Search completed in {search_time:.4f} seconds")
            logger.info(f"Found {len(results)} results")
            
            # Format results
            formatted_results = []
            for i, (doc, score) in enumerate(results):
                # Format the result
                result = {
                    "content": doc.page_content,
                    "metadata": doc.metadata,
                    "score": score,
                    "rank": i + 1
                }
                formatted_results.append(result)
                
                # Log the result
                logger.info(f"Result {i+1}: Score={score:.4f}, Content length={len(doc.page_content)}")
                if doc.metadata:
                    logger.info(f"Metadata: {doc.metadata}")
            
            return formatted_results
            
        except Exception as e:
            logger.error(f"Error searching vector store: {e}")
            logger.error(f"Exception type: {type(e).__name__}")
            logger.error(f"Exception traceback: {traceback.format_exc()}")
            return [{"error": f"Search failed: {str(e)}"}]
    
    def get_document_count(self) -> int:
        """
        Get the number of documents in the vector store.
        
        Returns:
            Number of documents in the vector store
        """
        if self.vector_store is None:
            logger.warning("Vector store not initialized, cannot get document count")
            return 0
            
        try:
            # For AstraDB, we need to use the collection_count method
            count = self.vector_store.collection_count()
            logger.info(f"Vector store contains {count} documents")
            return count
        except AttributeError as e:
            # If collection_count is not available, log the error
            logger.warning(f"collection_count method not available: {e}")
            logger.warning("Trying alternative approach to check if collection exists")
            
            try:
                # Try to get a single document to see if the collection exists
                results = self.vector_store.similarity_search("test", k=1)
                # If we get here, the collection exists but we don't know the count
                logger.info("Vector store exists but count is unknown")
                return len(results) if results else 0
            except Exception as search_error:
                logger.warning(f"Error checking collection existence: {search_error}")
                return 0
        except Exception as e:
            logger.warning(f"Error getting document count: {e}")
            return 0


def main():
    """
    Main function to demonstrate the usage of the vector store.
    """
    logger.info("=" * 80)
    logger.info("NATIONAL AI TASK FORCE VECTOR STORE DEMO")
    logger.info("=" * 80)
    
    # Create vector store
    logger.info("Initializing National AI Task Force Vector Store")
    try:
        start_time = time.time()
        vector_store = NationalAITaskForceVectorStore()
        init_time = time.time() - start_time
        logger.info(f"Vector store initialized in {init_time:.2f} seconds")
        
        # Get document count
        doc_count = vector_store.get_document_count()
        logger.info(f"Vector store contains {doc_count} documents")
        
        # If no documents, explicitly create the vector store
        if doc_count == 0:
            logger.info("No documents found in vector store, creating vector store...")
            vector_store.create_vector_store()
            
            # Check document count again
            new_doc_count = vector_store.get_document_count()
            logger.info(f"Vector store now contains {new_doc_count} documents")
            
            if new_doc_count == 0:
                logger.error("Failed to add documents to vector store")
                print("Error: Failed to add documents to vector store")
                return
        
        # Example search
        query = "What are the key recommendations of the National AI Task Force?"
        logger.info(f"Performing example search: '{query}'")
        
        search_start_time = time.time()
        results = vector_store.search(query)
        search_time = time.time() - search_start_time
        logger.info(f"Search completed in {search_time:.4f} seconds")
        
        print("\n" + "=" * 50)
        print(f"SEARCH RESULTS FOR: '{query}'")
        print("=" * 50)
        print(f"Found {len(results)} results\n")
        
        for i, result in enumerate(results[:3]):  # Show top 3 results
            if "error" in result:
                print(f"Error: {result['error']}")
                logger.error(f"Error in search result: {result['error']}")
            else:
                print(f"Result {i+1}:")
                print(f"Content: {result['content'][:200]}...")
                print(f"Score: {result.get('score', 'N/A')}")
                print(f"Metadata: {result.get('metadata', {})}")
                print("-" * 50)
        
    except Exception as e:
        logger.error(f"Error in main function: {e}")
        logger.error(f"Exception type: {type(e).__name__}")
        logger.error(f"Exception traceback: {traceback.format_exc()}")
        print(f"Error: {e}")
        
    print("\nDemo completed. Check the logs for more details.")


#if __name__ == "__main__":
#    main()