"""
Streamlit application for the National AI Task Force Agent

This module provides a web interface for interacting with the 
National AI Task Force Agent using Streamlit.
"""
import logging
import streamlit as st
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

def on_model_change():
    """Handle model change event."""
    try:
        selected_model_name = st.session_state.selected_model
        logger.info(f"Changing model to {selected_model_name}")
        
        # Reinitialize the agent with the new model
        st.session_state.agent = NationalAITaskForceAgent(model_name=selected_model_name)
        
        # Generate a new conversation ID
        st.session_state.conversation_id = str(uuid.uuid4())
        logger.info(f"Generated new conversation ID: {st.session_state.conversation_id}")
        
        # Reset the message history in the UI
        st.session_state.messages = []
        
        # Show success message
        st.success(f"Model changed to {NationalAITaskForceAgent.AVAILABLE_MODELS[selected_model_name]}!")
        
    except Exception as e:
        logger.error(f"Error changing model: {e}")
        st.error(f"Failed to change model: {e}")

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
user_input = st.chat_input("Ask a question about the National AI Task Force")

if user_input:
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
    
    # Model selection with automatic change
    model_options = NationalAITaskForceAgent.AVAILABLE_MODELS
    
    st.selectbox(
        "Select GROQ Model",
        options=list(model_options.keys()),
        format_func=lambda x: model_options[x],
        index=0,
        key="selected_model",
        on_change=on_model_change
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
            
            st.success("Started a new conversation!")
            st.rerun()
        except Exception as e:
            logger.error(f"Error creating new conversation: {e}")
            st.error(f"Failed to create new conversation: {e}")
    
    # Display the current conversation ID
    st.text(f"Conversation ID: {st.session_state.conversation_id[:8]}...")
    
    # Add custom CSS for the creator section
    st.markdown("""
    <style>
    .creator-section {
        background-color: transparent;
        border: 3px solid #FFFF00;
        padding: 15px;
        border-radius: 5px;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .creator-section h3 {
        font-weight: bold;
    }
    .creator-section a {
        display: block;
        margin-bottom: 8px;
        text-decoration: none;
    }
    .creator-section a:hover {
        text-decoration: underline;
    }
    .creator-links {
        margin-top: 10px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Add information about the creator with custom styling
    st.markdown("---")
    st.markdown("""
    <div class="creator-section">
    <h3>Created by Jonathan White</h3>
    
    <div class="creator-links">
    <a href="https://www.linkedin.com/in/jonathanwhite-jm/" target="_blank">
    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="20"/> LinkedIn
    </a>
    <a href="https://twitter.com/jondoescoding" target="_blank">
    <img src="https://cdn-icons-png.flaticon.com/512/733/733579.png" width="20"/> Twitter
    </a>
    <a href="https://nightshadeai.xyz/" target="_blank">
    <img src="https://cdn-icons-png.flaticon.com/512/1006/1006771.png" width="20"/> Website
    </a>
    </div>
    
    <i>I transform</i> complex ideas into <b>intuitive digital experiences</b>.<br>
    • Building intelligent <b>chatbots</b> that engage users, online 24/7 and are accurate. <br>
    • Creating <b>rapid prototypes</b> to validate concepts using lovable, base44 and rork. (Skip the Figma board). <br>
    <i>Technology that works like magic, feels natural, and drives results.</i>
    </div>
    """, unsafe_allow_html=True)
    
    # Add information about the agent
    st.markdown("---")
    st.markdown("""
    ### About
    
    This agent uses LangGraph's ReAct architecture with GROQ models to 
    provide information and analysis based on the National AI Task Force documents.
    
    It maintains conversation context across multiple interactions and uses 
    semantic search to find relevant information in the documents.
    """)
