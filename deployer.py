import json
import os
from web3 import Web3
from solcx import compile_standard, install_solc

# Configuration
CONTRACT_NAME = "MyToken"
CONTRACT_FILE = "JTK.sol"
RPC_URL = "https://sepolia.infura.io/v3/YOUR_INFURA_KEY"  # Testnet
PRIVATE_KEY = "YOUR_PRIVATE_KEY"  # Never commit this!
CHAIN_ID = 11155111  # Sepolia testnet
GAS_LIMIT = 3000000


def compile_contract():
    print("🛠️ Compiling contract...")
    install_solc('0.8.0')

    with open(CONTRACT_FILE, "r") as file:
        contract_source = file.read()

    compiled_sol = compile_standard({
        "language": "Solidity",
        "sources": {CONTRACT_FILE: {"content": contract_source}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "evm.bytecode"]}
            }
        }
    })

    with open("compiled_code.json", "w") as file:
        json.dump(compiled_sol, file)

    return compiled_sol


def deploy_contract(compiled_contract):
    print("🚀 Deploying contract...")
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    account = w3.eth.account.from_key(PRIVATE_KEY)

    # Get contract data
    contract_data = compiled_contract["contracts"][CONTRACT_FILE][CONTRACT_NAME]
    bytecode = contract_data["evm"]["bytecode"]["object"]
    abi = contract_data["abi"]

    # Create contract instance
    MyToken = w3.eth.contract(abi=abi, bytecode=bytecode)

    # Build transaction
    transaction = MyToken.constructor().build_transaction({
        "chainId": CHAIN_ID,
        "gas": GAS_LIMIT,
        "gasPrice": w3.eth.gas_price,
        "nonce": w3.eth.get_transaction_count(account.address),
    })

    # Sign and send transaction
    signed_txn = w3.eth.account.sign_transaction(transaction, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    print(f"✅ Contract deployed at: {tx_receipt.contractAddress}")
    print(
        f"📄 View on Etherscan: https://sepolia.etherscan.io/address/{tx_receipt.contractAddress}")

    # Save contract address and ABI
    with open("deployed_contract.json", "w") as file:
        json.dump({
            "address": tx_receipt.contractAddress,
            "abi": abi
        }, file)

    return tx_receipt.contractAddress, abi


if __name__ == "__main__":
    print(f"🔨 Starting {CONTRACT_NAME} deployment...")

    # Step 1: Compile
    compiled = compile_contract()

    # Step 2: Deploy
    contract_address, abi = deploy_contract(compiled)

    print("\n🎉 Deployment complete!")
    print(f"Contract Address: {contract_address}")
