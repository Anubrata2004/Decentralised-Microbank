// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Withdraw {
    struct Withdrawal {
        address from;  // Bank address (assigned)
        address to;    // User address
        uint256 amount;
        uint256 timestamp;
    }

    Withdrawal[] public withdrawals;

    event Withdrawn(address indexed from, address indexed to, uint256 amount, uint256 timestamp);

    function withdrawTo(address payable to) public payable {
        require(msg.value > 0, "Amount must be greater than zero");
        require(to != address(0), "Recipient cannot be zero address");

        withdrawals.push(Withdrawal(msg.sender, to, msg.value, block.timestamp));
        to.transfer(msg.value);

        emit Withdrawn(msg.sender, to, msg.value, block.timestamp);
    }

    function getAllWithdrawals() public view returns (Withdrawal[] memory) {
        return withdrawals;
    }

    function getWithdrawalCount() public view returns (uint256) {
        return withdrawals.length;
    }
}
