# 🪙 JTK (Javad Token) - Personal ERC-20 Token
- ✨ Created by Javad Tarabi
- 🔗 Standard: ERC-20 on Ethereum


## 🚀 Introduction

JTK is a custom ERC-20 token deployed on the Ethereum network, designed for learning, experimentation, and blockchain development. It features 9 decimal places for precise transactions.

---

## 🔑 Key Features

- ✅ Fully ERC-20 Compliant
- ✅ 9 Decimal Places (e.g., 1 JTK = 1,000,000,000 smallest units)
- ✅ Python & Web3.py Integration
- ✅ Deployable on EVM Networks (Ethereum, Polygon, etc.)

---

## 📦 Setup & Usage
1. Prerequisites

    - Python 3.8+

    - web3.py library

    - MetaMask (for testing)

    - Ethereum node access (Infura/Alchemy)


2. Install Dependencies
```bash
    pip install -r requirements.txt
```


3. Check Token Balance

```python
    def check_balance(address):
        balance = contract.functions.balanceOf(address).call()
        human_balance = balance / 10**9  # Convert to JTK units
        print(f"Balance: {human_balance} JTK")

    check_balance("0xYOUR_WALLET_ADDRESS")
```