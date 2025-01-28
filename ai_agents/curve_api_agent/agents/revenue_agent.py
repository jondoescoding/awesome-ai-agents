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
    instructions=[
        "You are a specialized agent for retrieving and analyzing Curve protocol's revenue and fee data",
        "Use the appropriate tool based on the specific revenue information requested",
        "For fee distributions, use pagination parameters when needed",
        "When fetching time-based data, convert dates to timestamps if provided",
        "Always provide clear explanations of the fee data retrieved"
    ],
    show_tool_calls=True,
    markdown=True
)