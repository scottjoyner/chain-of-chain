from web3 import Web3
import json

# Connect to local node or testnet
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))  # Or use Infura, Alchemy etc.

# Load compiled contract ABI
with open('ThoughtChainV2.abi.json') as f:
    abi = json.load(f)

contract_address = Web3.to_checksum_address("0xYourDeployedContractAddress")
contract = w3.eth.contract(address=contract_address, abi=abi)

account = w3.eth.accounts[0]

# Submit a new thought
def submit_thought(thought: dict):
    tx = contract.functions.submitThought(
        thought["hash"],
        thought["agentId"],
        thought["input"],
        thought["reasoning"],
        thought["output"],
        thought["dependencies"],
        thought["signature"],
        thought["ipfsHash"],
        bytes()  # zkProof placeholder
    ).build_transaction({
        "from": account,
        "nonce": w3.eth.get_transaction_count(account),
        "gas": 3000000,
        "gasPrice": w3.to_wei("20", "gwei")
    })

    signed_tx = w3.eth.account.sign_transaction(tx, private_key="0xYourPrivateKey")
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Thought stored in TX:", receipt.transactionHash.hex())
