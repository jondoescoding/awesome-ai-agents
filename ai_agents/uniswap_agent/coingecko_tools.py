"""
Tools for interacting with CoinGecko API
--------------------------------------

What:
This script provides tools for getting token contract addresses from CoinGecko
using token names or symbols.
"""

import os
import logging
from typing import Union
from pycoingecko import CoinGeckoAPI
from langchain_core.tools import tool
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

# Initialize CoinGecko API client with API key from environment
COINGECKO_DEMO_API_KEY = os.getenv("COINGECKO_DEMO_API_KEY", "")  # Demo API key

cg = CoinGeckoAPI(demo_api_key=COINGECKO_DEMO_API_KEY)
logging.info("Using CoinGecko Demo API")

@tool
def get_token_contract_address(token_identifier: str, platform: str = "ethereum") -> Union[str, None]:
    """
    Get the contract address for a token using its name or symbol.
    
    Parameters:
    token_identifier (str): The token name or symbol (e.g., "USDC" or "USD Coin")
    platform (str): The blockchain platform (default: "ethereum")
    
    Returns:
    Union[str, None]: Contract address if found, None if not found
    """
    try:
        # Search for the token
        search_results = cg.search(token_identifier)
        
        if not search_results or 'coins' not in search_results or not search_results['coins']:
            logging.error(f"No results found for token: {token_identifier}")
            return None
            
        # Get the first matching coin's ID
        coin_id = search_results['coins'][0]['id']
        logging.info(f"Found coin ID: {coin_id}")
        
        # Get detailed coin info including contract addresses
        coin_info = cg.get_coin_by_id(coin_id)
        
        if not coin_info or 'platforms' not in coin_info or platform not in coin_info['platforms']:
            logging.error(f"No contract address found for {token_identifier} on {platform}")
            return None
            
        contract_address = coin_info['platforms'][platform]
        if not contract_address:
            logging.error(f"Empty contract address for {token_identifier} on {platform}")
            return None
            
        logging.info(f"Found contract address: {contract_address}")
        return contract_address
        
    except Exception as e:
        logging.error(f"Error getting contract address: {str(e)}")
        return None
