import requests
from typing import List, Dict, Set

CHAIN_RPC = "http://localhost:8545"  # Replace with your actual RPC
CONTRACT_ADDRESS = "0x123..."        # Replace with actual contract address

# Simulated chain query function
def fetch_thought(hash: str) -> Dict:
    """Query the blockchain for a thought by its hash."""
    response = requests.post(CHAIN_RPC, json={
        "jsonrpc": "2.0",
        "method": "eth_call",
        "params": [{
            "to": CONTRACT_ADDRESS,
            "data": "0x..."  # ABI-encoded call to `getThought(hash)`
        }, "latest"],
        "id": 1
    })
    # In practice you'd decode the returned data using web3.py or similar
    return {
        "hash": hash,
        "agentId": "LLM_001",
        "input": "...",
        "reasoning": "...",
        "output": "...",
        "dependencies": ["hashA", "hashB"],
        "timestamp": 12345678,
        "signature": "..."
    }

# DFS-style traversal
def traverse_dependencies(start_hash: str, visited: Set[str] = None) -> Dict[str, Dict]:
    if visited is None:
        visited = set()
    thought_graph = {}

    def dfs(current_hash):
        if current_hash in visited:
            return
        visited.add(current_hash)

        thought = fetch_thought(current_hash)
        thought_graph[current_hash] = thought

        for dep_hash in thought.get("dependencies", []):
            dfs(dep_hash)

    dfs(start_hash)
    return thought_graph

# Optional JSON graph builder
def build_graph_json(root_hash: str) -> Dict:
    graph = traverse_dependencies(root_hash)
    nodes = []
    edges = []

    for hash, data in graph.items():
        nodes.append({"id": hash, "label": data["reasoning"]})
        for dep in data.get("dependencies", []):
            edges.append({"from": dep, "to": hash})

    return {"nodes": nodes, "edges": edges}
