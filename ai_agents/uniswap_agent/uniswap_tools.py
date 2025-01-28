"""
Tools for interacting with Uniswap's Universal Router
---------------------------------------------------

What:
This script provides tools for interacting with Uniswap's Universal Router contract,
allowing for token swaps and other DeFi operations.
"""

import os
import json
import logging
from typing import Union, Tuple
from web3 import Web3
from langchain_core.tools import tool
from langchain_core.pydantic_v1 import BaseModel, Field
from coingecko_tools import get_token_contract_address
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

# Global variable for private key
_private_key = None

def set_private_key(key: str):
    """Set the private key for transactions."""
    global _private_key
    _private_key = key
    logging.info("Private key has been set")

# Initialize Web3
rpc_url = os.getenv("RPC_URL")
if not rpc_url:
    raise ValueError("RPC_URL environment variable not set")
web3 = Web3(Web3.HTTPProvider(rpc_url))
logging.info(f"Connected to Ethereum network via {rpc_url}")

# Contract addresses
UNIVERSAL_ROUTER_ADDRESS = "0x3fC91A3afd70395Cd496C647d5a6CC9D4B2b7FAD"  # Sepolia Universal Router

# Common Sepolia testnet token addresses
SEPOLIA_TOKENS = {
    "WETH": "0xfFf9976782d46CC05630D1f6eBAb18b2324d6B14L",
    "USDC": "0x1c7D4B196Cb0C7B01d743Fbc6116a902379C7238",
    "DAI": "0x68194a729C2450ad26072b3D33ADaCbcef39D574",
    "WBTC": "0xf864F011C5A97fD8Da79baEd78ba77b47112935a"
}

# Load Universal Router ABI
with open('uniswap_universal_router.json', 'r') as abi_file:
    UNIVERSAL_ROUTER_ABI = json.load(abi_file)

def resolve_token_address(token_identifier: str) -> str:
    """
    Helper function to resolve a token name/symbol to its contract address.
    First checks Sepolia testnet tokens, then falls back to mainnet if not found.
    """
    # Check if input is already a valid address
    if web3.is_address(token_identifier):
        return token_identifier
        
    # Check Sepolia testnet tokens first
    token_upper = token_identifier.upper()
    if token_upper in SEPOLIA_TOKENS:
        return SEPOLIA_TOKENS[token_upper]
        
    # If not found in Sepolia tokens, try CoinGecko (mainnet only)
    logging.warning(f"Token {token_identifier} not found in Sepolia tokens, attempting CoinGecko lookup (mainnet only)")
    contract_address = get_token_contract_address(token_identifier)
    if not contract_address:
        raise ValueError(f"Could not find contract address for token: {token_identifier}")
        
    return contract_address

class SwapTokensInput(BaseModel):
    """Input model for swap_tokens function"""
    token_in: str = Field(..., description="Name, symbol, or address of token to swap from (e.g., 'USDC' or contract address)")
    token_out: str = Field(..., description="Name, symbol, or address of token to swap to (e.g., 'ETH' or contract address)")
    amount_in: float = Field(..., description="Amount of input token to swap")
    min_amount_out: float = Field(..., description="Minimum amount of output token to receive")
    deadline: int = Field(None, description="Optional transaction deadline timestamp")

@tool
def swap_tokens(
    token_in: str,
    token_out: str,
    amount_in: float,
    min_amount_out: float,
    deadline: int = None
) -> Union[str, None]:
    """
    Swap tokens using Uniswap's Universal Router on Sepolia testnet.

    Args:
        token_in: Name, symbol, or address of token to swap from (e.g., "USDC" or contract address)
        token_out: Name, symbol, or address of token to swap to (e.g., "ETH" or contract address)
        amount_in: Amount of input token to swap
        min_amount_out: Minimum amount of output token to receive
        deadline: Optional transaction deadline timestamp

    Returns:
        str: Transaction hash if successful
        None: If the swap failed
    """
    try:
        # Resolve token addresses
        token_in_address = resolve_token_address(token_in)
        token_out_address = resolve_token_address(token_out)
        
        logging.info(f"Starting token swap: {amount_in} tokens from {token_in} ({token_in_address}) to {token_out} ({token_out_address})")
        
        # Initialize contracts
        router = web3.eth.contract(
            address=UNIVERSAL_ROUTER_ADDRESS,
            abi=UNIVERSAL_ROUTER_ABI
        )
        
        # Get account from private key
        if not _private_key:
            logging.error("Private key not set")
            return None
        account = web3.eth.account.from_key(_private_key)
        
        # Convert amounts to Wei
        erc20_abi = [
            {
                "constant": True,
                "inputs": [],
                "name": "decimals",
                "outputs": [{"name": "", "type": "uint8"}],
                "type": "function"
            }
        ]
        
        token_in_contract = web3.eth.contract(address=token_in_address, abi=erc20_abi)
        token_out_contract = web3.eth.contract(address=token_out_address, abi=erc20_abi)
        
        decimals_in = token_in_contract.functions.decimals().call()
        decimals_out = token_out_contract.functions.decimals().call()
        
        amount_in_wei = int(amount_in * (10 ** decimals_in))
        min_amount_out_wei = int(min_amount_out * (10 ** decimals_out))
        
        # Set deadline if not provided
        if not deadline:
            deadline = web3.eth.get_block('latest')['timestamp'] + 1800  # 30 minutes
            
        # Build transaction parameters
        tx_params = {
            'from': account.address,
            'nonce': web3.eth.get_transaction_count(account.address),
            'gas': 2000000,  # Adjust based on network conditions
            'gasPrice': web3.eth.gas_price,
            'value': amount_in_wei if token_in_address == SEPOLIA_TOKENS["WETH"] else 0,
        }

        # Universal Router command structure for swap
        command = bytes([0x00])  # V3_SWAP_EXACT_IN command
        
        # Encode the path for V3 swap
        encoded_path = b''
        encoded_path += token_in_address.replace('0x', '').zfill(40).encode('utf-8')
        encoded_path += (3000).to_bytes(3, 'big')  # fee in hex
        encoded_path += token_out_address.replace('0x', '').zfill(40).encode('utf-8')
        
        # Encode the swap parameters according to V3_SWAP_EXACT_IN structure
        swap_params = web3.eth.contract(abi=[{
            "inputs": [
                {"type": "address", "name": "recipient"},
                {"type": "uint256", "name": "amountIn"},
                {"type": "uint256", "name": "minAmountOut"},
                {"type": "bytes", "name": "path"},
                {"type": "bool", "name": "payerIsUser"}
            ],
            "name": "v3SwapExactIn",
            "outputs": [],
            "stateMutability": "payable",
            "type": "function"
        }]).encodeParameters(
            ['address', 'uint256', 'uint256', 'bytes', 'bool'],
            [
                account.address,
                amount_in_wei,
                min_amount_out_wei,
                encoded_path,
                True  # payerIsUser: True since we're using Permit2
            ]
        )

        # Execute the swap using contract function interface
        swap_tx = router.functions.execute(
            command,
            [swap_params],
            deadline or (web3.eth.get_block('latest')['timestamp'] + 1800)  # 30 min default
        ).build_transaction(tx_params)

        # Sign and send transaction
        signed_tx = account.sign_transaction(swap_tx)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        logging.info(f"Transaction sent with hash: {tx_hash.hex()}")
        return tx_hash.hex()

    except Exception as e:
        logging.error(f"Error in swap_tokens: {str(e)}")
        return None

def main():
    """
    Main function providing a terminal interface for token swapping.
    """
    print("\n=== Uniswap Token Swap Interface ===")
    
    # Get private key if not set
    if not _private_key:
        private_key = input("\nEnter your private key (or press Enter to load from .env): ").strip()
        if private_key:
            set_private_key(private_key)
        else:
            private_key = os.getenv("PRIVATE_KEY")
            if not private_key:
                print("Error: No private key provided or found in .env")
                return
            set_private_key(private_key)
    
    while True:
        print("\n=== Available Actions ===")
        print("1. Swap Tokens")
        print("2. Exit")
        
        choice = input("\nEnter your choice (1-2): ").strip()
        
        if choice == "2":
            print("\nExiting...")
            break
            
        elif choice == "1":
            try:
                # Get token input details
                token_in = input("\nEnter input token (name, symbol, or address): ").strip()
                token_out = input("Enter output token (name, symbol, or address): ").strip()
                
                # Get amounts
                amount_in = float(input("Enter amount to swap: ").strip())
                slippage = float(input("Enter maximum slippage percentage (e.g., 0.5 for 0.5%): ").strip())
                
                # Calculate min amount out based on slippage
                min_amount_out = amount_in * (1 - slippage/100)
                
                print("\nConfirm Transaction Details:")
                print(f"Swap: {amount_in} {token_in} → {token_out}")
                print(f"Minimum output amount (with {slippage}% slippage): {min_amount_out}")
                
                confirm = input("\nProceed with swap? (y/n): ").strip().lower()
                if confirm != 'y':
                    print("Transaction cancelled")
                    continue
                
                # Execute swap using invoke method
                result = swap_tokens.invoke({
                    "token_in": token_in,
                    "token_out": token_out,
                    "amount_in": amount_in,
                    "min_amount_out": min_amount_out
                })
                
                if result:
                    print(f"\nTransaction successful!")
                    print(f"Transaction hash: {result}")
                    
                    # Get transaction receipt to confirm status
                    receipt = web3.eth.wait_for_transaction_receipt(result)
                    if receipt['status'] == 1:
                        print("Transaction confirmed and successful!")
                    else:
                        print("Transaction failed after being mined!")
                else:
                    print("\nTransaction failed!")
                    
            except ValueError as e:
                print(f"\nError: {str(e)}")
            except Exception as e:
                print(f"\nUnexpected error: {str(e)}")
                
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
