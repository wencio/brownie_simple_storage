
//SPDX-License-Identifier:MIT
pragma solidity ^0.6.0;

contract  SimpleStorage {

// this will get initialized to 0!

    uint256  favoriteNumber;


    struct People {
        uint256 favoriteNumber;
        string name;
    }

    People [] public people;
    mapping(string => uint256) public nameToFavoriteNumber;

    function store (uint256 _favoriteNumber) public {
        favoriteNumber = _favoriteNumber;
    }
    
    // pure and view functions are blue, they do not change the state of the Blockchain - only read not write on the Blockchain
    // pure functions do a math calculation  
 function retrieve() public view returns(uint256){
     return favoriteNumber;
 }

// memory means thah only se mantiene during the function execution - storage persist afert function execution 
function addPerson( uint256 _favoriteNumber,string memory _name) public {
    people.push(People(_favoriteNumber,_name));
    nameToFavoriteNumber[_name] = _favoriteNumber;
}
}