import aiohttp
from llama_index.llms.openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize LLM configuration
llm = OpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

class APIClient:
    def __init__(self):
        self.base_url = "https://prices.curve.fi"
        self._session = None
        
    async def __aenter__(self):
        self._session = aiohttp.ClientSession()
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._session:
            await self._session.close()
            
    async def get(self, endpoint: str, params: dict = None) -> dict:
        """Make a GET request to the API
        
        Args:
            endpoint (str): API endpoint to call
            params (dict, optional): Query parameters to include. Defaults to None.
            
        Returns:
            dict: JSON response from the API
        """
        if not self._session:
            self._session = aiohttp.ClientSession()
        async with self._session.get(f"{self.base_url}{endpoint}", params=params) as response:
            response.raise_for_status()
            return await response.json() 