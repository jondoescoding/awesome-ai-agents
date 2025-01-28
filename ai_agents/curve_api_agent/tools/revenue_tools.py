import logging
from typing import Optional, Dict, Any
from core.config import APIClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_fee_distributions(page: int = 1, per_page: int = 10) -> Dict[str, Any]:
    """
    Get historical fee distributions with pagination
    
    Args:
        page (int): Page number for pagination (default: 1)
        per_page (int): Number of items per page (default: 10)
        
    Returns:
        Dict containing fee distribution data including:
        - distributions: List of fee distribution events
        - page: Current page number
        - count: Total number of distributions
    """
    logger.info(f"Fetching fee distributions for page {page} with {per_page} items per page")
    
    params = {
        "page": page,
        "per_page": per_page
    }
    
    with APIClient() as client:
        return client.get("/v1/dao/fees/distributions", params=params)

def get_crvusd_weekly_fees(start: Optional[int] = None, end: Optional[int] = None) -> Dict[str, Any]:
    """
    Get weekly fees (including currently pending) from crvUSD markets
    
    Args:
        start (int, optional): Start timestamp
        end (int, optional): End timestamp
        
    Returns:
        Dict containing weekly crvUSD fees data including:
        - fees: List of fee distribution data per controller/collateral
    """
    logger.info(f"Fetching crvUSD weekly fees from {start} to {end}")
    
    params = {}
    if start is not None:
        params["start"] = start
    if end is not None:
        params["end"] = end
        
    with APIClient() as client:
        return client.get("/v1/dao/fees/crvusd/weekly", params=params)

def get_pools_weekly_fees(start: Optional[int] = None, end: Optional[int] = None) -> Dict[str, Any]:
    """
    Get weekly fees (including currently pending) from pools across all chains
    
    Args:
        start (int, optional): Start timestamp
        end (int, optional): End timestamp
        
    Returns:
        Dict containing weekly pool fees data including:
        - fees: List of fee distribution data per chain
    """
    logger.info(f"Fetching pools weekly fees from {start} to {end}")
    
    params = {}
    if start is not None:
        params["start"] = start
    if end is not None:
        params["end"] = end
        
    with APIClient() as client:
        return client.get("/v1/dao/fees/pools/weekly", params=params)

def get_pending_pool_fees(chain: str) -> Dict[str, Any]:
    """
    Get pending admin fees on all pools for a specific chain
    
    Args:
        chain (str): Chain identifier (e.g., "ethereum", "polygon")
        
    Returns:
        Dict containing pending pool fees data including:
        - chain: Chain identifier
        - data: List of pools with their pending fees
    """
    logger.info(f"Fetching pending pool fees for chain: {chain}")
    
    with APIClient() as client:
        return client.get(f"/v1/dao/fees/{chain}/pending")

def get_cow_settlements(timestamp: Optional[int] = None) -> Dict[str, Any]:
    """
    Get information on the latest settlements of fees via CoWSwap
    
    Args:
        timestamp (int, optional): Unix timestamp to filter settlements
        
    Returns:
        Dict containing CoWSwap settlement data
    """
    logger.info(f"Fetching CoWSwap settlements before timestamp: {timestamp}")
    
    params = {}
    if timestamp is not None:
        params["timestamp"] = timestamp
        
    with APIClient() as client:
        return client.get("/v1/dao/fees/settlements", params=params)

def get_collected_fees() -> Dict[str, Any]:
    """
    Get the list of tokens collected in the Fee Collector
    
    Returns:
        Dict containing collected fees data including:
        - data: List of tokens with their amounts and USD values
    """
    logger.info("Fetching collected fees from Fee Collector")
    
    with APIClient() as client:
        return client.get("/v1/dao/fees/collected")

def get_staged_fees() -> Dict[str, Any]:
    """
    Get the list of tokens collected in the Fee Burner
    
    Returns:
        Dict containing staged fees data including:
        - data: List of tokens with their amounts and USD values
    """
    logger.info("Fetching staged fees from Fee Burner")
    
    with APIClient() as client:
        return client.get("/v1/dao/fees/staged")
