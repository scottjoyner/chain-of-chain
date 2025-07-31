from graph.cot_logger import log_reasoning_to_graph

examples = [
    {
        "query": "What is the company growth rate?",
        "steps": ["Check last year revenue", "Check current revenue", "Compute % increase"],
        "answer": "The growth rate is 15%."
    },
    {
        "query": "How to onboard a new engineer?",
        "steps": ["Retrieve HR policy", "Assign mentor", "Provision tools"],
        "answer": "Follow the 3-step onboarding protocol."
    }
]

for item in examples:
    log_reasoning_to_graph(item["query"], item["steps"], item["answer"])
    print(f"Inserted: {item['query']}")
