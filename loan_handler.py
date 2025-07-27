from web3 import Web3
import json
import datetime

# Ganache URL
ganache_url = "http://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(ganache_url))

# Admin (MetaMask) account and private key
admin_address = "0x92b2422E8597482C106Be235d6c3B06CEc270184"
private_key = "3bad5f464c8335f97fbb0914d46d7f37734b4dbe65afaf1af6a0bdf6234d9530"

# Load ABI and contract address
with open("loan_abi.json", "r") as f:
    abi = json.load(f)

with open("loan_contract_address.txt", "r") as f:
    contract_address = f.read().strip()

# Connect to contract
contract = w3.eth.contract(address=contract_address, abi=abi)

def give_loan(to_address, amount_eth):
    try:
        # Convert amount to Wei
        amount_wei = w3.to_wei(amount_eth, 'ether')

        # Check admin balance
        balance = w3.eth.get_balance(admin_address)
        if amount_wei > balance:
            return f"❌ Not enough balance in admin account. Available: {w3.from_wei(balance, 'ether')} ETH"

        # Build transaction to call giveLoan()
        nonce = w3.eth.get_transaction_count(admin_address)
        txn = contract.functions.giveLoan(to_address).build_transaction({
            'from': admin_address,
            'value': amount_wei,
            'gas': 300000,
            'gasPrice': w3.to_wei('20', 'gwei'),
            'nonce': nonce
        })

        # Sign and send transaction
        signed_txn = w3.eth.account.sign_transaction(txn, private_key=private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

        # Fetch balances after transaction
        new_balance_admin = w3.from_wei(w3.eth.get_balance(admin_address), 'ether')
        new_balance_user = w3.from_wei(w3.eth.get_balance(to_address), 'ether')
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return {
            "status": "✅ Loan successful",
            "tx_hash": tx_hash.hex(),
            "to": to_address,
            "amount": amount_eth,
            "admin_balance": str(new_balance_admin),
            "user_balance": str(new_balance_user),
            "timestamp": timestamp
        }

    except Exception as e:
        return {"status": "❌ Error", "message": str(e)}
