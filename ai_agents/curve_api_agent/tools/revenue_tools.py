import logging
from typing import Optional, Dict, Any
from core.config import APIClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_fee_distributions(page: int = 1, per_page: int = 10) -> str:
    """
    Get historical fee distributions with pagination
    
    Args:
        page (int): Page number for pagination (default: 1)
        per_page (int): Number of items per page (default: 10)
        
    Returns:
        Formatted string containing fee distribution data
    """
    logger.info(f"Fetching fee distributions for page {page} with {per_page} items per page")
    
    params = {
        "page": page,
        "per_page": per_page
    }
    
    with APIClient() as client:
        response = client.get("/v1/dao/fees/distributions", params=params)
        
        # Format the response as a string
        result = []
        result.append(f"Fee Distributions (Page {response['page']}, Total: {response['count']})")
        result.append("\n")
        
        for dist in response['distributions']:
            result.append("---")
            for key, value in dist.items():
                result.append(f"{key}: {value}")
            result.append("\n")
            
        return "\n".join(result)

def get_crvusd_weekly_fees(start: Optional[int] = None, end: Optional[int] = None) -> str:
    """
    Get weekly fees (including currently pending) from crvUSD markets
    
    Args:
        start (int, optional): Start timestamp
        end (int, optional): End timestamp
        
    Returns:
        Formatted string containing weekly crvUSD fees data
    """
    logger.info(f"Fetching crvUSD weekly fees from {start} to {end}")
    
    params = {}
    if start is not None:
        params["start"] = start
    if end is not None:
        params["end"] = end
        
    with APIClient() as client:
        response = client.get("/v1/dao/fees/crvusd/weekly", params=params)
        
        # Format the response as a string
        result = []
        result.append("Weekly crvUSD Fees")
        result.append("\n")
        
        # Group fees by timestamp for better readability
        fees_by_date = {}
        for fee in response['fees']:
            timestamp = fee['timestamp']
            if timestamp not in fees_by_date:
                fees_by_date[timestamp] = []
            fees_by_date[timestamp].append(fee)
        
        # Format each date's fees
        for timestamp, fees in sorted(fees_by_date.items(), reverse=True):
            result.append(f"\n## {timestamp}")
            total_fees = sum(fee['fees_usd'] for fee in fees)
            result.append(f"Total Fees: ${total_fees:,.2f}")
            
            for fee in fees:
                result.append(f"\n- {fee['collateral']}")
                result.append(f"  Fees: ${fee['fees_usd']:,.2f}")
                result.append(f"  Controller: {fee['controller']}")
            
        return "\n".join(result)

def get_pools_weekly_fees(start: Optional[int] = None, end: Optional[int] = None) -> str:
    """
    Get weekly fees (including currently pending) from pools across all chains
    
    Args:
        start (int, optional): Start timestamp
        end (int, optional): End timestamp
        
    Returns:
        Formatted string containing weekly pool fees data
    """
    logger.info(f"Fetching pools weekly fees from {start} to {end}")
    
    params = {}
    if start is not None:
        params["start"] = start
    if end is not None:
        params["end"] = end
        
    with APIClient() as client:
        response = client.get("/v1/dao/fees/pools/weekly", params=params)
        
        # Format the response as a string
        result = []
        result.append("Weekly Pool Fees Across Chains")
        result.append("\n")
        
        # Group fees by chain and timestamp
        fees_by_chain = {}
        for fee in response['fees']:
            chain = fee.get('chain', 'unknown')
            if chain not in fees_by_chain:
                fees_by_chain[chain] = {}
            
            timestamp = fee.get('timestamp')
            if timestamp not in fees_by_chain[chain]:
                fees_by_chain[chain][timestamp] = []
            fees_by_chain[chain][timestamp].append(fee)
        
        # Format each chain's fees
        for chain in sorted(fees_by_chain.keys()):
            result.append(f"\n# {chain.upper()}")
            
            for timestamp in sorted(fees_by_chain[chain].keys(), reverse=True):
                fees = fees_by_chain[chain][timestamp]
                result.append(f"\n## {timestamp}")
                total_chain_fees = sum(fee.get('fees_usd', 0) for fee in fees)
                result.append(f"Total Chain Fees: ${total_chain_fees:,.2f}")
                
                for fee in fees:
                    result.append(f"\n- Pool: {fee.get('pool_name', 'Unknown Pool')}")
                    result.append(f"  Fees: ${fee.get('fees_usd', 0):,.2f}")
                    if 'volume_usd' in fee:
                        result.append(f"  Volume: ${fee.get('volume_usd', 0):,.2f}")
            
        return "\n".join(result)

def get_pending_pool_fees(chain: str) -> str:
    """
    Get pending admin fees on all pools for a specific chain
    
    Args:
        chain (str): Chain identifier (e.g., "ethereum", "polygon")
        
    Returns:
        Formatted string containing pending pool fees data
    """
    logger.info(f"Fetching pending pool fees for chain: {chain}")
    
    with APIClient() as client:
        response = client.get(f"/v1/dao/fees/{chain}/pending")
        
        # Format the response as a string
        result = []
        result.append(f"Pending Pool Fees for {chain.upper()}")
        result.append("\n")
        
        if 'data' in response:
            total_pending_usd = sum(pool.get('pending_fees_usd', 0) for pool in response['data'])
            result.append(f"Total Pending Fees: ${total_pending_usd:,.2f}\n")
            
            # Sort pools by pending fees
            sorted_pools = sorted(
                response['data'], 
                key=lambda x: x.get('pending_fees_usd', 0), 
                reverse=True
            )
            
            for pool in sorted_pools:
                result.append(f"\n## {pool.get('name', 'Unknown Pool')}")
                result.append(f"Pending Fees: ${pool.get('pending_fees_usd', 0):,.2f}")
                if 'tokens' in pool:
                    result.append("\nToken Breakdown:")
                    for token in pool['tokens']:
                        result.append(f"- {token.get('symbol', 'Unknown')}: {token.get('amount', 0)}")
                        if 'usd_value' in token:
                            result.append(f"  (${token.get('usd_value', 0):,.2f})")
        
        return "\n".join(result)

def get_cow_settlements(timestamp: Optional[int] = None) -> str:
    """
    Get information on the latest settlements of fees via CoWSwap
    
    Args:
        timestamp (int, optional): Unix timestamp to filter settlements
        
    Returns:
        Formatted string containing CoWSwap settlement data
    """
    logger.info(f"Fetching CoWSwap settlements before timestamp: {timestamp}")
    
    params = {}
    if timestamp is not None:
        params["timestamp"] = timestamp
        
    with APIClient() as client:
        response = client.get("/v1/dao/fees/settlements", params=params)
        
        # Format the response as a string
        result = []
        result.append("CoWSwap Fee Settlements")
        result.append("\n")
        
        if 'settlements' in response:
            for settlement in response['settlements']:
                result.append("\n---")
                result.append(f"Timestamp: {settlement.get('timestamp', 'Unknown')}")
                result.append(f"Transaction: {settlement.get('tx_hash', 'Unknown')}")
                
                if 'tokens' in settlement:
                    result.append("\nTokens Settled:")
                    for token in settlement['tokens']:
                        result.append(f"- {token.get('symbol', 'Unknown')}")
                        result.append(f"  Amount: {token.get('amount', 0)}")
                        if 'usd_value' in token:
                            result.append(f"  Value: ${token.get('usd_value', 0):,.2f}")
                
                if 'total_usd' in settlement:
                    result.append(f"\nTotal Value: ${settlement.get('total_usd', 0):,.2f}")
        
        return "\n".join(result)

def get_collected_fees() -> str:
    """
    Get the list of tokens collected in the Fee Collector
    
    Returns:
        Formatted string containing collected fees data
    """
    logger.info("Fetching collected fees from Fee Collector")
    
    with APIClient() as client:
        response = client.get("/v1/dao/fees/collected")
        
        # Format the response as a string
        result = []
        result.append("Collected Fees in Fee Collector")
        result.append("\n")
        
        if 'data' in response:
            total_usd = sum(token.get('usd_value', 0) for token in response['data'])
            result.append(f"Total Value: ${total_usd:,.2f}\n")
            
            # Sort tokens by USD value
            sorted_tokens = sorted(
                response['data'],
                key=lambda x: x.get('usd_value', 0),
                reverse=True
            )
            
            for token in sorted_tokens:
                result.append(f"\n## {token.get('symbol', 'Unknown Token')}")
                result.append(f"Amount: {token.get('amount', 0):,.6f}")
                if 'usd_value' in token:
                    result.append(f"Value: ${token.get('usd_value', 0):,.2f}")
        
        return "\n".join(result)

def get_staged_fees() -> str:
    """
    Get the list of tokens collected in the Fee Burner
    
    Returns:
        Formatted string containing staged fees data
    """
    logger.info("Fetching staged fees from Fee Burner")
    
    with APIClient() as client:
        response = client.get("/v1/dao/fees/staged")
        
        # Format the response as a string
        result = []
        result.append("Staged Fees in Fee Burner")
        result.append("\n")
        
        if 'data' in response:
            total_usd = sum(token.get('usd_value', 0) for token in response['data'])
            result.append(f"Total Value: ${total_usd:,.2f}\n")
            
            # Sort tokens by USD value
            sorted_tokens = sorted(
                response['data'],
                key=lambda x: x.get('usd_value', 0),
                reverse=True
            )
            
            for token in sorted_tokens:
                result.append(f"\n## {token.get('symbol', 'Unknown Token')}")
                result.append(f"Amount: {token.get('amount', 0):,.6f}")
                if 'usd_value' in token:
                    result.append(f"Value: ${token.get('usd_value', 0):,.2f}")
        
        return "\n".join(result)
