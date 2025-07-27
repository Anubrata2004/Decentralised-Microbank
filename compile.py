from solcx import compile_standard, install_solc
import json

# Step 1: Install Solidity 0.8.0 (only once)
install_solc("0.8.0")

# Step 2: Read the contract file
with open("Deposit.sol", "r") as file:
    source_code = file.read()

# Step 3: Compile the contract
compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {
        "Deposit.sol": {
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

# Step 4: Extract ABI and Bytecode
abi = compiled_sol["contracts"]["Deposit.sol"]["Deposit"]["abi"]
bytecode = compiled_sol["contracts"]["Deposit.sol"]["Deposit"]["evm"]["bytecode"]["object"]

# Step 5: Save ABI
with open("DepositContract_abi.json", "w") as abi_file:
    json.dump(abi, abi_file)

# Step 6: Save Bytecode
with open("DepositContract_bytecode.txt", "w") as bytecode_file:
    bytecode_file.write(bytecode)

print("✅ Compilation successful. ABI and bytecode saved.")
