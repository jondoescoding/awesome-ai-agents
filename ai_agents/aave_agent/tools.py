"""
Tools
-------------------
What:
This script is the warehouse of tools that the AI Agent has access to. It controls what the agent can do when interacting with the DeFi platform, AAVE. As of the current implementation the agent can both borrow and lend on the AAVE platform.


Functions:
    lend_tokens
    borrow_tokens
"""
# Built in python imports
import os
import json
import logging
from typing import Union
from dotenv import load_dotenv

# Web 3 Interactions
from web3 import Web3

"""
Initial Setup -> GLOBAL VARIABLES
"""
rpc_url = os.getenv("RPC_URL") # what will be used to connect to the blockchain
aave_lending_pool_address = "0x6Ae43d3271ff6888e7Fc43Fd7321a503ff738951"

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(rpc_url))

# Load AAVE Lending Pool ABI
with open('./aave_lending_pool_abi.json', 'r') as abi_file:
    aave_lending_pool_abi = json.load(abi_file)

load_dotenv()
private_key = os.getenv("PRIVATE_KEY")

def lend_crypto(amount: float, asset_address: str) -> Union[str, None]:
    """
    Lend cryptocurrency to the AAVE lending pool.

    Parameters:
    amount (float): The amount of cryptocurrency to lend.
    asset_address (str): The address of the asset to lend.

    Returns:
    Union[str, None]: The transaction hash if successful, None otherwise.
    """
    if not web3.is_connected():
        logging.error("Unable to connect to Ethereum")
        return None

    try:
        lending_pool = web3.eth.contract(address=aave_lending_pool_address, abi=aave_lending_pool_abi)
        account = web3.eth.account.from_key(private_key)
        nonce = web3.eth.get_transaction_count(account.address) + 1 # increment nonce by 1 to avoid nonce collision
        logging.info(f"Lending from this address: {account.address}")

        amount_in_wei = int(web3.from_wei(amount, 'ether'))

        tx = lending_pool.functions.deposit(asset_address, web3.from_wei(amount_in_wei, 'ether'), account.address, 0).build_transaction({
            'chainId': 11155111,
            'gas': 700000,
            'gasPrice': web3.eth.gas_price * 2, 
            'nonce': nonce,
        })

        logging.info(f"Transaction before estimation: {tx}")

        tx['gas'] = web3.eth.estimate_gas(tx)
        logging.info(f"Estimated gas: {tx['gas']}")

        signed_tx = web3.eth.account.sign_transaction(tx, private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        logging.info(f"Lending Transaction Hash: {tx_hash.hex()}")
        return web3.to_hex(tx_hash)
    except Exception as e:
        logging.error(f"An error occurred during lending: {e}")
        return None