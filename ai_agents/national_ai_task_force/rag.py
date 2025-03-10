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

# LangChain imports for document loading and processing
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
PDF_PATH = os.path.join("docs", "National-Artificial-Intelligence-Task-Force-Policy-Recommendations-Final-1.pdf")
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
FAISS_INDEX_PATH = "national_ai_task_force_faiss"

class NationalAITaskForceVectorStore:
    """
    A class to handle the creation, saving, loading, and querying of a FAISS vector store
    from the National AI Task Force PDF document.
    """
    
    def __init__(self, pdf_path: str = PDF_PATH, embedding_model: str = EMBEDDING_MODEL):
        """
        Initialize the vector store with the PDF document.
        
        Args:
            pdf_path: Path to the PDF document
            embedding_model: HuggingFace model to use for embeddings
        """
        self.pdf_path = pdf_path
        logger.info(f"Initializing with PDF path: {self.pdf_path}")
        
        # Initialize HuggingFace embeddings
        logger.info(f"Loading HuggingFace embedding model: {embedding_model}")
        self.embeddings = HuggingFaceEmbeddings(model_name=embedding_model)
        
        # Initialize vector store
        self.vector_store = None
        
        # Try to load existing vector store or create a new one
        self._load_or_create_vector_store()
    
    def _load_or_create_vector_store(self) -> None:
        """
        Try to load an existing FAISS vector store, or create a new one if it doesn't exist.
        """
        try:
            if os.path.exists(FAISS_INDEX_PATH):
                logger.info(f"Found existing FAISS index at {FAISS_INDEX_PATH}")
                start_time = time.time()
                self._load_vector_store()
                load_time = time.time() - start_time
                logger.info(f"Loaded existing vector store in {load_time:.2f} seconds")
            else:
                logger.info("No existing FAISS index found, creating new vector store")
                start_time = time.time()
                self.create_vector_store()
                create_time = time.time() - start_time
                logger.info(f"Created and saved new vector store in {create_time:.2f} seconds")
        except Exception as e:
            logger.error(f"Error in _load_or_create_vector_store: {e}")
            logger.info("Falling back to creating a new vector store")
            try:
                self.create_vector_store()
            except Exception as inner_e:
                logger.error(f"Critical error creating vector store: {inner_e}")
                raise RuntimeError(f"Failed to initialize vector store: {inner_e}") from inner_e
    
    def _load_vector_store(self) -> None:
        """
        Load the FAISS vector store from disk.
        """
        try:
            logger.info(f"Loading FAISS index from {FAISS_INDEX_PATH}")
            self.vector_store = FAISS.load_local(
                FAISS_INDEX_PATH, 
                self.embeddings,
                allow_dangerous_deserialization=True
            )
            doc_count = self.get_document_count()
            logger.info(f"Successfully loaded FAISS index with {doc_count} documents")
        except Exception as e:
            logger.error(f"Error loading FAISS index: {e}")
            raise
    
    def load_and_split_document(self) -> List[Document]:
        """
        Load the PDF document and split it into chunks.
        
        Returns:
            List of document chunks
        """
        logger.info(f"Loading PDF from {self.pdf_path}...")
        loader = PyPDFLoader(self.pdf_path)
        documents = loader.load()
        
        logger.info(f"Loaded {len(documents)} pages from PDF")
        
        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            length_function=len,
        )
        
        logger.info(f"Splitting documents with chunk size {CHUNK_SIZE} and overlap {CHUNK_OVERLAP}")
        chunks = text_splitter.split_documents(documents)
        logger.info(f"Split into {len(chunks)} chunks")
        
        return chunks
    
    def create_vector_store(self) -> None:
        """
        Create a FAISS vector store from the document chunks and save it to disk.
        """
        try:
            # Load and split document
            chunks = self.load_and_split_document()
            
            # Create FAISS vector store
            logger.info("Creating FAISS vector store...")
            start_time = time.time()
            self.vector_store = FAISS.from_documents(chunks, self.embeddings)
            create_time = time.time() - start_time
            logger.info(f"Created FAISS vector store in {create_time:.2f} seconds")
            
            # Save the vector store
            logger.info(f"Saving FAISS index to {FAISS_INDEX_PATH}")
            save_start_time = time.time()
            self.vector_store.save_local(FAISS_INDEX_PATH)
            save_time = time.time() - save_start_time
            logger.info(f"Saved FAISS index in {save_time:.2f} seconds")
            
            logger.info("FAISS vector store created and saved successfully")
        except Exception as e:
            logger.error(f"Error creating FAISS vector store: {e}")
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
        if self.vector_store is None:
            logger.warning("Vector store not initialized, attempting to load or create...")
            self._load_or_create_vector_store()
            
            if self.vector_store is None:
                logger.error("Failed to initialize vector store")
                return [{"error": "Vector store initialization failed"}]
        
        logger.info(f"Searching for: '{query}' with k={k}")
        
        try:
            # Search for similar documents
            start_time = time.time()
            results = self.vector_store.similarity_search_with_score(query, k=k)
            search_time = time.time() - start_time
            logger.info(f"Search completed in {search_time:.4f} seconds")
            
            # Format results
            formatted_results = []
            for i, (doc, score) in enumerate(results):
                logger.info(f"Result {i+1} - Score: {score:.4f}, Page: {doc.metadata.get('page', 'Unknown')}")
                formatted_results.append({
                    "content": doc.page_content,
                    "metadata": doc.metadata,
                    "score": score
                })
            
            return formatted_results
        except Exception as e:
            logger.error(f"Error in search: {e}")
            # Try alternative search method if the first one fails
            try:
                logger.info("Trying alternative search method")
                start_time = time.time()
                results = self.vector_store.similarity_search(query, k=k)
                search_time = time.time() - start_time
                logger.info(f"Alternative search completed in {search_time:.4f} seconds")
                
                # Format results without scores
                formatted_results = []
                for i, doc in enumerate(results):
                    logger.info(f"Result {i+1} - Page: {doc.metadata.get('page', 'Unknown')}")
                    formatted_results.append({
                        "content": doc.page_content,
                        "metadata": doc.metadata,
                        "score": 0.0  # Default score since we don't have actual scores
                    })
                
                return formatted_results
            except Exception as inner_e:
                logger.error(f"Error in alternative search: {inner_e}")
                return [{"error": f"Search failed: {str(inner_e)}"}]
    
    def get_document_count(self) -> int:
        """
        Get the number of documents in the vector store.
        
        Returns:
            Number of documents
        """
        if self.vector_store is None:
            logger.warning("Vector store not initialized, attempting to load or create...")
            self._load_or_create_vector_store()
            
            if self.vector_store is None:
                logger.error("Failed to initialize vector store")
                return -1
        
        try:
            # For FAISS, we can use the index_to_docstore_id dictionary to get the count
            count = len(self.vector_store.index_to_docstore_id)
            logger.info(f"Vector store contains {count} documents")
            return count
        except AttributeError as e:
            logger.error(f"Error getting document count: {e}")
            return -1


def main():
    """
    Main function to demonstrate the usage of the vector store.
    """
    # Create vector store
    logger.info("Initializing National AI Task Force Vector Store")
    try:
        vector_store = NationalAITaskForceVectorStore()
        
        # Example search
        query = "Who is on the task force team?"
        logger.info(f"Performing example search: '{query}'")
        results = vector_store.search(query)
        
        print(f"\nSearch results for query: '{query}'")
        print(f"Found {len(results)} results\n")
        
        for i, result in enumerate(results):
            if "error" in result:
                print(f"Error: {result['error']}")
                continue
                
            print(f"Result {i+1} (Score: {result['score']:.4f}):")
            print(f"Page: {result['metadata'].get('page', 'Unknown')}")
            print(f"Content: {result['content'][:200]}...\n")
    except Exception as e:
        logger.error(f"Error in main function: {e}")
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()