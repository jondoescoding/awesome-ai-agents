"""
Tools
-------------------
What:
This script is the warehouse of tools that the AI Agent has access to. It controls what the agent can do when interacting with the DeFi platform, AAVE. As of the current implementation the agent can both borrow and lend on the AAVE platform.

Functions:
    lend_tokens
    borrow_tokens
    get_tokens
"""

# Built in python imports
import os
import json
import logging
from typing import Union
from dotenv import load_dotenv
from langchain_core.tools import tool

# Web3 Interactions
from web3 import Web3

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
    """
    Set the private key for use in transactions.
    This should be called from main.py when the private key is received from the user.
    
    Args:
        key (str): The private key to use for transactions
    """
    global _private_key
    _private_key = key
    logging.info("Private key has been set")

"""
Initial Setup -> GLOBAL VARIABLES
"""
rpc_url = os.getenv("RPC_URL") # what will be used to connect to the blockchain
aave_lending_pool_address = "0x6Ae43d3271ff6888e7Fc43Fd7321a503ff738951" # aave's pool address on the blockchain 


# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(rpc_url))

# Load AAVE Lending Pool ABI - the ABI allows us to know what functions are available
with open('./aave_lending_pool_abi_testnet.json', 'r') as abi_file:
    aave_lending_pool_abi = json.load(abi_file)

# Loading the environmental variables which we don't want to be exposed to the general public
load_dotenv()

@tool
def lend_crypto(amount: float, asset_address: str) -> Union[str, None]:
    """
    Lends a specific cryptocurrency (via its token address) to the AAVE lending pool.

    Technical Flow:
    1. Connects to Ethereum network
    2. Initializes smart contract interfaces
    3. Approves AAVE to spend tokens (ERC20 approve)
    4. Supplies tokens to AAVE pool
    
    Parameters:
    amount (float): The amount of cryptocurrency to lend in human-readable format (e.g., 100 USDC)
    asset_address (str): The Ethereum address of the token to be lent

    Returns:
    Union[str, None]: The transaction hash if successful, None if any step fails

    Implementation Details:
    --------------------
    1. Initial Setup and Validation:
       - Logs attempt to lend with amount and asset address
       - Checks web3 connection to ensure we're connected to Ethereum
       Why: Ensures we have proper connection before attempting any transactions

    2. Contract Setup:
       - Loads minimal ERC20 ABI for token approval
       - Initializes both AAVE lending pool and token contracts
       Why: Need interfaces to interact with both the token and AAVE contracts

    3. Account Setup:
       - Creates account from private key
       - Gets current nonce (transaction count)
       - Retrieves current gas price
       Why: Required for transaction signing and gas estimation

    4. Amount Conversion:
       - Converts human-readable amount to token decimals
       Why: Smart contracts work with raw numbers, not decimals

    5. Token Approval:
       - Builds approval transaction with EIP-1559 parameters
       - Signs and sends approval transaction
       - Waits for approval confirmation
       Why: ERC20 tokens require explicit approval before third-party contracts can move them

    6. Supply to AAVE:
       - Builds supply transaction with EIP-1559 parameters
       - Signs and sends supply transaction
       - Waits for supply confirmation
       Why: Actually supplies the tokens to AAVE's lending pool

    Error Handling:
    - Separate try-catch blocks for approval and supply steps
    - Detailed logging of transaction states and errors
    - Transaction receipt validation
    Why: Provides clear error messages and transaction status for debugging

    Gas and Transaction Parameters:
    - Uses EIP-1559 transaction type (type 2)
    - Calculates maxFeePerGas and maxPriorityFeePerGas
    - Sets appropriate gas limits for each operation
    Why: Ensures reliable transaction processing with optimal gas costs
    """
    # Initial validation: Log the attempt and verify Ethereum connection
    logging.info(f"Attempting to lend {amount} of asset at {asset_address}")
    if not web3.is_connected():
        logging.warning("Unable to connect to Ethereum")
        return None

    # Validate private key is set
    if _private_key is None:
        logging.error("Private key not set. Please set private key before attempting transactions.")
        return None

    try:
        # Log connection details for debugging purposes
        logging.info("Connected to Ethereum")
        logging.info(f"Using RPC URL: {rpc_url}")
        logging.info(f"AAVE Lending Pool Address: {aave_lending_pool_address}")
        
        # Define minimal ERC20 ABI for approval and decimals
        erc20_abi = [
            {
                "constant": False,
                "inputs": [
                    {"name": "_spender", "type": "address"},
                    {"name": "_value", "type": "uint256"}
                ],
                "name": "approve",
                "outputs": [{"name": "", "type": "bool"}],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function"
            },
            {
                "constant": True,
                "inputs": [],
                "name": "decimals",
                "outputs": [{"name": "", "type": "uint8"}],
                "type": "function"
            }
        ]
        
        # Initialize smart contract interfaces
        # lending_pool: Interface to interact with AAVE's lending pool
        # token_contract: Interface to interact with the token contract
        lending_pool = web3.eth.contract(address=aave_lending_pool_address, abi=aave_lending_pool_abi)
        token_contract = web3.eth.contract(address=asset_address, abi=erc20_abi)
        logging.info("Contracts initialized successfully")
        
        # Get token decimals
        token_decimals = token_contract.functions.decimals().call()
        logging.info(f"Token decimals: {token_decimals}")
        
        # Setup account and get current blockchain state
        account = web3.eth.account.from_key(_private_key)
        nonce = web3.eth.get_transaction_count(account.address)
        logging.info(f"Account address: {account.address}")
        logging.info(f"Current nonce: {nonce}")
        logging.info(f"Current gas price: {web3.eth.gas_price}")

        # Convert human-readable amount to token decimals
        # Dynamically use the token's decimal places
        amount_in_wei = int(amount * 10**token_decimals)
        logging.info(f"Amount in token base units: {amount_in_wei}")

        # Build approval transaction
        # This transaction allows AAVE to spend our tokens
        approve_tx = token_contract.functions.approve(
            aave_lending_pool_address,  # Who we're approving (AAVE)
            amount_in_wei              # How much we're approving
        ).build_transaction({
            'from': account.address,                    # Who is giving approval
            'chainId': 11155111,                       # Sepolia testnet chain ID
            'gas': 100000,                             # Maximum gas willing to spend
            'maxFeePerGas': web3.eth.gas_price * 2,    # Maximum total fee per gas unit
            'maxPriorityFeePerGas': web3.eth.gas_price,# Tip to miners
            'nonce': nonce,                            # Transaction count
            'type': 2                                  # EIP-1559 transaction type
        })
        logging.info(f"Approval transaction built: {approve_tx}")
        
        try:
            # Sign and send approval transaction
            logging.info("Attempting to sign approval transaction...")
            signed_approve_tx = account.sign_transaction(approve_tx)
            logging.info("Approval transaction signed successfully")
            
            # Debug: Inspect SignedTransaction object attributes
            logging.info("SignedTransaction attributes:")
            logging.info(f"Hash: {signed_approve_tx.hash.hex()}")
            logging.info(f"r: {signed_approve_tx.r}")  # Part of transaction signature
            logging.info(f"s: {signed_approve_tx.s}")  # Part of transaction signature
            logging.info(f"v: {signed_approve_tx.v}")  # Recovery value for signature
            
            # Send the raw transaction to the network
            try:
                tx_hash_approve = web3.eth.send_raw_transaction(signed_approve_tx.raw_transaction)
            except Exception as e:
                logging.error("Failed to send raw transaction")
                logging.error(f"Raw transaction: {signed_approve_tx.raw_transaction.hex()}")
                raise e
                
            logging.info(f"Approval Transaction Hash: {tx_hash_approve.hex()}")
            
            # Wait for transaction to be mined and get receipt
            receipt = web3.eth.wait_for_transaction_receipt(tx_hash_approve)
            logging.info(f"Approval transaction mined in block: {receipt['blockNumber']}")
            logging.info(f"Approval transaction status: {'Success' if receipt['status'] == 1 else 'Failed'}")
        except Exception as e:
            logging.error(f"Error in approval transaction: {str(e)}")
            logging.error(f"Error type: {type(e)}")
            raise e
        
        try:
            # Build supply transaction to AAVE
            # This transaction actually supplies our tokens to the lending pool
            supply_tx = lending_pool.functions.supply(
                asset_address,          # Token we're supplying
                amount_in_wei,          # Amount we're supplying
                account.address,        # Who will receive the aToken (us)
                0                       # Referral code (not used)
            ).build_transaction({
                'from': account.address,                    # Who is supplying
                'chainId': 11155111,                       # Sepolia testnet chain ID
                'gas': 700000,                             # Maximum gas willing to spend
                'maxFeePerGas': web3.eth.gas_price * 2,    # Maximum total fee per gas unit
                'maxPriorityFeePerGas': web3.eth.gas_price,# Tip to miners
                'nonce': nonce + 1,                        # Increment nonce for second transaction
                'type': 2                                  # EIP-1559 transaction type
            })
            logging.info("Supply transaction built successfully")

            # Sign the supply transaction
            logging.info("Attempting to sign supply transaction...")
            signed_tx = account.sign_transaction(supply_tx)
            logging.info("Supply transaction signed successfully")
            
            # Debug: Inspect SignedTransaction object for supply tx
            logging.info("SignedTransaction attributes:")
            logging.info(f"Hash: {signed_tx.hash.hex()}")
            logging.info(f"r: {signed_tx.r}")  # Part of transaction signature
            logging.info(f"s: {signed_tx.s}")  # Part of transaction signature
            logging.info(f"v: {signed_tx.v}")  # Recovery value for signature
            
            # Send the supply transaction to the network
            try:
                tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
            except Exception as e:
                logging.error("Failed to send raw transaction")
                logging.error(f"Raw transaction: {signed_tx.raw_transaction.hex()}")
                raise e
                
            logging.info(f"Supply Transaction Hash: {tx_hash.hex()}")
            
            # Wait for supply transaction to be mined and get receipt
            receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
            logging.info(f"Supply transaction mined in block: {receipt['blockNumber']}")
            logging.info(f"Supply transaction status: {'Success' if receipt['status'] == 1 else 'Failed'}")
            
            return web3.to_hex(tx_hash)
        except Exception as e:
            logging.error(f"Error in supply transaction: {str(e)}")
            logging.error(f"Error type: {type(e)}")
            raise e
    except Exception as e:
        logging.error(f"An error occurred during the lending process: {e}")
        logging.error(f"Error type: {type(e)}")
        return None


def get_user_account_data(account_address: str) -> dict:
    """
    Get user's account data from AAVE, including collateral and borrowing power.
    
    Parameters:
    account_address (str): The Ethereum address of the user

    Returns:
    dict: User account data including:
        - totalCollateralBase: Total collateral in base currency (ETH)
        - totalDebtBase: Total debt in base currency (ETH)
        - availableBorrowsBase: Available borrowing power in base currency (ETH)
        - currentLiquidationThreshold: Current liquidation threshold
        - ltv: Current loan to value
        - healthFactor: Current health factor
    """
    try:
        lending_pool = web3.eth.contract(address=aave_lending_pool_address, abi=aave_lending_pool_abi)
        account_data = lending_pool.functions.getUserAccountData(account_address).call()
        
        return {
            'totalCollateralBase': account_data[0],
            'totalDebtBase': account_data[1],
            'availableBorrowsBase': account_data[2],
            'currentLiquidationThreshold': account_data[3],
            'ltv': account_data[4],
            'healthFactor': account_data[5]
        }
    except Exception as e:
        logging.error(f"Error getting user account data: {e}")
        return None

@tool
def borrow_crypto(amount: float, asset_address: str, interest_rate_mode: int = 2) -> Union[str, None]:
    """
    Borrow cryptocurrency from the AAVE lending pool.

    Technical Flow:
    1. Connects to Ethereum network
    2. Initializes AAVE lending pool interface
    3. Executes borrow transaction
    4. Waits for confirmation
    
    Parameters:
    amount (float): The amount of cryptocurrency to borrow in human-readable format (e.g., 100 USDC)
    asset_address (str): The Ethereum address of the token to be borrowed
    interest_rate_mode (int): Interest rate type (2 for variable). Defaults to 2 (variable) since stable rate is deprecated in AAVE V3.

    Returns:
    Union[str, None]: The transaction hash if successful, None if any step fails

    Interest Rate Modes:
    - Mode 1 (Stable): Fixed interest rate that can change under specific conditions
    - Mode 2 (Variable): Interest rate that varies based on market conditions
    Why: Stable rates provide predictability but might be higher, variable rates fluctuate but could be lower

    Implementation Details:
    --------------------
    1. Initial Setup and Validation:
       - Logs attempt to borrow with amount and asset address
       - Checks web3 connection to ensure we're connected to Ethereum
       Why: Ensures we have proper connection before attempting any transactions

    2. Contract Setup:
       - Initializes AAVE lending pool interface
       Why: Need interface to interact with AAVE's borrowing functionality

    3. Account Setup:
       - Creates account from private key
       - Gets current nonce (transaction count)
       - Retrieves current gas price
       Why: Required for transaction signing and gas estimation

    4. Amount Conversion:
       - Converts human-readable amount to token decimals
       Why: Smart contracts work with raw numbers, not decimals

    5. Borrow from AAVE:
       - Builds borrow transaction with EIP-1559 parameters
       - Signs and sends borrow transaction
       - Waits for confirmation
       Why: Actually borrows the tokens from AAVE's lending pool

    Error Handling:
    - Detailed logging of transaction states and errors
    - Transaction receipt validation
    Why: Provides clear error messages and transaction status for debugging

    Gas and Transaction Parameters:
    - Uses EIP-1559 transaction type (type 2)
    - Calculates maxFeePerGas and maxPriorityFeePerGas
    - Sets appropriate gas limits
    Why: Ensures reliable transaction processing with optimal gas costs
    """
    # Initial validation: Log the attempt and verify Ethereum connection
    logging.info(f"Attempting to borrow {amount} of asset at {asset_address} with interest rate mode {interest_rate_mode}")
    if not web3.is_connected():
        logging.error("Unable to connect to Ethereum")
        return None

    # Validate private key is set
    if _private_key is None:
        logging.error("Private key not set. Please set private key before attempting transactions.")
        return None

    try:
        # Log connection details for debugging purposes
        logging.info("Connected to Ethereum")
        
        # Initialize AAVE lending pool interface and token contract
        lending_pool = web3.eth.contract(address=aave_lending_pool_address, abi=aave_lending_pool_abi)
        
        # Define minimal ERC20 ABI for decimals
        erc20_abi = [
            {
                "constant": True,
                "inputs": [],
                "name": "decimals",
                "outputs": [{"name": "", "type": "uint8"}],
                "type": "function"
            }
        ]
        token_contract = web3.eth.contract(address=asset_address, abi=erc20_abi)
        logging.info("Contracts initialized successfully")
        
        # Setup account
        account = web3.eth.account.from_key(_private_key)
        
        # Check user's borrowing capacity
        account_data = get_user_account_data(account.address)
        if account_data is None:
            logging.error("Failed to get account data")
            return None
            
        logging.info("Account Data:")
        logging.info(f"Total Collateral: {account_data['totalCollateralBase']} (base units)")
        logging.info(f"Total Debt: {account_data['totalDebtBase']} (base units)")
        logging.info(f"Available Borrows: {account_data['availableBorrowsBase']} (base units)")
        logging.info(f"Current LTV: {account_data['ltv']}")
        logging.info(f"Health Factor: {account_data['healthFactor']}")
        
        if account_data['totalCollateralBase'] == 0:
            logging.error("No collateral supplied. Please supply collateral before borrowing.")
            return None
            
        if account_data['availableBorrowsBase'] == 0:
            logging.error("No borrowing power available. Please supply more collateral.")
            return None
        
        # Get token decimals
        token_decimals = token_contract.functions.decimals().call()
        logging.info(f"Token decimals: {token_decimals}")
        
        # Get current nonce and gas price
        nonce = web3.eth.get_transaction_count(account.address)
        logging.info(f"Account address: {account.address}")
        logging.info(f"Current nonce: {nonce}")
        logging.info(f"Current gas price: {web3.eth.gas_price}")

        # Convert human-readable amount to token decimals
        amount_in_wei = int(amount * 10**token_decimals)
        logging.info(f"Amount in token base units: {amount_in_wei}")

        try:
            # Build borrow transaction
            borrow_tx = lending_pool.functions.borrow(
                asset_address,          # Token we're borrowing
                amount_in_wei,          # Amount we're borrowing
                interest_rate_mode,     # Interest rate type (1=stable, 2=variable)
                0,                      # Referral code (not used)
                account.address         # Who will receive the borrowed tokens
            ).build_transaction({
                'from': account.address,                    # Who is borrowing
                'chainId': 11155111,                       # Sepolia testnet chain ID
                'gas': 500000,                             # Maximum gas willing to spend
                'maxFeePerGas': web3.eth.gas_price * 2,    # Maximum total fee per gas unit
                'maxPriorityFeePerGas': web3.eth.gas_price,# Tip to miners
                'nonce': nonce,                            # Transaction count
                'type': 2                                  # EIP-1559 transaction type
            })
            logging.info("Borrow transaction built successfully")

            # Sign the borrow transaction
            logging.info("Attempting to sign borrow transaction...")
            signed_tx = account.sign_transaction(borrow_tx)
            logging.info("Borrow transaction signed successfully")
            
            # Debug: Inspect SignedTransaction object
            logging.info("SignedTransaction attributes:")
            logging.info(f"Hash: {signed_tx.hash.hex()}")
            logging.info(f"r: {signed_tx.r}")  # Part of transaction signature
            logging.info(f"s: {signed_tx.s}")  # Part of transaction signature
            logging.info(f"v: {signed_tx.v}")  # Recovery value for signature
            
            # Send the borrow transaction to the network
            try:
                tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
            except Exception as e:
                logging.error("Failed to send raw transaction")
                logging.error(f"Raw transaction: {signed_tx.raw_transaction.hex()}")
                raise e
                
            logging.info(f"Borrow Transaction Hash: {tx_hash.hex()}")
            
            # Wait for borrow transaction to be mined and get receipt
            receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
            logging.info(f"Borrow transaction mined in block: {receipt['blockNumber']}")
            logging.info(f"Borrow transaction status: {'Success' if receipt['status'] == 1 else 'Failed'}")
            
            return web3.to_hex(tx_hash)
        except Exception as e:
            logging.error(f"Error in borrow transaction: {str(e)}")
            logging.error(f"Error type: {type(e)}")
            raise e
    except Exception as e:
        logging.error(f"An error occurred during the borrowing process: {e}")
        logging.error(f"Error type: {type(e)}")
        return None

@tool
def get_token_balance(token_address: str, user_address: str = None) -> Union[float, None]:
    """
    Get the token balance for a specific address.
    
    Parameters:
    token_address (str): The Ethereum address of the token
    user_address (str): The user's address to check balance for. If None, uses the connected wallet.
    
    Returns:
    Union[float, None]: The token balance in human-readable format, None if error occurs
    """
    logging.info("=== Starting get_token_balance function ===")
    logging.info(f"Input parameters - token_address: {token_address}, user_address: {user_address}")
    
    try:
        # Check web3 connection
        logging.info(f"Checking Web3 connection to: {web3.provider.endpoint_uri}")
        if not web3.is_connected():
            logging.error("Web3 is not connected!")
            return None
        logging.info("Web3 connection confirmed")

        # Handle user address
        if not user_address:
            logging.info("No user_address provided, using connected wallet")
            try:
                if _private_key is None:
                    logging.error("Private key not set. Please set private key before checking balance.")
                    return None
                account = web3.eth.account.from_key(_private_key)
                user_address = account.address
                logging.info(f"Generated address from private key: {user_address}")
            except Exception as e:
                logging.error(f"Error creating account from private key: {str(e)}")
                return None
        
        logging.info(f"Using address for balance check: {user_address}")

        # Log token contract setup
        logging.info("Setting up ERC20 ABI")
        erc20_abi = [
            {
                "constant": True,
                "inputs": [{"name": "_owner", "type": "address"}],
                "name": "balanceOf",
                "outputs": [{"name": "balance", "type": "uint256"}],
                "type": "function"
            },
            {
                "constant": True,
                "inputs": [],
                "name": "decimals",
                "outputs": [{"name": "", "type": "uint8"}],
                "type": "function"
            }
        ]

        # Initialize token contract
        logging.info(f"Initializing token contract at address: {token_address}")
        token_contract = web3.eth.contract(address=token_address, abi=erc20_abi)
        logging.info("Token contract initialized")
        
        # Get token decimals
        logging.info("Attempting to get token decimals")
        try:
            decimals = token_contract.functions.decimals().call()
            logging.info(f"Token decimals: {decimals}")
        except Exception as e:
            logging.error(f"Error getting token decimals: {str(e)}")
            logging.error(f"Error type: {type(e)}")
            return None
        
        # Get balance
        logging.info(f"Attempting to get balance for address: {user_address}")
        try:
            balance_wei = token_contract.functions.balanceOf(user_address).call()
            logging.info(f"Raw balance (wei): {balance_wei}")
        except Exception as e:
            logging.error(f"Error getting token balance: {str(e)}")
            logging.error(f"Error type: {type(e)}")
            return None
        
        # Convert to human readable format
        balance = balance_wei / (10 ** decimals)
        logging.info(f"Converted balance: {balance}")
        
        logging.info("=== get_token_balance function completed successfully ===")
        return balance
    except Exception as e:
        logging.error("=== get_token_balance function failed ===")
        logging.error(f"Error type: {type(e)}")
        logging.error(f"Error message: {str(e)}")
        logging.error(f"Error details: {e.__dict__ if hasattr(e, '__dict__') else 'No additional details'}")
        return None