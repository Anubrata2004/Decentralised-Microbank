from solcx import compile_standard, install_solc
import json

# Install Solidity compiler version
install_solc('0.8.0')

# Read the contract
with open("Withdraw.sol", "r") as f:
    source_code = f.read()

# Compile the contract
compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {
        "Withdraw.sol": {
            "content": source_code
        }
    },
    "settings": {
        "outputSelection": {
            "*": {
                "*": ["abi", "evm.bytecode"]
            }
        }
    }
}, solc_version="0.8.0")

# Extract ABI and Bytecode
abi = compiled_sol['contracts']['Withdraw.sol']['Withdraw']['abi']
bytecode = compiled_sol['contracts']['Withdraw.sol']['Withdraw']['evm']['bytecode']['object']

# Save ABI
with open("WithdrawContract_abi.json", "w") as f:
    json.dump(abi, f)

# Save Bytecode
with open("WithdrawContract_bytecode.txt", "w") as f:
    f.write(bytecode)

print("✅ Withdraw.sol compiled successfully.")
