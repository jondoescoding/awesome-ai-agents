import streamlit as st

# Page config must be the first Streamlit command
st.set_page_config(
    page_title="Curve Protocol Agent Chat",
    page_icon="🦙",
    layout="wide"
)

from phi.agent import Agent
from agents.revenue_agent import revenue_agent
from agents.chain_agent import chain_agent
import os

# Custom CSS
st.markdown("""
<style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .social-links {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }
    .social-links a {
        text-decoration: none;
        color: #1DA1F2;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for API key if not present
if "openai_api_key" not in st.session_state:
    st.session_state.openai_api_key = ""

# Sidebar
with st.sidebar:
    st.title("🔑 API Configuration")
    api_key = st.text_input(
        "Enter your OpenAI API key",
        type="password",
        value=st.session_state.openai_api_key,
        help="Get your API key from https://platform.openai.com/account/api-keys"
    )
    
    # Update session state when API key changes
    if api_key != st.session_state.openai_api_key:
        st.session_state.openai_api_key = api_key
        # Set environment variable for OpenAI
        os.environ["OPENAI_API_KEY"] = api_key
    
    st.divider()
    st.title("🦙 About")
    st.markdown("""
    Chat with a LlamaIndex-powered agent that can help you with:
    - Curve Protocol Revenue & Fees
    - Chain Transactions & Analytics
    """)
    
    st.markdown("### 🔗 Connect")
    st.markdown("""
    <div class="social-links">
        <a href="https://twitter.com/jondoescoding" target="_blank">
            <img src="https://img.shields.io/twitter/follow/jondoescoding?style=social" alt="Twitter Follow">
        </a>
        <a href="https://github.com/jondoescoding/awesome-ai-agents" target="_blank">
            <img src="https://img.shields.io/github/stars/jondoescoding/awesome-ai-agents?style=social" alt="GitHub stars">
        </a>
    </div>
    """, unsafe_allow_html=True)

    # Agent Selection
    st.markdown("### 🤖 Select Agent")
    agent_type = st.radio(
        "Choose which agent to interact with:",
        ["Revenue Agent", "Chain Agent", "Multi-Agent"],
        key="agent_selection"
    )
    
    # Move examples to sidebar
    st.markdown("### 📝 Example Questions")
    if st.session_state.agent_selection == "Revenue Agent":
        st.markdown("""
        Try asking:
        - What are the current fee distributions?
        - Show me the weekly CrvUSD fees
        - What are the pending pool fees?
        """)
    elif st.session_state.agent_selection == "Chain Agent":
        st.markdown("""
        Try asking:
        - What is the last 7 days of transactions for Ethereum?
        - Show me the current lending chains
        - How many users are on each chain?
        """)
    else:  # Multi-Agent mode
        st.markdown("""
        Try asking complex questions that combine both agents:
        - Compare ETH chain fees to CrvUSD fees
        - What's the relationship between user growth and revenue?
        - Show me high-fee pools and their transaction volumes
        """)

# Initialize individual agents only if API key is provided
if st.session_state.openai_api_key:
    revenue_assistant = revenue_agent
    chain_assistant = chain_agent

    # Create team as a single agent with multiple sub-agents
    curve_team = Agent(
        name="Curve Analysis Team",
        team=[revenue_assistant, chain_assistant],
        instructions=[
            "First, use the revenue agent to analyze fee and revenue data.",
            "Then, use the chain agent to analyze blockchain transactions and metrics.",
            "Combine insights from both agents to provide comprehensive analysis.",
            "Important: When analyzing fees, always correlate with chain activity.",
            "Finally, provide a clear summary that connects revenue and chain insights."
        ],
        show_tool_calls=True,
        markdown=True
    )

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Main chat interface
st.title("🦙 Curve Protocol Agent Chat")

# Chat input at the bottom
chat_container = st.container()
input_container = st.container()

with input_container:
    # Only enable chat input if API key is provided
    if st.session_state.openai_api_key:
        prompt = st.chat_input("What would you like to know?")
    else:
        st.error("Please enter your OpenAI API key in the sidebar to start chatting.")
        prompt = None

with chat_container:
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with chat_container:
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get agent response
        with st.chat_message("assistant"):
            if not st.session_state.openai_api_key:
                st.error("Please enter your OpenAI API key in the sidebar to get a response.")
            else:
                message_placeholder = st.empty()
                full_response = ""
                
                # Select the appropriate assistant based on user selection
                if st.session_state.agent_selection == "Multi-Agent":
                    with st.spinner("Agents collaborating..."):
                        response_stream = curve_team.run(prompt, stream=True)
                        for response in response_stream:
                            full_response += str(response.content)
                            message_placeholder.markdown(full_response + "▌")
                else:
                    selected_assistant = revenue_assistant if st.session_state.agent_selection == "Revenue Agent" else chain_assistant
                    with st.spinner("Thinking..."):
                        response_stream = selected_assistant.run(prompt, stream=True)
                        for response in response_stream:
                            full_response += str(response.content)
                            message_placeholder.markdown(full_response + "▌")
                
                message_placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response}) 