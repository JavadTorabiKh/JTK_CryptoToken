#!/usr/bin/env python3
"""
JavadToken Deployment and Interaction Script
Requirements: web3.py, python-dotenv
"""

import json
import os
from web3 import Web3
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()


class JavadTokenDeployer:
    def __init__(self, rpc_url, private_key):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.account = self.w3.eth.account.from_key(private_key)
        self.contract = None

    def deploy_contract(self, contract_path):
        """Deploy the JavadToken contract"""
        # Compile contract (you need solc for this)
        compiled_contract = self.compile_contract(contract_path)

        # Get contract interface
        contract_interface = compiled_contract['<stdin>:JavadToken']

        # Create contract
        contract = self.w3.eth.contract(
            abi=contract_interface['abi'],
            bytecode=contract_interface['bin']
        )

        # Build transaction
        transaction = contract.constructor().build_transaction({
            'from': self.account.address,
            'nonce': self.w3.eth.get_transaction_count(self.account.address),
            'gas': 2000000,
            'gasPrice': self.w3.eth.gas_price
        })

        # Sign and send transaction
        signed_txn = self.w3.eth.account.sign_transaction(
            transaction, private_key)
        tx_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)

        # Wait for receipt
        receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)

        print(f"✅ Contract deployed at: {receipt.contractAddress}")
        return receipt.contractAddress

    def load_contract(self, contract_address, abi_path):
        """Load existing contract instance"""
        with open(abi_path, 'r') as f:
            abi = json.load(f)

        self.contract = self.w3.eth.contract(
            address=contract_address,
            abi=abi
        )
        return self.contract

    def transfer(self, to_address, amount):
        """Transfer tokens"""
        if not self.contract:
            raise Exception("Contract not loaded")

        transaction = self.contract.functions.transfer(
            to_address,
            amount
        ).build_transaction({
            'from': self.account.address,
            'nonce': self.w3.eth.get_transaction_count(self.account.address),
            'gas': 100000,
            'gasPrice': self.w3.eth.gas_price
        })

        signed_txn = self.w3.eth.account.sign_transaction(
            transaction, private_key)
        tx_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)

        print(f"✅ Transfer successful: {tx_hash.hex()}")
        return receipt

    def get_balance(self, address=None):
        """Get token balance"""
        if not self.contract:
            raise Exception("Contract not loaded")

        if not address:
            address = self.account.address

        balance = self.contract.functions.balanceOf(address).call()
        return balance

    def burn_tokens(self, amount):
        """Burn tokens"""
        if not self.contract:
            raise Exception("Contract not loaded")

        transaction = self.contract.functions.burn(amount).build_transaction({
            'from': self.account.address,
            'nonce': self.w3.eth.get_transaction_count(self.account.address),
            'gas': 100000,
            'gasPrice': self.w3.eth.gas_price
        })

        signed_txn = self.w3.eth.account.sign_transaction(
            transaction, private_key)
        tx_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)

        print(f"✅ Burn successful: {tx_hash.hex()}")
        return receipt


# Usage example
if __name__ == "__main__":
    # Configuration
    RPC_URL = os.getenv(
        'RPC_URL', 'https://sepolia.infura.io/v3/YOUR_PROJECT_ID')
    PRIVATE_KEY = os.getenv('PRIVATE_KEY')
    CONTRACT_ADDRESS = os.getenv('CONTRACT_ADDRESS')

    if not PRIVATE_KEY:
        raise ValueError("Please set PRIVATE_KEY in environment variables")

    # Initialize deployer
    deployer = JavadTokenDeployer(RPC_URL, PRIVATE_KEY)

    # Deploy new contract (uncomment to deploy)
    # contract_address = deployer.deploy_contract("JavadToken.sol")

    # Or load existing contract
    if CONTRACT_ADDRESS:
        contract = deployer.load_contract(CONTRACT_ADDRESS, "JavadToken.abi")

        # Example interactions
        balance = deployer.get_balance()
        print(f"💰 Your balance: {balance} JTK")

        # Transfer example
        # deployer.transfer("0xRecipientAddress", 1000000000)  # 1 token

        # Burn example
        # deployer.burn_tokens(500000000)  # 0.5 tokens
