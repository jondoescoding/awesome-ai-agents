from phi.agent import Agent
from tools.chains_tool import (
    get_chain_transactions,
    get_chain_users,
    get_lending_chains,
    get_all_supported_chains,
    get_chain_pools
)
from core.config import llm

# Initialize the chain agent
chain_agent = Agent(
    name="Chain Agent",
    role="Analyze and provide information about blockchain chains using Curve.fi data",
    model=llm,
    tools=[
        get_chain_transactions,
        get_chain_users,
        get_lending_chains,
        get_all_supported_chains,
        get_chain_pools
    ],
    instructions=[
        "Provide accurate chain transaction and user statistics",
        "Format numerical data in tables when possible",
        "Include timestamps with data when available",
        "Explain significant trends or patterns in the data",
    ],
    show_tool_calls=True,
    markdown=True,
)

def get_agent():
    """Returns the initialized chain agent"""
    return chain_agent