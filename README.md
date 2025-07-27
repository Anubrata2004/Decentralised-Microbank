# 🏦 Decentralised Microbank

A blockchain-powered microbanking system built for underbanked or rural communities. It supports secure deposits, withdrawals, and loans through Ethereum smart contracts and local Ganache testnet.

---

## 🎯 Key Features

- 🔐 **User & Admin Login System**
  - Users are assigned a blockchain address and private key during registration
  - Admin (Bank) uses a MetaMask account to fund loans

- 💰 **Deposit Functionality**
  - Users deposit Ether from one wallet to their assigned bank wallet
  - Transactions are recorded immutably with a timestamp

- 💸 **Withdrawal Functionality**
  - Users withdraw Ether to their external wallet
  - Entire flow stored securely on-chain

- 🏦 **Loan Functionality**
  - Admin gives Ether-based loans from MetaMask bank account
  - Records are maintained on-chain

- 🧾 **Smart Contract Transaction Logs**
  - View all deposits, withdrawals, and loans with timestamps

---

## 🧠 Why This Matters

> Over 1.7 billion people worldwide remain unbanked. This system simulates a **trustless microbanking model** with transparency, auditability, and no need for intermediaries. Blockchain ensures:
- ✅ No tampering with transactions
- ✅ Timestamp-based proof of operations
- ✅ Immutable records for auditing & trust

---

## 🛠️ Tech Stack

| Layer        | Technology                       |
|--------------|----------------------------------|
| Smart Contract | Solidity                         |
| Blockchain   | Ethereum (Ganache Local Testnet) |
| Backend      | Python (Flask / FastAPI), Web3.py |
| Frontend     | HTML, CSS (3D styled), JavaScript |
| Database     | SQLite                            |
| Wallet       | MetaMask (Admin), Ganache Wallets (Users) |
