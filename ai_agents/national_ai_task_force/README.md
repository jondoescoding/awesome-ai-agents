# National AI Task Force Agent

This project provides a conversational AI agent that can search and analyze information from the National AI Task Force using LangGraph's ReAct agent architecture with GROQ models.

## Features

- **Conversational AI Agent**: Uses LangGraph's ReAct architecture with GROQ models
- **Semantic Search**: Searches the National AI Task Force information using vector embeddings in AstraDB
- **Conversation Memory**: Maintains context across multiple interactions
- **Streamlit Web Interface**: Provides a user-friendly interface for interacting with the agent
- **Error Handling**: Comprehensive error handling for robustness

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your API keys (see `.env.example` for reference)
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ASTRADB_TOKEN=your_astradb_application_token_here
   ASTRADB_ENDPOINT=your_astradb_api_endpoint_here
   ASTRADB_COLLECTION_NAME=national_ai_task_force
   ```

## Usage

### Running the Web Interface

Start the Streamlit web interface:

```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501` to interact with the agent.

### Using the Agent in Your Own Code

```python
from agent import NationalAITaskForceAgent

# Initialize the agent
agent = NationalAITaskForceAgent(model_name="qwen-qwq-32b")

# Ask a question
response = agent.chat(
    user_message="What are the key policy recommendations for AI governance?",
    thread_id="my_conversation"  # Optional conversation ID for memory
)

print(response)

# Reset a conversation thread
agent.reset_thread(thread_id="my_conversation")
```

### Using the Vector Store Directly

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

## Architecture

The project consists of the following components:

1. **Vector Store (`rag.py`)**: 
   - Cloud-based AstraDB vector store containing National AI Task Force information
   - Uses HuggingFace embeddings for semantic search
   - Handles document retrieval with similarity search

2. **Agent Implementation (`agent.py`)**:
   - Implements LangGraph ReAct agent architecture
   - Uses GROQ's LLaMA model for natural language understanding
   - Manages conversation memory and thread-based state

3. **Search Tools (`tools.py`)**:
   - Provides the search functionality that connects the agent to the vector store
   - Implements singleton pattern for vector store efficiency

4. **Web Interface (`app.py`)**:
   - Streamlit-based chat interface for user interactions
   - Manages session state and conversation history
   - Provides configuration options for model selection

## Customization

You can customize the following parameters:

### Vector Store (in `rag.py`)
- `CHUNK_SIZE`: The size of each document chunk (default: 1000)
- `CHUNK_OVERLAP`: The overlap between chunks (default: 200)
- `EMBEDDING_MODEL`: The HuggingFace model to use for embeddings (default: "sentence-transformers/all-mpnet-base-v2")

### Agent (in `agent.py`)
- `model_name`: The GROQ model to use (options: "qwen-qwq-32b", "mistral-saba-24b", "deepseek-r1-distill-llama-70b-specdec")
- System prompt for the agent can be modified in the `_initialize_agent` method

## Available GROQ Models

The agent supports the following GROQ models:

1. **Qwen QWQ 32B** (`qwen-qwq-32b`): Default model
2. **Mistral Saba 24B** (`mistral-saba-24b`): Alternative model
3. **Deepseek R1 Distill LLaMA 70B** (`deepseek-r1-distill-llama-70b-specdec`): Alternative model

## Requirements

- Python 3.8+
- LangChain and LangGraph
- GROQ API access
- Streamlit
- sentence-transformers
- PyTorch
- PyPDF 