# National AI Task Force Agent

This project provides a conversational AI agent that can search and analyze information from the National AI Task Force PDF document using LangGraph's ReAct agent architecture with GROQ's LLaMA model.

## Features

- **Conversational AI Agent**: Uses LangGraph's ReAct architecture with GROQ's LLaMA model
- **Semantic Search**: Searches the National AI Task Force document using vector embeddings
- **Conversation Memory**: Maintains context across multiple interactions
- **Streamlit Web Interface**: Provides a user-friendly interface for interacting with the agent
- **Error Handling**: Comprehensive error handling for robustness

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your GROQ API key (see `.env.example` for reference)
   ```
   GROQ_API_KEY=your_groq_api_key_here
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
agent = NationalAITaskForceAgent(model_name="llama3")

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

The project uses the following architecture:

1. **Vector Store**: An in-memory vector store created from the National AI Task Force PDF document
   - Uses "sentence-transformers/all-mpnet-base-v2" model for embeddings
   - Splits the document into chunks for better search results

2. **LangGraph ReAct Agent**: A conversational agent that can search and analyze information
   - Uses GROQ's LLaMA model for natural language understanding
   - Uses the prebuilt ReAct agent from LangGraph for tool interaction
   - Maintains conversation memory across interactions

3. **Streamlit Web Interface**: A user-friendly interface for interacting with the agent
   - Chat interface for conversations
   - Options to select different models and start new conversations

## Customization

You can customize the following parameters:

### Vector Store (in `rag.py`)
- `CHUNK_SIZE`: The size of each document chunk (default: 1000)
- `CHUNK_OVERLAP`: The overlap between chunks (default: 200)
- `EMBEDDING_MODEL`: The HuggingFace model to use for embeddings (default: "sentence-transformers/all-mpnet-base-v2")

### Agent (in `agent.py`)
- `model_name`: The GROQ model to use (options: "llama3", "llama3-70b", "llama3-8b")
- System prompt for the agent can be modified in the `_initialize_agent` method

## Requirements

- Python 3.8+
- LangChain and LangGraph
- GROQ API access
- Streamlit
- sentence-transformers
- PyTorch
- PyPDF 