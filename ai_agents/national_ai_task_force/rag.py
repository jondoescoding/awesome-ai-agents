"""
Vector Search over National AI Task Force PDF Document

This script creates an in-memory vector store from the National AI Task Force PDF document
and provides functionality to search through it using semantic similarity.
"""

import os
import logging
from typing import List, Dict, Any

# LangChain imports for document loading and processing
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
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
EMBEDDING_MODEL = "sentence-transformers/all-mpnet-base-v2"

class NationalAITaskForceVectorStore:
    """
    A class to handle the creation and querying of an in-memory vector store
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
        
        # Initialize in-memory vector store
        self.vector_store = None
    
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
        Create an in-memory vector store from the document chunks.
        """
        # Load and split document
        chunks = self.load_and_split_document()
        
        # Create in-memory vector store
        logger.info("Creating in-memory vector store...")
        self.vector_store = InMemoryVectorStore(embedding=self.embeddings)
        
        # Add documents to vector store
        logger.info(f"Adding {len(chunks)} document chunks to vector store")
        self.vector_store.add_documents(chunks)
        
        logger.info("In-memory vector store created successfully")
    
    def search(self, query: str, k: int = 5) -> List[Dict[str, Any]]:
        """
        Search the vector store for documents similar to the query.
        
        Args:
            query: The search query
            k: Number of results to return
            
        Returns:
            List of documents with their similarity scores
        """
        if self.vector_store is None:
            logger.info("Vector store not initialized, creating now...")
            self.create_vector_store()
        
        logger.info(f"Searching for: '{query}' with k={k}")
        
        # Search for similar documents
        results = self.vector_store.similarity_search_with_score(query, k=k)
        
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
    
    def get_document_count(self) -> int:
        """
        Get the number of documents in the vector store.
        
        Returns:
            Number of documents
        """
        if self.vector_store is None:
            logger.info("Vector store not initialized, creating now...")
            self.create_vector_store()
        
        count = len(self.vector_store.docstore._dict)
        logger.info(f"Vector store contains {count} documents")
        return count


def main():
    """
    Main function to demonstrate the usage of the vector store.
    """
    # Create vector store
    logger.info("Initializing National AI Task Force Vector Store")
    vector_store = NationalAITaskForceVectorStore()
    vector_store.create_vector_store()
    
    # Example search
    query = "What are the key policy recommendations for AI governance in Jamaica?"
    logger.info(f"Performing example search: '{query}'")
    results = vector_store.search(query)
    
    print(f"\nSearch results for query: '{query}'")
    print(f"Found {len(results)} results\n")
    
    for i, result in enumerate(results):
        print(f"Result {i+1} (Score: {result['score']:.4f}):")
        print(f"Page: {result['metadata'].get('page', 'Unknown')}")
        print(f"Content: {result['content'][:200]}...\n")


if __name__ == "__main__":
    main()
