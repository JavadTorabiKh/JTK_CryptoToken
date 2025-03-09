from web3 import Web3
from web3.contract import Contract
from web3.middleware import geth_poa_middleware
from eth_account import Account

from abi import contractABI
from config import PROVIDERINFURA, CONTRACT, WALLET, PRIVATEKEY


web3 = Web3(Web3.HTTPProvider(PROVIDERINFURA))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

print("connection : ", web3.is_connected())

# contract object
contract = web3.eth.contract(address=CONTRACT, abi=contractABI)


# -----------------------------------------------------------------------------------

# VIEW FUNCTIONS
index = "0x99baFA590a24755f94F5815df06102C2450AcD3D"
result = contract.functions.getBalance(index).call()
print(result)

# -----------------------------------------------------------------------------------

# transfer Token functions
function_address = contract.functions.transfer(
    100, '0x99baFA590a24755f94F5815df06102C2450AcD3D').address

transaction = {
    'to': CONTRACT,
    'data': contract.encodeABI(fn_name='transfer', args=[100, '0x99baFA590a24755f94F5815df06102C2450AcD3D']),
    'gas': 200000,
    'gasPrice': web3.to_wei('50', 'gwei'),
    'nonce': web3.eth.get_transaction_count(WALLET),
}

signed_transaction = web3.eth.account.sign_transaction(
    transaction, private_key=PRIVATEKEY)
transaction_hash = web3.eth.send_raw_transaction(
    signed_transaction.rawTransaction)
print(f'Transaction sent: {transaction_hash.hex()}')

# ------------------------------------------------------------------------------------

# send amount with payable functions to contract
function_address = contract.functions.sendAmount().address
amount_ether = web3.to_wei(0.000000000000001, 'ether')

transaction = {
    'to': CONTRACT,
    'data': contract.encodeABI(fn_name='sendAmount', args=[]),
    'value': amount_ether,
    'gas': 200000,
    'gasPrice': web3.to_wei('50', 'gwei'),
    'nonce': web3.eth.get_transaction_count(WALLET),
}

signed_transaction = web3.eth.account.sign_transaction(
    transaction, private_key=PRIVATEKEY)
transaction_hash = web3.eth.send_raw_transaction(
    signed_transaction.rawTransaction)
print(f'Transaction sent: {transaction_hash.hex()}')

# -------------------------------------------------------------------------------------
