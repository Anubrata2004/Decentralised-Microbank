from fastapi import FastAPI
from web3 import Web3
import json

app = FastAPI()

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# Load ABIs
with open("DepositContract_abi.json") as f:
    deposit_abi = json.load(f)

with open("WithdrawContract_abi.json") as f:
    withdraw_abi = json.load(f)

with open("loan_abi.json") as f:
    loan_abi = json.load(f)

# Replace these with your deployed contract addresses
deposit_address = "0x9e229fdf35069e73C4C7Ff3f106E75c2B64B6df3"
withdraw_address = "0xEADF0C716d71491580027Cf0557Effe49fC50e9D"
loan_address = "0x701b666328819ad9948348a7806fE650F01106C3"

# Contract instances
deposit_contract = w3.eth.contract(address=deposit_address, abi=deposit_abi)
withdraw_contract = w3.eth.contract(address=withdraw_address, abi=withdraw_abi)
loan_contract = w3.eth.contract(address=loan_address, abi=loan_abi)

# Routes
@app.get("/")
def welcome():
    return {"message": "Welcome to Decentralized Bank API"}

@app.get("/transactions/deposits")
def get_deposits():
    events = deposit_contract.events.DepositMade.create_filter(fromBlock=0).get_all_entries()
    return [{"from": e["args"]["from"], "to": e["args"]["to"], "amount": w3.fromWei(e["args"]["amount"], 'ether'), "timestamp": e["args"]["timestamp"]} for e in events]

@app.get("/transactions/withdrawals")
def get_withdrawals():
    events = withdraw_contract.events.WithdrawalMade.create_filter(fromBlock=0).get_all_entries()
    return [{"from": e["args"]["from"], "to": e["args"]["to"], "amount": w3.fromWei(e["args"]["amount"], 'ether'), "timestamp": e["args"]["timestamp"]} for e in events]

@app.get("/transactions/loans")
def get_loans():
    events = loan_contract.events.LoanIssued.create_filter(fromBlock=0).get_all_entries()
    return [{"to": e["args"]["to"], "amount": w3.fromWei(e["args"]["amount"], 'ether'), "timestamp": e["args"]["timestamp"]} for e in events]
