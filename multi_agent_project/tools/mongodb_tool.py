from crewai.tools import BaseTool


from db.mongo_client import clients_col, orders_col, payments_col, courses_col, classes_col
from bson.objectid import ObjectId

class MongoDBTool(BaseTool):
    name: str = "MongoDBTool"
    description: str = "Use this tool to query clients, orders, payments, courses, and classes"

    def _run(self, query: str):
        if "client" in query and "email" in query:
            email = query.split("email")[-1].strip()
            return clients_col.find_one({"email": email})
        if "orders for client" in query:
            name = query.split("client")[-1].strip()
            client = clients_col.find_one({"name": name})
            return list(orders_col.find({"client_id": client["_id"]})) if client else "Client not found"

        return "MongoDBTool could not process the query"


