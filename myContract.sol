// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/// @title MyToken - A basic ERC20 Token with burn functionality
contract MyToken {
    // Token name
    string public name = "JavadToken";

    // Token symbol
    string public symbol = "JTK";

    // Number of decimals (e.g., 9 means balances are stored as whole numbers * 10^9)
    uint8 public decimals = 9;

    // Total supply of tokens (in smallest units, i.e., multiplied by 10^decimals)
    uint256 public totalSupply;

    // Mapping of account addresses to their balances
    mapping(address => uint256) public balanceOf;

    // Mapping of allowances: owner => (spender => amount)
    mapping(address => mapping(address => uint256)) public allowance;

    // Event emitted on successful transfer
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Event emitted on approval of allowance
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Event emitted when tokens are burned
    event Burn(address indexed burner, uint256 value);

    /// @notice Constructor sets the initial total supply and assigns it to the deployer
    constructor() {
        // Set total supply to 1,000,000 tokens (with decimals considered)
        totalSupply = 1_000_000 * (10 ** uint256(decimals));

        // Assign all tokens to the deployer (contract creator)
        balanceOf[msg.sender] = totalSupply;

        // Emit a transfer event from address(0) to indicate minting
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /// @notice Transfer tokens from the caller to another address
    /// @param _to The recipient address
    /// @param _value The amount of tokens to transfer
    /// @return success True if the transfer was successful
    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");
        _transfer(msg.sender, _to, _value);
        return true;
    }

    /// @notice Internal transfer function
    /// @param _from The sender address
    /// @param _to The recipient address
    /// @param _value The amount of tokens to transfer
    function _transfer(address _from, address _to, uint256 _value) internal {
        require(_to != address(0), "Invalid recipient address");

        // Subtract from sender
        balanceOf[_from] -= _value;

        // Add to recipient
        balanceOf[_to] += _value;

        // Emit transfer event
        emit Transfer(_from, _to, _value);
    }

    /// @notice Approve another address to spend tokens on behalf of the caller
    /// @param _spender The address allowed to spend
    /// @param _value The amount allowed
    /// @return success True if approval was successful
    function approve(address _spender, uint256 _value) public returns (bool success) {
        allowance[msg.sender][_spender] = _value;

        // Emit approval event
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /// @notice Transfer tokens from one address to another, using allowance
    /// @param _from The address to send tokens from
    /// @param _to The address to receive tokens
    /// @param _value The amount of tokens to transfer
    /// @return success True if the transfer was successful
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");

        // Deduct from allowance
        allowance[_from][msg.sender] -= _value;

        // Perform the transfer
        _transfer(_from, _to, _value);
        return true;
    }

    /// @notice Burn (destroy) tokens from sender's account
    /// @param _value The amount of tokens to burn
    /// @return success True if tokens were successfully burned
    function burn(uint256 _value) public returns (bool success) {
        require(balanceOf[msg.sender] >= _value, "Insufficient balance to burn");

        // Subtract tokens from sender's balance
        balanceOf[msg.sender] -= _value;

        // Decrease total supply
        totalSupply -= _value;

        // Emit burn and transfer events
        emit Burn(msg.sender, _value);
        emit Transfer(msg.sender, address(0), _value);
        return true;
    }
}