from web3 import Web3
import json

# Connect to Ganache
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# Load ABI and Bytecode
with open("DepositContract_abi.json", "r") as f:
    abi = json.load(f)

with open("DepositContract_bytecode.txt", "r") as f:
    bytecode = f.read()

# Pick the first account from Ganache
account = web3.eth.accounts[0]

# Build contract instance
contract = web3.eth.contract(abi=abi, bytecode=bytecode)

# Build transaction
tx = contract.constructor().build_transaction({
    'from': account,
    'nonce': web3.eth.get_transaction_count(account),
    'gas': 3000000,
    'gasPrice': web3.to_wei('20', 'gwei')
})

# Sign and send transaction (no private key needed for unlocked Ganache accounts)
tx_hash = web3.eth.send_transaction(tx)
receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

print("✅ Contract deployed at:", receipt.contractAddress)

# Save address
with open("DepositContract_address.txt", "w") as f:
    f.write(receipt.contractAddress)
