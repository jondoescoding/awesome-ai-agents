"""
Main script
-----------

What: This script allows the LLM to access the v1 chains from the Price Feeds Backend API from Curve.fi

"""
from core.config import APIClient
import logging
from typing import Optional
import requests

# FUNCTIONS
def get_all_supported_chains() -> str:
    """Gets ALL supported chains available on Curve.fi
    
    Returns:
        Formatted string containing chain data
    """
    try:
        logging.info("Fetching supported chains from Curve API...")
        with APIClient() as client:
            response = client.get(endpoint="/v1/chains")
            
            # Format the response as a string
            result = []
            result.append("Supported Chains on Curve.fi")
            result.append("\n")
            
            if 'chains' in response:
                for chain in sorted(response['chains']):
                    result.append(f"- {chain.upper()}")
                    
            return "\n".join(result)
    except requests.RequestException as e:
        return f"API Error: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"
    
def get_chain_pools(chain: str, page: int = 1, per_page: int = 10) -> str:
    """Gets all supported contracts/pools for a specific chain on Curve.fi
    
    Args:
        chain (str): The chain name to get pools for (e.g. 'ethereum', 'polygon')
        page (int, optional): Page number for pagination. Defaults to 1.
        per_page (int, optional): Number of results per page. Defaults to 10.
    
    Returns:
        Formatted string containing pool data for the specified chain
    """
    try:
        params = {
            'page': page,
            'per_page': per_page
        }
            
        logging.info(f"Fetching pools for chain {chain} from Curve API...")
        with APIClient() as client:
            response = client.get(
                endpoint=f"/v1/chains/{chain}",
                params=params
            )
            
            # Format the response as a string
            result = []
            result.append(f"Pools on {chain.upper()}")
            result.append(f"Page {response.get('page', 1)} of {(response.get('count', 0) + per_page - 1) // per_page}")
            result.append("\n")
            
            if 'stats' in response:
                stats = response['stats']
                result.append("## Chain Statistics")
                result.append(f"Total TVL: ${stats.get('tvl', 0):,.2f}")
                result.append(f"Daily Volume: ${stats.get('daily_volume', 0):,.2f}")
                result.append("\n")
            
            if 'pools' in response:
                result.append("## Pools")
                for pool in response['pools']:
                    result.append(f"\n### {pool.get('name', 'Unknown Pool')}")
                    result.append(f"Address: {pool.get('address', 'N/A')}")
                    result.append(f"TVL: ${pool.get('tvl', 0):,.2f}")
                    if 'volume' in pool:
                        result.append(f"Volume (24h): ${pool.get('volume', 0):,.2f}")
                    if 'tokens' in pool:
                        result.append("\nTokens:")
                        for token in pool['tokens']:
                            result.append(f"- {token.get('symbol', 'Unknown')}")
            
            return "\n".join(result)
    except requests.RequestException as e:
        return f"API Error: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_chain_transactions(start: Optional[int] = None, end: Optional[int] = None) -> str:
    """Get daily transactions count for each supported chain
    
    Args:
        start (int, optional): Start timestamp for filtering. Defaults to None.
        end (int, optional): End timestamp for filtering. Defaults to None.
    
    Returns:
        Formatted string containing transaction activity data for each chain
    """
    try:
        params = {}
        if start is not None:
            params['start'] = start
        if end is not None:
            params['end'] = end
            
        logging.info("Fetching chain transaction activity...")
        with APIClient() as client:
            response = client.get(
                endpoint="/v1/chains/activity/transactions",
                params=params
            )
            
            # Format the response as a string
            result = []
            result.append("Chain Transaction Activity")
            result.append("\n")
            
            if 'data' in response:
                # Group by chain
                chain_data = {}
                for entry in response['data']:
                    chain = entry.get('chain', 'unknown')
                    if chain not in chain_data:
                        chain_data[chain] = []
                    chain_data[chain].append(entry)
                
                # Format each chain's data
                for chain in sorted(chain_data.keys()):
                    result.append(f"\n## {chain.upper()}")
                    entries = sorted(chain_data[chain], key=lambda x: x.get('timestamp', ''), reverse=True)
                    
                    total_txns = sum(entry.get('transactions', 0) for entry in entries)
                    result.append(f"Total Transactions: {total_txns:,}")
                    
                    result.append("\nDaily Breakdown:")
                    for entry in entries[:7]:  # Show last 7 days
                        result.append(f"- {entry.get('timestamp', 'Unknown')}: {entry.get('transactions', 0):,} transactions")
            
            return "\n".join(result)
    except requests.RequestException as e:
        return f"API Error: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_chain_users(start: Optional[int] = None, end: Optional[int] = None) -> str:
    """Get daily unique user count for each supported chain
    
    Args:
        start (int, optional): Start timestamp for filtering. Defaults to None.
        end (int, optional): End timestamp for filtering. Defaults to None.
    
    Returns:
        Formatted string containing user activity data for each chain
    """
    try:
        params = {}
        if start is not None:
            params['start'] = start
        if end is not None:
            params['end'] = end
            
        logging.info("Fetching chain user activity...")
        with APIClient() as client:
            response = client.get(
                endpoint="/v1/chains/activity/users",
                params=params
            )
            
            # Format the response as a string
            result = []
            result.append("Chain User Activity")
            result.append("\n")
            
            if 'data' in response:
                # Group by chain
                chain_data = {}
                for entry in response['data']:
                    chain = entry.get('chain', 'unknown')
                    if chain not in chain_data:
                        chain_data[chain] = []
                    chain_data[chain].append(entry)
                
                # Format each chain's data
                for chain in sorted(chain_data.keys()):
                    result.append(f"\n## {chain.upper()}")
                    entries = sorted(chain_data[chain], key=lambda x: x.get('timestamp', ''), reverse=True)
                    
                    total_users = sum(entry.get('users', 0) for entry in entries)
                    result.append(f"Total Unique Users: {total_users:,}")
                    
                    result.append("\nDaily Breakdown:")
                    for entry in entries[:7]:  # Show last 7 days
                        result.append(f"- {entry.get('timestamp', 'Unknown')}: {entry.get('users', 0):,} users")
            
            return "\n".join(result)
    except requests.RequestException as e:
        return f"API Error: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_lending_chains() -> str:
    """Get all supported chains for lending stats
    
    Returns:
        Formatted string containing list of supported chains for lending
    """
    try:
        logging.info("Fetching supported lending chains...")
        with APIClient() as client:
            response = client.get(endpoint="/v1/lending/chains/")
            
            # Format the response as a string
            result = []
            result.append("Supported Lending Chains")
            result.append("\n")
            
            if 'chains' in response:
                for chain in sorted(response['chains']):
                    result.append(f"- {chain.upper()}")
                    if 'stats' in response and chain in response['stats']:
                        stats = response['stats'][chain]
                        result.append(f"  TVL: ${stats.get('tvl', 0):,.2f}")
                        result.append(f"  Total Borrowed: ${stats.get('total_borrowed', 0):,.2f}")
                        result.append(f"  Available Liquidity: ${stats.get('available_liquidity', 0):,.2f}")
            
            return "\n".join(result)
    except requests.RequestException as e:
        return f"API Error: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"