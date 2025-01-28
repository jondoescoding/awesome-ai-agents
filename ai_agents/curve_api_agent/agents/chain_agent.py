from tools.chains_tool import get_chain_transactions, get_chain_users, get_lending_chains
from llama_index.llms.openai import OpenAI
from llama_index.core.agent.workflow import AgentWorkflow
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

llm = OpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

workflow = AgentWorkflow.from_tools_or_functions(
    [get_chain_transactions, get_chain_users, get_lending_chains],
    llm=llm,
    system_prompt="You are a helpful assistant that can get chain transactions, users, and lending chains.",
)

async def main():
    response = await workflow.run(user_msg="What is the last 7 days of transactions for Ethereum?")
    print(str(response))

if __name__ == "__main__":
    asyncio.run(main())