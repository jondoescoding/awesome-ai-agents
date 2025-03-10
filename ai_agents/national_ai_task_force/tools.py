"""
Tools for the National AI Task Force Agent

This module contains tools that can be used by an agent to interact with
the National AI Task Force PDF document.
"""

import logging
import time
from typing import List, Dict, Any

from langchain_core.tools import tool
from rag import NationalAITaskForceVectorStore

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize the vector store as a global variable to avoid reloading
# the PDF document for each tool call
_vector_store = None

def get_vector_store() -> NationalAITaskForceVectorStore:
    """
    Get or initialize the vector store.
    
    Returns:
        An initialized NationalAITaskForceVectorStore instance
    """
    global _vector_store
    
    if _vector_store is None:
        logger.info("Initializing vector store for the first time")
        try:
            start_time = time.time()
            _vector_store = NationalAITaskForceVectorStore()
            init_time = time.time() - start_time
            logger.info(f"Vector store initialized in {init_time:.2f} seconds with {_vector_store.get_document_count()} documents")
        except Exception as e:
            logger.error(f"Error initializing vector store: {e}")
            raise RuntimeError(f"Failed to initialize vector store: {e}")
    
    return _vector_store

@tool
def search_national_ai_task_force(query: str, k: int = 5) -> List[Dict[str, Any]]:
    """
    Search the National AI Task Force PDF document for information related to the query.
    
    Args:
        query: The search query to find relevant information in the document
        k: Number of results to return (default: 5)
        
    Returns:
        A list of document chunks that match the query, with their metadata and similarity scores
    """
    logger.info(f"Tool called with query: '{query}', k={k}")
    
    try:
        # Get or initialize the vector store
        vector_store = get_vector_store()
        
        # Search for documents
        start_time = time.time()
        logger.info(f"Searching vector store for: '{query}'")
        results = vector_store.search(query, k=k)
        search_time = time.time() - start_time
        
        logger.info(f"Found {len(results)} results for query: '{query}' in {search_time:.4f} seconds")
        return results
    
    except FileNotFoundError as e:
        logger.error(f"PDF document not found: {e}")
        return [{"error": f"PDF document not found: {e}"}]
    
    except Exception as e:
        logger.error(f"Error searching National AI Task Force document: {e}")
        return [{"error": f"Error searching National AI Task Force document: {e}"}]
