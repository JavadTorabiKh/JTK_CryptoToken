// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;


import "liberary/safeMath.sol";
import "liberary/Ownable.sol";

contract MyContract is Ownable(msg.sender) {
    using SafeMath for uint256;

    mapping(address => uint256) private _balances;

    function getBalance(address _addr) public view returns (uint256) {
        return _balances[_addr];
    }

    function getBalanceContract() public view returns (uint256) {
        return address(this).balance;
    }

    function sendAmount() public payable {
        _balances[msg.sender] = _balances[msg.sender].add(msg.value);
    }

    function transfer(uint256 _amount, address payable _to) public {
        require(_amount <= _balances[msg.sender]);
        _balances[msg.sender] = _balances[msg.sender].sub(_amount);
        _to.transfer(_amount);
    }

    function transferFrom(
        address _from,
        address payable _to,
        uint256 _amount
    ) public onlyOwner {
        require(_amount <= _balances[_from]);
        _balances[_from] = _balances[_from].sub(_amount);
        _to.transfer(_amount);
    }

    function renounceOwnership() public virtual override onlyOwner {
        revert("no no ...");
    }
}
