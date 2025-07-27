from solcx import compile_standard, install_solc
import json

# Install Solidity compiler
install_solc("0.8.0")

# Read the Loan.sol file
with open("Loan.sol", "r") as file:
    loan_source_code = file.read()

# Compile the contract
compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {
        "Loan.sol": {
            "content": loan_source_code
        }
    },
    "settings": {
        "outputSelection": {
            "*": {
                "*": ["abi", "evm.bytecode.object"]
            }
        }
    }
}, solc_version="0.8.0")

# Extract ABI and Bytecode
abi = compiled_sol['contracts']['Loan.sol']['Loan']['abi']
bytecode = compiled_sol['contracts']['Loan.sol']['Loan']['evm']['bytecode']['object']

# Save ABI to file
with open("loan_abi.json", "w") as f:
    json.dump(abi, f)

# Save Bytecode to file
with open("loan_bytecode.txt", "w") as f:
    f.write(bytecode)

print("✅ Loan.sol compiled successfully. ABI and bytecode saved.")
