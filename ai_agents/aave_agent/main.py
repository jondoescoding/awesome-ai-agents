"""
Main script
-------------------
What:
This script acts as the entrypoint to the AI Agent. Within you'll find that it provides functionality to be able to connect to a Web3 endpoint and have the AI agent act on it.


"""
# Python Built In Libraries
from typing import Annotated # used to set additional metadata for a variable  
from typing_extensions import TypedDict # a type that allows you to define dictionaries with specific key-value types


# Langchain / Langraphpip 
from langgraph.graph import (StateGraph, # data structure which represents the current snapshot of an application 
                             START # type of node (a python function which has some kind of logic) which takes user input and sends it into the graph 
                            )
from langgraph.graph.message import add_messages # appends messages to the end of the attribute it was assigned to
from langgraph.prebuilt import (ToolNode, # a pre-built component and node whichs runs the tools called in the last AIMessage 
                                tools_condition # a pre-built component and node which uses the conditional_edge to route to the ToolNode if the last message has tool calls. Otherwise, route to the end.
                                )
from langchain_groq import ChatGroq


# User Interface
import streamlit as st


# Local Imports


"""
UI -> Streamlit 
Here we create the sidebar and logic for handling the API key
It is created here eariler since we can't use LLM variable before it is created as without the the API the if statement will move into the warning + stop code scope  
"""

with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", key="chatbot_api_key", type="password")
    "[Get an Groq API key](https://console.groq.com/keys)"
    
    private_key = st.text_input("Private Key", key="private_key", type="password")
    "[Create a private key with Rabby Wallet](https://rabby.io/)"

    "[![View the source code](https://badgen.net/static/Github/Repository/black?icon=github)](https://github.com/jondoescoding/awesome-ai-agents/tree/main/ai_agents/coingecko_agent)"

    
if not groq_api_key:
    st.warning(body="API key is not set. Please set the Groq API key.")
    st.stop()
if not private_key:
    st.warning(body="Private key is not set. Please set your wallet private key.")
    st.stop()

llm = ChatGroq(model="llama3-70b-8192", api_key=groq_api_key)


