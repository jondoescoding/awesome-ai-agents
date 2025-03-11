"""
Vector Search over National AI Task Force Document using AstraDB

This script provides functionality to search through the National AI Task Force
information stored in AstraDB using semantic similarity.
"""

import os
import logging
from typing import List, Dict, Any
import time
import traceback

# LangChain imports for embeddings and vector store
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_astradb import AstraDBVectorStore

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants

CHUNK_SIZE = 2000
CHUNK_OVERLAP = 200
EMBEDDING_MODEL = "BAAI/bge-base-en-v1.5"

# AstraDB Configuration
ASTRA_DB_API_ENDPOINT = os.getenv("ASTRADB_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRADB_TOKEN")
ASTRA_DB_COLLECTION_NAME = "national_ai_task_force3"

class NationalAITaskForceVectorStore:
    """
    A class to handle querying of an AstraDB vector store
    containing National AI Task Force information.
    """
    
    def __init__(self, embedding_model: str = EMBEDDING_MODEL):
        """
        Initialize the vector store connection.
        
        Args:
            embedding_model: HuggingFace model to use for embeddings
        """
        logger.info("=" * 50)
        logger.info("INITIALIZING NATIONAL AI TASK FORCE VECTOR STORE")
        logger.info("=" * 50)
        
        self.embedding_model = embedding_model
        logger.info(f"Using embedding model: {self.embedding_model}")
        
        # Initialize embeddings
        try:
            start_time = time.time()
            self.embeddings = HuggingFaceEmbeddings(model_name=self.embedding_model)
            init_time = time.time() - start_time
            logger.info(f"Embeddings initialized in {init_time:.2f} seconds")
        except Exception as e:
            logger.error(f"Error initializing embeddings: {e}")
            logger.error(traceback.format_exc())
            raise RuntimeError(f"Failed to initialize embeddings: {e}")
        
        # Connect to AstraDB
        self._connect_to_vector_store()
    
    def _connect_to_vector_store(self) -> None:
        """
        Connect to the AstraDB vector store.
        """
        try:
            # Check if AstraDB credentials are available
            if not ASTRA_DB_API_ENDPOINT or not ASTRA_DB_APPLICATION_TOKEN:
                logger.error("AstraDB credentials not found")
                raise ValueError(
                    "AstraDB credentials not found. Please set ASTRADB_ENDPOINT and ASTRADB_TOKEN environment variables."
                )
            
            logger.info(f"Connecting to AstraDB collection: {ASTRA_DB_COLLECTION_NAME}")
            start_time = time.time()
            
            # Connect to AstraDB
            self.vector_store = AstraDBVectorStore(
                embedding=self.embeddings,
                collection_name=ASTRA_DB_COLLECTION_NAME,
                api_endpoint=ASTRA_DB_API_ENDPOINT,
                token=ASTRA_DB_APPLICATION_TOKEN,
            )
            
            connect_time = time.time() - start_time
            logger.info(f"Connected to AstraDB in {connect_time:.2f} seconds")
            
            # Get document count
            doc_count = self.get_document_count()
            logger.info(f"Collection has {doc_count} documents")
            
        except Exception as e:
            logger.error(f"Error connecting to AstraDB: {e}")
            logger.error(traceback.format_exc())
            raise RuntimeError(f"Failed to connect to AstraDB: {e}")
    
    def search(self, query: str, k: int = 10) -> List[Dict[str, Any]]:
        """
        Search the vector store for documents similar to the query.
        
        Args:
            query: The search query
            k: Number of results to return
            
        Returns:
            A list of document chunks with their metadata and similarity scores
        """
        try:
            logger.info(f"Searching for: '{query}' with k={k}")
            start_time = time.time()
            
            # Perform similarity search
            results = self.vector_store.similarity_search_with_score(query, k=k)
            
            search_time = time.time() - start_time
            logger.info(f"Search completed in {search_time:.4f} seconds")
            
            # Format results
            formatted_results = []
            for doc, score in results:
                # Convert to dictionary format
                result = {
                    "content": doc.page_content,
                    "metadata": doc.metadata,
                    "score": float(score)
                }
                formatted_results.append(result)
            
            logger.info(f"Returning {len(formatted_results)} results")
            return formatted_results
            
        except Exception as e:
            logger.error(f"Error searching vector store: {e}")
            logger.error(traceback.format_exc())
            raise RuntimeError(f"Search failed: {e}")
    
    def get_document_count(self) -> int:
        """
        Get the number of documents in the vector store.
        
        Returns:
            The number of documents
        """
        try:
            # Get document count from AstraDB
            count = self.vector_store.collection_count()
            return count
        except Exception as e:
            logger.error(f"Error getting document count: {e}")
            return 0


def main():
    """
    Main function for testing the vector store.
    """
    try:
        # Initialize the vector store
        vector_store = NationalAITaskForceVectorStore()
        
        # Test search
        test_query = "What are the key recommendations of the National AI Task Force?"
        results = vector_store.search(test_query, k=3)
        
        print(f"\nQuery: {test_query}")
        print(f"Found {len(results)} results\n")
        
        # Print results
        for i, result in enumerate(results):
            print(f"Result {i+1} (Score: {result['score']:.4f}):")
            print(f"Content: {result['content'][:200]}...\n")
            print(f"Metadata: {result['metadata']}\n")
            print("-" * 80)
        
    except Exception as e:
        logger.error(f"Error in main: {e}")
        print(f"Error: {e}")

#if __name__ == "__main__":
#    main()