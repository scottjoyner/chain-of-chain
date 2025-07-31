// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract ThoughtChainV2 {
    struct Thought {
        string agentId;
        string input;
        string reasoning;
        string output;
        string[] dependencies;
        uint256 timestamp;
        string signature;
        string ipfsHash;       // NEW: Points to off-chain payload
        bytes zkProof;         // NEW: Optional zkSNARK proof (stub only)
    }

    mapping(string => Thought) private thoughts;  // hash → Thought
    mapping(string => bool) public exists;
    string[] private allHashes;

    event ThoughtSubmitted(string indexed hash, string agentId, string ipfsHash, uint256 timestamp);

    /// Submit a new thought step with optional IPFS CID + zkProof
    function submitThought(
        string memory hash,
        string memory agentId,
        string memory input,
        string memory reasoning,
        string memory output,
        string[] memory dependencies,
        string memory signature,
        string memory ipfsHash,
        bytes memory zkProof
    ) public {
        require(!exists[hash], "Thought already exists");

        // OPTIONAL: Verify zkProof here in future
        // bool valid = verifyProof(zkProof);
        // require(valid, "Invalid zk proof");

        thoughts[hash] = Thought({
            agentId: agentId,
            input: input,
            reasoning: reasoning,
            output: output,
            dependencies: dependencies,
            timestamp: block.timestamp,
            signature: signature,
            ipfsHash: ipfsHash,
            zkProof: zkProof
        });

        exists[hash] = true;
        allHashes.push(hash);
        emit ThoughtSubmitted(hash, agentId, ipfsHash, block.timestamp);
    }

    function getThought(string memory hash) public view returns (
        string memory agentId,
        string memory input,
        string memory reasoning,
        string memory output,
        string[] memory dependencies,
        uint256 timestamp,
        string memory signature,
        string memory ipfsHash,
        bytes memory zkProof
    ) {
        require(exists[hash], "Thought not found");
        Thought storage t = thoughts[hash];
        return (
            t.agentId,
            t.input,
            t.reasoning,
            t.output,
            t.dependencies,
            t.timestamp,
            t.signature,
            t.ipfsHash,
            t.zkProof
        );
    }

    function getAllThoughtHashes() public view returns (string[] memory) {
        return allHashes;
    }

    function getThoughtCount() public view returns (uint256) {
        return allHashes.length;
    }
}
