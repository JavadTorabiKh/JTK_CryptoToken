# 🪙 JTK (Javad Token) - Personal ERC-20 Token
    ✨ Created by Javad Tarabi
    🔗 Standard: ERC-20 on Ethereum


## 🚀 Introduction

JTK is a custom ERC-20 token deployed on the Ethereum network, designed for learning, experimentation, and blockchain development. It features 9 decimal places for precise transactions.

---

## 🔑 Key Features

    ✅ Fully ERC-20 Compliant
    ✅ 9 Decimal Places (e.g., 1 JTK = 1,000,000,000 smallest units)
    ✅ Python & Web3.py Integration
    ✅ Deployable on EVM Networks (Ethereum, Polygon, etc.)

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

---

## 🔗 Contract Details

📜 Contract Address: 0xYOUR_CONTRACT_ADDRESS

📊 Total Supply: 1,000,000 JTK

🔢 Decimals: 9

📄 Etherscan: View Contract

---

## 📜 License

    MIT License.

---

## 💬 Contact

👨💻 Javad Tarabi
📧 Email: javadtorabi462@gmail.com

---

## 🌟 Contributions welcome!

Built with ❤️ by Javad Tababi | Powered by Ethereum & Web3.py

---

## Notes:

Security: Never hardcode private keys (use environment variables).

Testnets: Use Sepolia for testing.

Gas Optimization: Fetch dynamic gas_price with w3.eth.gas_price.

Let me know if you'd like to add deployment steps or other technical details! 😊