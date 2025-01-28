import streamlit as st
from llama_index.core.agent.workflow import AgentWorkflow
from agents.revenue_agent import workflow as revenue_workflow
from agents.chain_agent import workflow as chain_workflow

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
        ["Revenue Agent", "Chain Agent"],
        key="agent_selection"
    )

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Main chat interface
st.title("🦙 Curve Protocol Agent Chat")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get agent response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Select the appropriate workflow based on user selection
        selected_workflow = revenue_workflow if st.session_state.agent_selection == "Revenue Agent" else chain_workflow
        
        # Stream the agent's response
        handler = selected_workflow.run(user_msg=prompt)
        
        with st.spinner("Thinking..."):
            for event in handler.sync_events():
                if hasattr(event, "delta"):
                    full_response += str(event.delta)
                    message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})

# Footer with agent context
st.markdown("---")
current_agent = "Revenue Agent" if st.session_state.agent_selection == "Revenue Agent" else "Chain Agent"
st.markdown(f"Currently using: {current_agent} 🦙")

# Add helpful examples based on selected agent
with st.expander("📝 Example Questions"):
    if st.session_state.agent_selection == "Revenue Agent":
        st.markdown("""
        Try asking:
        - What are the current fee distributions?
        - Show me the weekly CrvUSD fees
        - What are the pending pool fees?
        """)
    else:
        st.markdown("""
        Try asking:
        - What is the last 7 days of transactions for Ethereum?
        - Show me the current lending chains
        - How many users are on each chain?
        """) 