# AAVE DeFi Assistant

A conversational AI agent that helps users interact with the AAVE protocol on Ethereum's Sepolia testnet. Built with LangGraph and Streamlit.

## What is AAVE?

AAVE is a decentralized finance (DeFi) protocol that enables users to:
- Lend crypto assets to earn interest
- Borrow crypto assets by providing collateral
- Participate in decentralized lending markets

## Features

- 🔍 Check token balances for USDC, DAI, WBTC, and USDT
- 💰 Lend your crypto assets to earn interest
- 💸 Borrow crypto assets using your deposited tokens as collateral
- 💬 Natural language interface for easy interaction

## Quick Start

1. **Install Dependencies**
```bash
pip install -r requirements.txt
```

2. **Set Environment Variables**
Create a `.env` file with:
```
RPC_URL=your_ethereum_rpc_url
```

3. **Run the Application**
```bash
streamlit run main.py
```

4. **Connect Your Wallet**
- Input your Groq API key
- Input your wallet's private key
- Start interacting with AAVE through natural language!

## How it Works

This project uses LangGraph to create an AI agent that can:
1. Understand user intentions through natural language
2. Execute appropriate actions on the AAVE protocol
3. Manage conversation state and tool execution flow

The agent is built as a state machine that can:
- Process user inputs
- Make decisions about which DeFi operations to perform
- Execute transactions on the Ethereum network
- Provide feedback in natural language

## Supported Tokens (Sepolia Testnet)

- USDC: 0x94a9D9AC8a22534E3FaCa9F4e7F2E2cf85d5E4C8
- DAI: 0xFF34B3d4Aee8ddCd6F9AFFFB6Fe49bD371b8a357
- WBTC: 0x29f2D40B0605204364af54EC677bD022dA425d03
- USDT: 0xaA8E23Fb1079EA71e0a56F48a2aA51851D8433D0

## Security Note

⚠️ Never share your private key
⚠️ Only use test tokens on Sepolia testnet
⚠️ Double-check all transaction details before confirming

## Requirements

- Python 3.8+
- Groq API key
- Ethereum wallet with Sepolia testnet ETH
- Sepolia testnet tokens for testing
