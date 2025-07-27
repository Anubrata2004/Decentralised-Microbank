// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Deposit {
    struct Transaction {
        address from;
        address to;
        uint256 amount;
        uint256 timestamp;
    }

    Transaction[] public transactions;

    event Deposited(address indexed from, address indexed to, uint256 amount, uint256 timestamp);

    function deposit(address to) public payable {
        require(msg.value > 0, "Amount must be greater than 0");
        require(to != address(0), "Recipient cannot be zero address");

        // Log transaction
        transactions.push(Transaction(msg.sender, to, msg.value, block.timestamp));

        // Transfer Ether
        payable(to).transfer(msg.value);

        emit Deposited(msg.sender, to, msg.value, block.timestamp);
    }

    function getAllTransactions() public view returns (Transaction[] memory) {
        return transactions;
    }

    function getTransactionCount() public view returns (uint256) {
        return transactions.length;
    }
}
