import streamlit as st
from phi.agent import Agent
from agents.revenue_agent import revenue_agent
from agents.chain_agent import chain_agent

# Initialize individual agents
revenue_assistant = Agent(agent=revenue_agent, name="Revenue Assistant")
chain_assistant = Agent(agent=chain_agent, name="Chain Assistant")

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

# Page config
st.set_page_config(
    page_title="Curve Protocol Agent Chat",
    page_icon="🦙",
    layout="wide"
)

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

# Sidebar
with st.sidebar:
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

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Main chat interface
st.title("🦙 Curve Protocol Agent Chat")

# Chat input at the bottom
chat_container = st.container()
input_container = st.container()

with input_container:
    prompt = st.chat_input("What would you like to know?")

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