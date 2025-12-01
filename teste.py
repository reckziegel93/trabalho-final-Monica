from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "12345678"))
driver.verify_connectivity()

def buscar_pessoas(tx):
    resultado = tx.run("MATCH (p:Pessoa) RETURN p.nome AS nome")
    return [record["nome"] for record in resultado]

with driver.session(database="neo4j") as session:
    nomes = session.execute_read(buscar_pessoas)
    for nome in nomes:
        print(nome)

driver.close()
