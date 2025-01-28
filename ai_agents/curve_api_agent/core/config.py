import requests
from phi.model.openai import OpenAIChat
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize LLM configuration with required settings
llm = OpenAIChat(
    id="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)

class APIClient:
    def __init__(self):
        self.base_url = "https://prices.curve.fi"
        self.session = requests.Session()
        
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
            
    def get(self, endpoint: str, params: dict = None) -> dict:
        """Make a GET request to the API
        
        Args:
            endpoint (str): API endpoint to call
            params (dict, optional): Query parameters to include. Defaults to None.
            
        Returns:
            dict: JSON response from the API
        """
        response = self.session.get(f"{self.base_url}{endpoint}", params=params)
        response.raise_for_status()
        return response.json() 