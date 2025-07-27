from web3 import Web3
import json

# Connect to local Ganache node
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# Load ABIs
with open("abi/deposit_abi.json") as f:
    deposit_abi = json.load(f)

with open("abi/withdraw_abi.json") as f:
    withdraw_abi = json.load(f)

with open("abi/loan_abi.json") as f:
    loan_abi = json.load(f)

# Contract addresses
deposit_address = "0x9e229fdf35069e73C4C7Ff3f106E75c2B64B6df3"
withdraw_address = "0xEADF0C716d71491580027Cf0557Effe49fC50e9D"
loan_address = "0x701b666328819ad9948348a7806fE650F01106C3"

# Contract instances
deposit_contract = w3.eth.contract(address=deposit_address, abi=deposit_abi)
withdraw_contract = w3.eth.contract(address=withdraw_address, abi=withdraw_abi)
loan_contract = w3.eth.contract(address=loan_address, abi=loan_abi)

# Fetch events
def get_deposit_events():
    return deposit_contract.events.DepositMade.create_filter(fromBlock=0).get_all_entries()

def get_withdrawal_events():
    return withdraw_contract.events.WithdrawalMade.create_filter(fromBlock=0).get_all_entries()

def get_loan_events():
    return loan_contract.events.LoanIssued.create_filter(fromBlock=0).get_all_entries()

# Print them
print("🔵 Deposit Events:")
for e in get_deposit_events():
    print(dict(e['args']))

print("\n🟠 Withdrawal Events:")
for e in get_withdrawal_events():
    print(dict(e['args']))

print("\n🟢 Loan Events:")
for e in get_loan_events():
    print(dict(e['args']))
