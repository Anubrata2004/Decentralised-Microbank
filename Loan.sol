// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Loan {
    struct LoanTransaction {
        address from;
        address to;
        uint amount;
        uint timestamp;
    }

    LoanTransaction[] public loans;

    function giveLoan(address to) public payable {
        require(msg.value > 0, "Loan amount must be greater than 0");
        payable(to).transfer(msg.value);

        loans.push(LoanTransaction({
            from: msg.sender,
            to: to,
            amount: msg.value,
            timestamp: block.timestamp
        }));
    }

    function getAllLoans() public view returns (LoanTransaction[] memory) {
        return loans;
    }

    function getLoanCount() public view returns (uint) {
        return loans.length;
    }
}
