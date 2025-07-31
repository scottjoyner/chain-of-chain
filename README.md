# ThoughtChain: Blockchain-Backed Chain-of-Thought Reasoning for AI Agents

This repository implements an architecture for decentralized, auditable AI reasoning steps (Chain-of-Thought or CoT) stored on a blockchain. Each thought is hashed, signed, and submitted as a transaction, forming a verifiable, graph-structured memory that LLMs can query.

---

## 📐 Architecture Overview

* AI agents generate reasoning steps (thoughts).
* Thoughts are signed and submitted to the blockchain.
* Thoughts are stored as a DAG (dependencies = graph edges).
* IPFS is used for storing large payloads off-chain.
* Optional zkProof support for future privacy guarantees.

---

## 🔧 Project Structure

```
project-root/
├── contracts/
│   └── ThoughtChainV2.sol         # Solidity contract with IPFS + zkProof support
├── scripts/
│   └── deploy.js                  # Hardhat deployment script
├── hardhat.config.js             # Local/testnet deployment config
├── README.md
└── package.json
```

---

## 🚀 Deploying to a Blockchain

### 1. Install Hardhat and initialize

```bash
npm install --save-dev hardhat
npx hardhat
```

Choose "Create a basic sample project".

### 2. Compile the contract

```bash
npx hardhat compile
```

### 3. Run a local Ethereum node (optional)

```bash
npx hardhat node
```

### 4. Deploy to Localhost

```bash
npx hardhat run scripts/deploy.js --network localhost
```

### 5. Deploy to Sepolia (or other testnet)

```bash
npx hardhat run scripts/deploy.js --network sepolia
```

Make sure you update `hardhat.config.js` with your Infura or Alchemy API key and private key:

```js
sepolia: {
  url: "https://sepolia.infura.io/v3/YOUR_INFURA_KEY",
  accounts: ["0xYOUR_PRIVATE_KEY"]
}
```

---

## 🧠 Submitting a Thought via Python (web3.py)

```python
from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

with open('ThoughtChainV2.abi.json') as f:
    abi = json.load(f)

contract = w3.eth.contract(address="0xDeployedAddress", abi=abi)
account = w3.eth.accounts[0]

thought = {
    "hash": "hash123",
    "agentId": "LLM_001",
    "input": "...",
    "reasoning": "...",
    "output": "...",
    "dependencies": ["hashA", "hashB"],
    "signature": "...",
    "ipfsHash": "ipfs://Qm..."
}

tx = contract.functions.submitThought(
    thought["hash"], thought["agentId"], thought["input"], thought["reasoning"],
    thought["output"], thought["dependencies"], thought["signature"],
    thought["ipfsHash"], bytes()  # zkProof placeholder
).build_transaction({
    "from": account,
    "nonce": w3.eth.get_transaction_count(account),
    "gas": 3000000,
    "gasPrice": w3.to_wei("20", "gwei")
})
```

---

## 🧪 Coming Soon

* zkProof integration (e.g., using ZoKrates or SnarkJS)
* IPFS pinning via Web3.Storage
* Frontend DApp UI (MetaMask + vis.js)
* Neo4j or JSON graph exports

---

## 🧾 License

MIT License

## 🤝 Contributions

PRs welcome for:

* Blockchain integrations (Kadena, IOTA, Radix)
* Optimized graph traversal
* Multi-agent consensus schemas

---

For more: contact Scott Joyner or contribute on GitHub.
