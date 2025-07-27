from web3 import Web3
import json
import time

# Connect to Ganache
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# Load ABI
with open("WithdrawContract_abi.json") as f:
    abi = json.load(f)

# Load contract address
with open("WithdrawContract_address.txt") as f:
    contract_address = f.read().strip()

# Create contract instance
contract = web3.eth.contract(address=contract_address, abi=abi)

def withdraw_funds(from_address, from_private_key, to_address, amount_eth):
    try:
        # Convert Ether to Wei
        amount_wei = web3.to_wei(amount_eth, 'ether')

        # Check if sender has enough balance
        sender_balance = web3.eth.get_balance(from_address)
        if sender_balance < amount_wei:
            return {"error": "Insufficient balance in sender account."}

        # Build transaction to call withdrawTo(to_address)
        txn = contract.functions.withdrawTo(to_address).build_transaction({
            'from': from_address,
            'value': amount_wei,
            'gas': 300000,
            'gasPrice': web3.to_wei('20', 'gwei'),
            'nonce': web3.eth.get_transaction_count(from_address)
        })

        # Sign the transaction
        signed_txn = web3.eth.account.sign_transaction(txn, private_key=from_private_key)

        # Send the transaction
        tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)

        # Wait for confirmation
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

        # Get updated balances
        sender_new_balance = web3.from_wei(web3.eth.get_balance(from_address), 'ether')
        recipient_new_balance = web3.from_wei(web3.eth.get_balance(to_address), 'ether')

        # Current timestamp
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        return {
            "tx_hash": tx_hash.hex(),
            "from_address": from_address,
            "to_address": to_address,
            "amount_eth": amount_eth,
            "sender_new_balance": str(sender_new_balance),
            "recipient_new_balance": str(recipient_new_balance),
            "timestamp": timestamp
        }

    except Exception as e:
        return {"error": str(e)}
