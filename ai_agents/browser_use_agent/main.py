from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, SystemPrompt
from pydantic import SecretStr
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the model
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))

user_input = input("What do you want to automate on your browser: ")

async def main():
    # Create agent with the model
    agent = Agent(
    task=user_input,
    llm=llm,
    )

    result = await agent.run()
    print(result)

asyncio.run(main())