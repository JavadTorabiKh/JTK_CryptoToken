from web3 import Web3
from web3.contract import Contract
from web3.middleware import geth_poa_middleware
from eth_account import Account


providerUrl = 'https://sepolia.infura.io/v3/08bc373c28134da2893b83f543fa3ad3'  
web3 = Web3(Web3.HTTPProvider(providerUrl))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)  

print(web3.is_connected())

contractABI = [
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			}
		],
		"name": "OwnableInvalidOwner",
		"type": "error"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "account",
				"type": "address"
			}
		],
		"name": "OwnableUnauthorizedAccount",
		"type": "error"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "previousOwner",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "OwnershipTransferred",
		"type": "event"
	},
	{
		"inputs": [],
		"name": "renounceOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "sendAmount",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_amount",
				"type": "uint256"
			},
			{
				"internalType": "address payable",
				"name": "_to",
				"type": "address"
			}
		],
		"name": "transfer",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_from",
				"type": "address"
			},
			{
				"internalType": "address payable",
				"name": "_to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_amount",
				"type": "uint256"
			}
		],
		"name": "transferFrom",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "transferOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_addr",
				"type": "address"
			}
		],
		"name": "getBalance",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getBalanceContract",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
contract_address = '0xee577210aFA5ECF45B74D65b500324A71ddd6E83'
contract = web3.eth.contract(address=contract_address, abi=contractABI)
wallet_address = '0x99baFA590a24755f94F5815df06102C2450AcD3D'
private_key = ''

# -----------------------------------------------------------------------------------

## VIEW FUNCTIONS
# index = "0x99baFA590a24755f94F5815df06102C2450AcD3D"  
# result = contract.functions.getBalance(index).call()
# print(result)

# -----------------------------------------------------------------------------------

# # transfer Token functions
# function_address = contract.functions.transfer(100, '0x99baFA590a24755f94F5815df06102C2450AcD3D').address

# transaction = {
#     'to': contract_address,
#     'data': contract.encodeABI(fn_name='transfer', args=[100, '0x99baFA590a24755f94F5815df06102C2450AcD3D']),
#     'gas': 200000,  
#     'gasPrice': web3.to_wei('50', 'gwei'),  
#     'nonce': web3.eth.get_transaction_count(wallet_address), 
# }

# signed_transaction = web3.eth.account.sign_transaction(transaction, private_key=private_key)
# transaction_hash = web3.eth.send_raw_transaction(signed_transaction.rawTransaction)
# print(f'Transaction sent: {transaction_hash.hex()}')

# ------------------------------------------------------------------------------------

# send amount with payable functions to contract
function_address = contract.functions.sendAmount().address
amount_ether = web3.to_wei(0.000000000000001, 'ether') 

transaction = {
    'to': contract_address,
    'data': contract.encodeABI(fn_name='sendAmount', args=[]),
    'value': amount_ether,
    'gas': 200000,  
    'gasPrice': web3.to_wei('50', 'gwei'),  
    'nonce': web3.eth.get_transaction_count(wallet_address), 
}

signed_transaction = web3.eth.account.sign_transaction(transaction, private_key=private_key)
transaction_hash = web3.eth.send_raw_transaction(signed_transaction.rawTransaction)
print(f'Transaction sent: {transaction_hash.hex()}')

# -------------------------------------------------------------------------------------