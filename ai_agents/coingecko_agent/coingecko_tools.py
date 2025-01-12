from typing import Dict, Any, Union, List
from langchain_core.tools import tool
from pycoingecko import CoinGeckoAPI
from dotenv import load_dotenv
import os

load_dotenv()

cg = CoinGeckoAPI(demo_api_key=os.getenv('coingecko_api_key'))

@tool
def get_trending_tokens() -> Dict[str, Any]:
    """
    Retrieves and cleans the top 7 trending coins data from CoinGecko within the last 24 hours.
    Removes specific fields (price changes and market cap changes) and limits results 
    to only the first 3 coins.

    Returns:
        Dict[str, Any]: Cleaned dictionary containing the top 3 trending tokens data
        with specified fields removed.
    """
    def clean_nested_data(data: Union[Dict, List, Any]) -> Union[Dict, List, Any]:
        """
        Recursively cleans nested data structures by removing specified fields.
        
        This function removes:
        - Any field containing 'price_change' in its name
        - The 'market_cap_1h_change' field
        
        Args:
            data: The data structure to clean (can be a dict, list, or simple value)
            
        Returns:
            The cleaned data structure with specified fields removed
        """
        # Create a list of fields we want to exclude
        fields_to_exclude = [
            'price_change',
            'market_cap_1h_change',
            'market_cap_change_percentage_24h'
        ]
        
        # Handle dictionaries
        if isinstance(data, dict):
            return {
                key: clean_nested_data(value)
                for key, value in data.items()
                if not any(excluded in key.lower() for excluded in fields_to_exclude)
            }
        
        # Handle lists
        if isinstance(data, list):
            return [clean_nested_data(item) for item in data]
        
        # Return unchanged data for other types
        return data

    # Get raw data from CoinGecko
    raw_data = cg.get_search_trending()
    
    # Create a new dictionary with only the top 3 coins
    limited_data = raw_data.copy()
    
    # Limit the coins list to the first 3 entries while preserving other data
    if 'coins' in limited_data and isinstance(limited_data['coins'], list):
        limited_data['coins'] = limited_data['coins'][:1] # Only returns the "coins" section of the API
    
    # Clean the limited data and return it
    return clean_nested_data(limited_data)