"""
Main script
-----------

What: This script allows the LLM to access the v1 chains from the Price Feeds Backend API from Curve.fi

"""
from core.config import APIClient
import logging
import asyncio
import aiohttp
from typing import Optional

# FUNCTIONS
async def get_all_supported_chains() -> dict:
    """Gets ALL supported chains available on Curve.fi
    
    Returns:
        dict: Chain data or error details
        
    Raises:
        HTTPError: For failed API requests
    """
    try:
        logging.info("Fetching supported chains from Curve API...")
        async with APIClient() as client:
            result = await client.get(endpoint="/v1/chains")
            logging.debug(f"Received {len(result)} chains")
            return result
    except aiohttp.ClientError as e:
        print(f"API Error: {str(e)}")
        return {"error": str(e)}
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"error": "Request failed"}
    
async def get_chain_pools(chain: str, page: int = 1, per_page: int = 10) -> dict:
    """Gets all supported contracts/pools for a specific chain on Curve.fi
    
    Args:
        chain (str): The chain name to get pools for (e.g. 'ethereum', 'polygon')
        page (int, optional): Page number for pagination. Defaults to 1.
        per_page (int, optional): Number of results per page. Defaults to 10.
    
    Returns:
        dict: Pool data for the specified chain or error details
            Contains count, page, per_page, total stats and pool data
            
    Raises:
        HTTPError: For failed API requests
    """
    try:
        # Build query parameters
        params = {
            'page': page,
            'per_page': per_page
        }
            
        logging.info(f"Fetching pools for chain {chain} from Curve API...")
        async with APIClient() as client:
            result = await client.get(
                endpoint=f"/v1/chains/{chain}",
                params=params
            )
            logging.debug(f"Received pool data for chain {chain}")
            return result
    except aiohttp.ClientError as e:
        print(f"API Error: {str(e)}")
        return {"error": str(e)}
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"error": "Request failed"}

async def get_chain_transactions(start: Optional[int] = None, end: Optional[int] = None) -> dict:
    """Get daily transactions count for each supported chain
    
    Args:
        start (int, optional): Start timestamp for filtering. Defaults to None.
        end (int, optional): End timestamp for filtering. Defaults to None.
    
    Returns:
        dict: Transaction activity data for each chain
            Contains chain name and list of transaction counts with timestamps
            
    Raises:
        HTTPError: For failed API requests
    """
    try:
        # Build query parameters if provided
        params = {}
        if start is not None:
            params['start'] = start
        if end is not None:
            params['end'] = end
            
        logging.info("Fetching chain transaction activity...")
        async with APIClient() as client:
            result = await client.get(
                endpoint="/v1/chains/activity/transactions",
                params=params
            )
            logging.debug("Received chain transaction activity data")
            return result
    except aiohttp.ClientError as e:
        print(f"API Error: {str(e)}")
        return {"error": str(e)}
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"error": "Request failed"}

async def get_chain_users(start: Optional[int] = None, end: Optional[int] = None) -> dict:
    """Get daily unique user count for each supported chain
    
    Args:
        start (int, optional): Start timestamp for filtering. Defaults to None.
        end (int, optional): End timestamp for filtering. Defaults to None.
    
    Returns:
        dict: User activity data for each chain
            Contains chain name and list of unique user counts with timestamps
            
    Raises:
        HTTPError: For failed API requests
    """
    try:
        # Build query parameters if provided
        params = {}
        if start is not None:
            params['start'] = start
        if end is not None:
            params['end'] = end
            
        logging.info("Fetching chain user activity...")
        async with APIClient() as client:
            result = await client.get(
                endpoint="/v1/chains/activity/users",
                params=params
            )
            logging.debug("Received chain user activity data")
            return result
    except aiohttp.ClientError as e:
        print(f"API Error: {str(e)}")
        return {"error": str(e)}
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"error": "Request failed"}

async def get_lending_chains() -> dict:
    """Get all supported chains for lending stats
    
    Returns:
        dict: List of supported chains for lending
            Contains chain names
            
    Raises:
        HTTPError: For failed API requests
    """
    try:
        logging.info("Fetching supported lending chains...")
        async with APIClient() as client:
            result = await client.get(endpoint="/v1/lending/chains/")
            logging.debug("Received lending chains data")
            return result
    except aiohttp.ClientError as e:
        print(f"API Error: {str(e)}")
        return {"error": str(e)}
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"error": "Request failed"}