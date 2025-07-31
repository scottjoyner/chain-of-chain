def retrieve_from_graph(query_keywords):
    from neo4j import GraphDatabase
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
    with driver.session() as session:
        def fetch(tx):
            result = tx.run("""
                MATCH (q:Query)-[:LEADS_TO*]->(a:Answer)
                WHERE q.text CONTAINS $kw
                RETURN q.text AS query, a.text AS answer LIMIT 5
            """, kw=query_keywords)
            return result.data()
        output = session.read_transaction(fetch)
    driver.close()
    return output
