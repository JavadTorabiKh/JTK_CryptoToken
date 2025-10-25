// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/// @title JavadToken - Advanced ERC20 Token with burn, mint, and security features
/// @author Javad Torabi
contract JavadToken is ReentrancyGuard {
    string public constant name = "JavadToken";
    string public constant symbol = "JTK";
    uint8 public constant decimals = 9;
    
    uint256 public totalSupply;
    address public owner;
    
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;
    mapping(address => bool) public isMinter;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Burn(address indexed burner, uint256 value);
    event Mint(address indexed minter, address indexed to, uint256 value);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this");
        _;
    }

    modifier onlyMinter() {
        require(isMinter[msg.sender] || msg.sender == owner, "Not authorized to mint");
        _;
    }

    constructor() {
        owner = msg.sender;
        totalSupply = 1_000_000 * (10 ** uint256(decimals));
        balanceOf[msg.sender] = totalSupply;
        isMinter[msg.sender] = true;
        
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    function transfer(address _to, uint256 _value) 
        external 
        nonReentrant 
        returns (bool) 
    {
        require(_to != address(0), "Invalid recipient");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");
        
        _transfer(msg.sender, _to, _value);
        return true;
    }

    function _transfer(address _from, address _to, uint256 _value) internal {
        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(_from, _to, _value);
    }

    function approve(address _spender, uint256 _value) 
        external 
        returns (bool) 
    {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    function transferFrom(address _from, address _to, uint256 _value) 
        external 
        nonReentrant 
        returns (bool) 
    {
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");

        allowance[_from][msg.sender] -= _value;
        _transfer(_from, _to, _value);
        return true;
    }

    function burn(uint256 _value) 
        external 
        nonReentrant 
        returns (bool) 
    {
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");
        
        balanceOf[msg.sender] -= _value;
        totalSupply -= _value;
        
        emit Burn(msg.sender, _value);
        emit Transfer(msg.sender, address(0), _value);
        return true;
    }

    function mint(address _to, uint256 _value) 
        external 
        onlyMinter 
        nonReentrant 
        returns (bool) 
    {
        require(_to != address(0), "Invalid recipient");
        
        balanceOf[_to] += _value;
        totalSupply += _value;
        
        emit Mint(msg.sender, _to, _value);
        emit Transfer(address(0), _to, _value);
        return true;
    }

    function addMinter(address _minter) external onlyOwner {
        isMinter[_minter] = true;
    }

    function removeMinter(address _minter) external onlyOwner {
        isMinter[_minter] = false;
    }

    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid new owner");
        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }
}