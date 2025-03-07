# National AI Task Force Vector Search

This project creates an in-memory vector store from the National AI Task Force PDF document and provides functionality to search through it using semantic similarity.

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the main script to create the vector store and perform a sample search:

```bash
python rag.py
```

### Using the Vector Store in Your Own Code

```python
from rag import NationalAITaskForceVectorStore

# Initialize the vector store
vector_store = NationalAITaskForceVectorStore()

# Create the vector store
vector_store.create_vector_store()

# Search for documents
query = "What are the key policy recommendations for AI governance?"
results = vector_store.search(query, k=5)  # k is the number of results to return

# Process the results
for result in results:
    print(f"Content: {result['content']}")
    print(f"Metadata: {result['metadata']}")
    print(f"Score: {result['score']}")
```

## Features

- **PDF Loading**: Loads the National AI Task Force PDF document using PyPDFLoader
- **Text Splitting**: Splits the document into chunks for better search results
- **HuggingFace Embeddings**: Uses the "sentence-transformers/all-mpnet-base-v2" model for embeddings
- **In-Memory Vector Store**: Stores document vectors in memory for fast retrieval
- **Similarity Search**: Searches for documents similar to a query
- **Detailed Logging**: Provides comprehensive logging of operations

## Customization

You can customize the following parameters in the `rag.py` file:

- `CHUNK_SIZE`: The size of each document chunk (default: 1000)
- `CHUNK_OVERLAP`: The overlap between chunks (default: 200)
- `EMBEDDING_MODEL`: The HuggingFace model to use for embeddings (default: "sentence-transformers/all-mpnet-base-v2")

## Requirements

- Python 3.8+
- LangChain
- sentence-transformers
- PyTorch
- PyPDF 