from neo4j import GraphDatabase

class neo4jApp:
	def __init__(self, uri, user, password):
		self.driver = GraphDatabase.driver(uri, auth=(user, password))

	def close(self):
		self.driver.close()

	def query(self, query, db=None):
		session = self.driver.session(database=db) if db is not None else self.driver.session()
		response = list(session.run(query))
		return response

if __name__ == "__main__":
	app = neo4jApp("bolt://34.117.227.3:7687", "neo4j", "s3cr3t")
	app.query("CREATE (n:Persona {nombre: 'Ane', apellido: 'García'})")

	app.query("CREATE (n:Persona {nombre: 'Kubernetes', apellido: 'Kubernetes'})")

	app.query("MATCH (a:Persona), (b:Persona) WHERE a.nombre = 'Ane' AND b.nombre = 'Kubernetes' CREATE (a)-[r:Odia]->(b) RETURN type(r)")
	app.close()
