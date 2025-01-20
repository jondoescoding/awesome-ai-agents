"""
Main script
-------------------
What:
This script acts as the entrypoint to the AI Agent. Within you'll find that it provides functionality to be able to connect to a Web3 endpoint and have the AI agent act on it.


"""
# Python Built In Libraries
from typing import Annotated, List # used to set additional metadata for a variable  
from typing_extensions import TypedDict # a type that allows you to define dictionaries with specific key-value types
import os

# Langchain / Langraphpip 
from langgraph.graph import (StateGraph, # data structure which represents the current snapshot of an application 
                             START # type of node (a python function which has some kind of logic) which takes user input and sends it into the graph 
                            )
from langgraph.graph.message import add_messages # appends messages to the end of the attribute it was assigned to
from langgraph.prebuilt import (ToolNode, # a pre-built component and node whichs runs the tools called in the last AIMessage 
                                tools_condition # a pre-built component and node which uses the conditional_edge to route to the ToolNode if the last message has tool calls. Otherwise, route to the end.
                                )
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, BaseMessage

# Tools
from tools import get_token_balance, lend_crypto, borrow_crypto
from web3 import Web3

# User Interface
import streamlit as st

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(os.getenv("RPC_URL")))

with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", key="chatbot_api_key", type="password")
    "[Get an Groq API key](https://console.groq.com/keys)"
    
    private_key = st.text_input("Private Key", key="private_key", type="password")
    "[Create a private key with Rabby Wallet](https://rabby.io/)"

    if st.button("Clear Chat History"):
        st.session_state.messages = [{"role": "assistant", "content": "Hello! I'm your AAVE DeFi assistant. I can help you check token balances, lend, and borrow crypto. How can I assist you today?"}]
        st.rerun()

    "[![View the source code](https://badgen.net/static/Github/Repository/black?icon=github)](https://github.com/jondoescoding/awesome-ai-agents/tree/main/ai_agents/aave_agent)"

    
if not groq_api_key:
    st.warning(body="API key is not set. Please set the Groq API key.")
    st.stop()
if not private_key:
    st.warning(body="Private key is not set. Please set your wallet private key.")
    st.stop()

# Create account from private key
account = web3.eth.account.from_key(private_key)
user_address = account.address

# System prompt with token information and user's address
SYSTEM_PROMPT = f"""You are an AAVE DeFi assistant that helps users interact with the AAVE protocol on Ethereum.
You are connected to the wallet address: {user_address}

You have access to the following tokens and their addresses:

- USDC (USD Coin): 0x94a9D9AC8a22534E3FaCa9F4e7F2E2cf85d5E4C8
- DAI (Dai Stablecoin): 0xFF34B3d4Aee8ddCd6F9AFFFB6Fe49bD371b8a357 
- WBTC (Wrapped Bitcoin): 0x29f2D40B0605204364af54EC677bD022dA425d03 
- USDT (Tether USD): 0xaA8E23Fb1079EA71e0a56F48a2aA51851D8433D0

You can help users:
1. Check their token balances of ONLY the above contracts. Let the user know what tokens are available.
2. Lend their tokens to earn interest
3. Borrow tokens against their collateral

Always use the exact token addresses provided above when helping users interact with the protocol."""

llm = ChatGroq(model="llama3-70b-8192", api_key=groq_api_key)

####
# LOGIC - LangGraph Setup
####

# Initialize LLM and Tools
tools = [get_token_balance, lend_crypto, borrow_crypto]
llm_with_tools = llm.bind_tools(tools=tools)

# State Management
class State(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]

# Graph Builder Setup
graph_builder = StateGraph(State)

# Chatbot Function
def chatbot(state: State):
    # Get all messages including history
    messages = state["messages"]
    
    # Add system message if it's not already in the messages
    if not any(isinstance(msg, SystemMessage) for msg in messages):
        messages = [SystemMessage(content=SYSTEM_PROMPT)] + messages
    
    # Get response from LLM with full conversation history
    response = llm_with_tools.invoke(messages)
    
    return {"messages": [response]}

# Node Configuration
tools_node = ToolNode(tools=tools)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", tools_node)

# Edge Configuration
graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge(START, "chatbot")

# Compile Graph
graph = graph_builder.compile()

####
# UI - Streamlit Chat Interface
####
st.title("🏦💬 AAVE DeFi Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hello! I'm your AAVE DeFi assistant. I can help you check token balances, lend, and borrow crypto. How can I assist you today?"}]

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Handle user input
if prompt := st.chat_input():
    if not groq_api_key:
        st.info("Please add your Groq API key to continue.")
        st.stop()

    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Convert chat history to LangChain message format
    from langchain_core.messages import HumanMessage, AIMessage
    history = []
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            history.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            history.append(AIMessage(content=msg["content"]))

    # Get AI response with a loading spinner
    with st.spinner("Thinking..."):
        response = graph.invoke({"messages": history})
        msg = response["messages"][-1].content

    # Add AI response to chat
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)


