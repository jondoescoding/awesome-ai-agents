from tools.revenue_tools import (
    get_fee_distributions,
    get_crvusd_weekly_fees,
    get_pools_weekly_fees,
    get_pending_pool_fees,
    get_cow_settlements,
    get_collected_fees,
    get_staged_fees
)
from llama_index.core.agent.workflow import AgentWorkflow
from core.config import llm
import asyncio

workflow = AgentWorkflow.from_tools_or_functions(
    [
        get_fee_distributions,
        get_crvusd_weekly_fees,
        get_pools_weekly_fees,
        get_pending_pool_fees,
        get_cow_settlements,
        get_collected_fees,
        get_staged_fees
    ],
    llm=llm,
    system_prompt="You are a helpful assistant that can retrieve information about Curve protocol's revenue and fees.",
)

async def main():
    # Example query to get fee distributions
    response = await workflow.run(user_msg="Show me crvusd weekly fees")
    print(str(response))

if __name__ == "__main__":
    asyncio.run(main())
