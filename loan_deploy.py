from web3 import Web3
import json

# Connect to Ganache
ganache_url = "http://127.0.0.1:7545"  # Change if needed
w3 = Web3(Web3.HTTPProvider(ganache_url))

# Admin MetaMask account
admin_address = "0x92b2422E8597482C106Be235d6c3B06CEc270184"
private_key = "3bad5f464c8335f97fbb0914d46d7f37734b4dbe65afaf1af6a0bdf6234d9530"

# Load ABI and Bytecode
with open("loan_abi.json", "r") as f:
    abi = json.load(f)

with open("loan_bytecode.txt", "r") as f:
    bytecode = f.read()

# Create the contract in Python
Loan = w3.eth.contract(abi=abi, bytecode=bytecode)

# Get the latest transaction nonce
nonce = w3.eth.get_transaction_count(admin_address)

# Build transaction
txn_dict = Loan.constructor().build_transaction({
    'from': admin_address,
    'nonce': nonce,
    'gas': 3000000,
    'gasPrice': w3.to_wei('20', 'gwei')
})

# Sign the transaction
signed_txn = w3.eth.account.sign_transaction(txn_dict, private_key=private_key)

# Send the transaction
tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# Save the contract address
with open("loan_contract_address.txt", "w") as f:
    f.write(tx_receipt.contractAddress)

print("✅ Loan contract deployed at:", tx_receipt.contractAddress)
