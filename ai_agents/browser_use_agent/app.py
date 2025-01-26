import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, SystemPrompt
from pydantic import SecretStr
from dotenv import load_dotenv
import os
import asyncio

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Streamlit page config
st.set_page_config(page_title="Browser Use Chat", page_icon="🌐", layout="wide")
st.title("Browser Use Chat")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "browser_mode" not in st.session_state:
    st.session_state.browser_mode = False

# Initialize the model
@st.cache_resource
def get_llm():
    return ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))

llm = get_llm()

# Toggle for browser automation mode
st.session_state.browser_mode = st.toggle("Enable Browser Automation", value=st.session_state.browser_mode)

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to do?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        if st.session_state.browser_mode:
            # Run browser automation
            async def run_agent():
                agent = Agent(task=prompt, llm=llm)
                result = await agent.run()
                return result

            with st.spinner("Running browser automation..."):
                result = asyncio.run(run_agent())
                message_placeholder.markdown(result)
                st.session_state.messages.append({"role": "assistant", "content": result})
        else:
            # Regular chat response
            with st.spinner("Working..."):
                full_response = ""
                for chunk in llm.stream(prompt):
                    if chunk.content:
                        full_response += chunk.content
                        message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})