"""
Streamlit application for the National AI Task Force Agent

This module provides a web interface for interacting with the 
National AI Task Force Agent using Streamlit.
"""

import os
import logging
import streamlit as st
from typing import Dict, Any, List, Optional
import uuid  # This is the built-in uuid module, we don't need uuid6

# Import the agent class
from agent import NationalAITaskForceAgent

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Page configuration
st.set_page_config(
    page_title="National AI Task Force Agent",
    page_icon="🤖",
    layout="wide",
)

# Session state initialization
def initialize_session_state():
    """Initialize session state variables if they don't exist."""
    if "agent" not in st.session_state:
        try:
            logger.info("Initializing agent in session state")
            st.session_state.agent = NationalAITaskForceAgent()
            logger.info("Agent initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing agent: {e}")
            st.error(f"Failed to initialize agent: {e}")
            st.session_state.agent = None
    
    if "conversation_id" not in st.session_state:
        # Generate a unique conversation ID
        st.session_state.conversation_id = str(uuid.uuid4())
        logger.info(f"Generated new conversation ID: {st.session_state.conversation_id}")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

def display_chat_message(role, content):
    """Display a chat message in the UI."""
    with st.chat_message(role):
        st.markdown(content)

# Initialize session state
initialize_session_state()

# App header
st.title("National AI Task Force Agent")
st.markdown("""
This application allows you to interact with an AI agent that can search and analyze 
information from the National AI Task Force documents. Ask any question related to 
the Task Force's work, recommendations, or findings.
""")

# Display chat messages from history
for message in st.session_state.messages:
    display_chat_message(message["role"], message["content"])

# Chat input
if user_input := st.chat_input("Ask a question about the National AI Task Force"):
    # Check if agent is initialized
    if st.session_state.agent is None:
        st.error("Agent is not initialized. Please refresh the page and try again.")
    else:
        try:
            # Add user message to chat history and display it
            st.session_state.messages.append({"role": "user", "content": user_input})
            display_chat_message("user", user_input)
            
            # Display thinking indicator
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    # Get response from agent
                    logger.info(f"Sending user input to agent: {user_input}")
                    response = st.session_state.agent.chat(
                        user_message=user_input,
                        thread_id=st.session_state.conversation_id
                    )
                    logger.info("Received response from agent")
                    
                    # Display assistant response
                    st.markdown(response)
            
            # Add assistant message to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
            
        except Exception as e:
            logger.error(f"Error processing user input: {e}")
            st.error(f"An error occurred: {str(e)}")

# Sidebar
with st.sidebar:
    st.header("Options")
    
    # Model selection
    model_options = ["llama-3.1-8b-instant", "llama3-70b-8192", "llama3-8b-8192"]
    selected_model = st.selectbox(
        "Select GROQ LLaMA Model",
        options=model_options,
        index=0,
    )
    
    # Button to create a new conversation
    if st.button("New Conversation"):
        try:
            logger.info("Creating new conversation")
            # Generate a new conversation ID
            st.session_state.conversation_id = str(uuid.uuid4())
            logger.info(f"Generated new conversation ID: {st.session_state.conversation_id}")
            
            # Reset the message history in the UI
            st.session_state.messages = []
            
            # Instead of trying to reset the thread, we'll just use the new conversation ID
            # which will effectively create a new conversation thread
            
            st.success("Started a new conversation!")
            st.rerun()
        except Exception as e:
            logger.error(f"Error creating new conversation: {e}")
            st.error(f"Failed to create new conversation: {e}")
    
    # API key input
    api_key = st.text_input(
        "GROQ API Key",
        type="password",
        placeholder="Enter your GROQ API key",
        value=os.getenv("GROQ_API_KEY", "")
    )
    
    # Button to update API key
    if st.button("Update API Key"):
        if api_key:
            logger.info("Updating GROQ API key")
            os.environ["GROQ_API_KEY"] = api_key
            
            # Reinitialize the agent with the new API key
            try:
                logger.info("Reinitializing agent with new API key")
                st.session_state.agent = NationalAITaskForceAgent(model_name=selected_model)
                st.success("API key updated and agent reinitialized!")
            except Exception as e:
                logger.error(f"Error reinitializing agent: {e}")
                st.error(f"Failed to reinitialize agent: {e}")
        else:
            st.warning("Please enter an API key.")
    
    # Display the current conversation ID
    st.text(f"Conversation ID: {st.session_state.conversation_id[:8]}...")
    
    # Add information about the agent
    st.markdown("---")
    st.markdown("""
    ### About
    
    This agent uses LangGraph's ReAct architecture with GROQ's LLaMA model to 
    provide information and analysis based on the National AI Task Force documents.
    
    It maintains conversation context across multiple interactions and uses 
    semantic search to find relevant information in the documents.
    """)

if __name__ == "__main__":
    # This will only run when the script is executed directly
    pass
