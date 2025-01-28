import gradio as gr
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, SystemPrompt
from pydantic import SecretStr
from dotenv import load_dotenv
import os
import asyncio

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the model
def get_llm():
    return ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))

llm = get_llm()

# Initialize browser mode state
browser_mode = False

def toggle_browser_mode():
    global browser_mode
    browser_mode = not browser_mode
    return f"Browser mode {'enabled' if browser_mode else 'disabled'}"

async def chat_response(message, history):
    if browser_mode:
        # Run browser automation
        agent = Agent(task=message, llm=llm)
        result = await agent.run()
        yield result
    else:
        # Regular chat response
        response = ""
        for chunk in llm.stream(message):
            if chunk.content:
                response += chunk.content
                yield response

# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Browser Use Chat")
    
    with gr.Row():
        browser_toggle = gr.Button("Toggle Browser Mode")
        status = gr.Textbox(label="Status", value="Browser mode disabled")
    
    chatbot = gr.ChatInterface(
        fn=chat_response,
        title="Chat with Browser Agent",
        description="Chat with an AI that can browse the web for you.",
        examples=["What's the weather like?", "Search for recent news about AI"],
        retry_btn=None,
        undo_btn=None,
        clear_btn="Clear",
    )
    
    browser_toggle.click(toggle_browser_mode, outputs=status)

if __name__ == "__main__":
    demo.launch()