from web3 import Web3
import json

# Connect to Ganache
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# Load ABI and Bytecode
with open("WithdrawContract_abi.json", "r") as f:
    abi = json.load(f)

with open("WithdrawContract_bytecode.txt", "r") as f:
    bytecode = f.read()

# Use first Ganache account for deployment
deployer = web3.eth.accounts[0]

# Contract instance
contract = web3.eth.contract(abi=abi, bytecode=bytecode)

# Build transaction
tx = contract.constructor().build_transaction({
    'from': deployer,
    'nonce': web3.eth.get_transaction_count(deployer),
    'gas': 3000000,
    'gasPrice': web3.to_wei('20', 'gwei')
})

# Send transaction
tx_hash = web3.eth.send_transaction(tx)
receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

# Save contract address
with open("WithdrawContract_address.txt", "w") as f:
    f.write(receipt.contractAddress)

print("✅ Withdraw contract deployed at:", receipt.contractAddress)
