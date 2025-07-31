def log_reasoning_to_graph(query, steps, answer):
    from neo4j import GraphDatabase

    driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
    with driver.session() as session:
        def write_tx(tx):
            tx.run("MERGE (q:Query {text: $query})", query=query)
            last = "q"
            for i, step in enumerate(steps):
                label = f"s{i}"
                tx.run(f"MERGE ({label}:Step {{text: $step}})", step=step)
                tx.run(f"MATCH (a),(b) WHERE a.text = $a_text AND b.text = $b_text CREATE (a)-[:LEADS_TO]->(b)", a_text=query if i == 0 else steps[i - 1], b_text=step)
            tx.run("MERGE (a:Answer {text: $answer})", answer=answer)
            tx.run("MATCH (last:Step {text: $last_step}), (a:Answer {text: $answer}) CREATE (last)-[:LEADS_TO]->(a)", last_step=steps[-1], answer=answer)
        session.write_transaction(write_tx)
    driver.close()
