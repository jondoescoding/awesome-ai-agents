"""
National AI Task Force Agent using LangGraph and GROQ models

This module implements a conversational agent that can search and analyze 
information from the National AI Task Force documents using LangGraph's 
pre-built ReAct agent with GROQ models.
"""

import logging
import os
from typing import List, Dict, Any

# LangChain and LangGraph imports
from langchain_core.messages import AIMessage, HumanMessage
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv

# Import the search tool
from tools import search_national_ai_task_force

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class NationalAITaskForceAgent:
    """
    A conversational agent that can search and analyze information from 
    the National AI Task Force documents using LangGraph's pre-built ReAct agent.
    """
    
    # Available models from GROQ
    AVAILABLE_MODELS = {
        "qwen-qwq-32b": "Qwen QWQ 32B",
        "mistral-saba-24b": "Mistral Saba 24B",
    }
    
    def __init__(self, model_name: str = "qwen-qwq-32b"):
        """
        Initialize the agent with the specified model.
        
        Args:
            model_name: The GROQ model to use (default: qwen-qwq-32b)
        """
        self.model_name = model_name
        self.agent = None
        self.memory_saver = None
        
        # Initialize the agent
        try:
            self._initialize_agent()
            logger.info(f"Agent initialized with model {model_name}")
        except Exception as e:
            logger.error(f"Error initializing agent: {e}")
            raise RuntimeError(f"Failed to initialize the agent: {e}")
    
    def _initialize_agent(self) -> None:
        """
        Initialize the LangGraph pre-built ReAct agent with the GROQ model.
        """
        try:
            # Get API key from environment variable
            api_key = os.getenv("GROQ_API_KEY")
            if not api_key:
                logger.error("GROQ_API_KEY environment variable not set")
                raise ValueError("GROQ_API_KEY environment variable not set")
            
            # Initialize the GROQ model
            logger.info(f"Initializing GROQ model: {self.model_name}")
            llm = ChatGroq(
                model_name=self.model_name,
                groq_api_key=api_key,
                temperature=0.5,
                streaming=True
            )
            
            # Define the system prompt for the agent
            # This prompt instructs the agent to use the search results as context
            system_prompt = """You are a helpful AI assistant for the National AI Task Force. You will be asked question question about the National AI Task Force and other general queries. In relation to the National AI Task Force use: search_national_ai_task_force. Everything else should be answered normally. Even though it won't be said specifically in many of the queries you are being asked about the document unless told otherwise. We are based on Jamaica.
            
            When using the search tool:
            1. Use the search results as your primary source of information
            2. If the search results don't contain enough information to answer fully, acknowledge this limitation
            3. Be thorough and informative in your responses, but maintain a conversational and helpful tone
            4. Do not reference the search process in your final response (e.g., don't say "According to the search results...")
            5. If you don't know the answer or can't find relevant information, be honest about it
            """
            
            # Initialize the memory saver for conversation history
            logger.info("Initializing conversation memory")
            self.memory_saver = InMemorySaver()
            
            # Create the pre-built ReAct agent
            logger.info("Creating pre-built ReAct agent with the search tool")
            self.agent = create_react_agent(
                llm,
                [search_national_ai_task_force],
                prompt=system_prompt,
                checkpointer=self.memory_saver,
            )
            
            logger.info("Agent successfully created")
            
        except Exception as e:
            logger.error(f"Error in _initialize_agent: {e}")
            raise
    
    def _get_or_create_thread(self, thread_id: str) -> str:
        """
        Get or create a conversation thread.
        
        Args:
            thread_id: A unique identifier for the conversation thread
            
        Returns:
            The thread ID
        """
        try:
            # With InMemorySaver in LangGraph, we don't need to explicitly check
            # if a thread exists. When we invoke the agent with a new thread_id,
            # LangGraph will automatically create it if it doesn't exist.
            logger.info(f"Using conversation thread: {thread_id}")
            return thread_id
        except Exception as e:
            logger.error(f"Error in _get_or_create_thread: {e}")
            raise RuntimeError(f"Failed to create or get thread: {e}")
    
    def chat(self, user_message: str, thread_id: str = "default") -> str:
        """
        Process a user message and return the agent's response.
        
        Args:
            user_message: The user's message
            thread_id: A unique identifier for the conversation thread (default: "default")
            
        Returns:
            The agent's response as a string
        """
        if not self.agent:
            logger.error("Agent not initialized")
            raise RuntimeError("Agent not initialized. Please check logs for details.")
        
        try:
            # Get thread ID
            thread_id = self._get_or_create_thread(thread_id)
            
            # Create input for the agent
            logger.info(f"Processing user message in thread {thread_id}: {user_message}")
            human_message = HumanMessage(content=user_message)
            
            # Run the agent with thread-specific memory
            config = {"configurable": {"thread_id": thread_id}}
            response = self.agent.invoke({"messages": [human_message]}, config=config)
            
            # Extract the assistant's response
            messages = response.get("messages", [])
            if not messages:
                logger.warning("No messages returned from agent")
                return "I'm sorry, I couldn't process your request. Please try again."
            
            # Get the last AI message
            for message in reversed(messages):
                if isinstance(message, AIMessage):
                    logger.info(f"Agent response generated successfully")
                    return message.content
            
            logger.warning("No AI message found in response")
            return "I'm sorry, I couldn't generate a response. Please try again."
            
        except Exception as e:
            logger.error(f"Error in chat: {e}")
            return f"I'm sorry, an error occurred: {str(e)}"
    
    def reset_thread(self, thread_id: str = "default") -> None:
        """
        Reset a conversation thread, clearing its history.
        
        Args:
            thread_id: The thread ID to reset (default: "default")
        """
        # In LangGraph, we can't directly delete threads with InMemorySaver
        # as the API doesn't expose this functionality in a straightforward way.
        # The best approach is to simply use a new thread_id when you want to start
        # a fresh conversation.
        logger.info(f"Note: In this version, resetting thread {thread_id} is not directly supported.")
        logger.info(f"To start a new conversation, please use a new thread ID.")


def main():
    """
    Main function for testing the agent.
    """
    try:
        logger.info("Initializing agent for testing")
        agent = NationalAITaskForceAgent()
        
        # Test the agent with a sample question
        test_question = "What are the primary recommendations of the National AI Task Force?"
        logger.info(f"Testing agent with question: {test_question}")
        
        response = agent.chat(test_question)
        print(f"\nQuestion: {test_question}")
        print(f"Response: {response}\n")
        
    except Exception as e:
        logger.error(f"Error in main: {e}")
        print(f"Error: {e}")
