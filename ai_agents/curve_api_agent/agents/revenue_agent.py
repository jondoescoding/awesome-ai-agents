from phi.agent import Agent
from tools.revenue_tools import (
    get_fee_distributions,
    get_crvusd_weekly_fees,
    get_pools_weekly_fees,
    get_pending_pool_fees,
    get_cow_settlements,
    get_collected_fees,
    get_staged_fees
)
from core.config import llm

# Create revenue agent with all tools
revenue_agent = Agent(
    name="Curve Revenue Agent",
    role="Retrieve and analyze information about Curve protocol's revenue and fees",
    model=llm,
    tools=[
        get_fee_distributions,
        get_crvusd_weekly_fees,
        get_pools_weekly_fees,
        get_pending_pool_fees,
        get_cow_settlements,
        get_collected_fees,
        get_staged_fees
    ],
    description="""You are a specialized agent for analyzing Curve Protocol's revenue and fees.
    You have access to tools that can fetch:
    - Fee distributions history
    - Weekly crvUSD fees
    - Weekly pool fees
    - Pending pool fees
    - CoW settlements
    - Collected and staged fees
    
    When asked about fees or revenue, always use these tools to provide accurate data.""",
    instructions=[
        "When asked about fee distributions, use get_fee_distributions() first",
        "For weekly fees data, combine crvUSD and pools data when relevant",
        "Always provide numerical analysis of the fee data",
        "Format large numbers for better readability",
        "Explain the significance of fee changes or patterns",
        "If a tool call fails, try with different parameters or use an alternative tool",
        "Present data in a clear, structured format using markdown"
    ],
    show_tool_calls=True,
    markdown=True,
    add_datetime_to_instructions=True
)