from neo4j import GraphDatabase
import sys

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
	app = neo4jApp("bolt://34.88.11.228:7687", "neo4j", "s3cr3t")
	nombre1 = sys.argv[1]
	apellido1 = sys.argv[2]
	app.query("CREATE (n:Persona {nombre: '"+nombre1+"', apellido: '"+apellido1+"'})")

	nombre2 = sys.argv[3]
	apellido2 = sys.argv[4]
	app.query("CREATE (n:Persona {nombre: '"+nombre2+"', apellido: '"+apellido2+"'})")

	app.query("MATCH (a:Persona), (b:Persona) WHERE a.nombre = '"+nombre1+"' AND b.nombre = '"+nombre2+"' CREATE (a)-[r:Enamorada]->(b) RETURN type(r)")
	app.close()
