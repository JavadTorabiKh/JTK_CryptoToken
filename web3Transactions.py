from web3 import Web3

# Connect to Ethereum network using Infura
infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check if the connection is successful
if not web3.isConnected():
    print("Unable to connect to Ethereum network")
    exit()

# Smart contract address and ABI
contract_address = "0xYourContractAddress"  # Replace with your contract address
abi = [
    # Place your contract ABI here
]

# Create a contract instance
contract = web3.eth.contract(address=contract_address, abi=abi)

# Function to get the token name


def get_token_name():
    name = contract.functions.name().call()
    print(f"Token Name: {name}")

# Function to get the token symbol


def get_token_symbol():
    symbol = contract.functions.symbol().call()
    print(f"Token Symbol: {symbol}")

# Function to get the balance of a specific address


def get_balance(account_address):
    balance = contract.functions.balanceOf(account_address).call()
    # Adjust token symbol if needed
    print(f"Balance of {account_address}: {balance} MTK")

# Function to transfer tokens from one address to another


def transfer_tokens(from_address, private_key, to_address, amount):
    # Get the nonce for the transaction
    nonce = web3.eth.getTransactionCount(from_address)

    # Build the transaction
    transaction = contract.functions.transfer(to_address, amount).buildTransaction({
        'chainId': 1,  # Mainnet chain ID
        'gas': 2000000,  # Gas limit
        'gasPrice': web3.toWei('50', 'gwei'),  # Gas price
        'nonce': nonce,
    })

    # Sign the transaction with the sender's private key
    signed_txn = web3.eth.account.signTransaction(transaction, private_key)

    # Send the signed transaction
    tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    print(f"Transaction sent: {web3.toHex(tx_hash)}")


# Example usage
if __name__ == "__main__":
    get_token_name()  # Retrieve and print token name
    get_token_symbol()  # Retrieve and print token symbol
    get_balance("0xYourAccountAddress")  # Replace with your account address

    # To transfer tokens, uncomment and provide the necessary details:
    # transfer_tokens("0xYourFromAddress", "YOUR_PRIVATE_KEY", "0xRecipientAddress", 100)
