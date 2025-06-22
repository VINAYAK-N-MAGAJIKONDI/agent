from crewai.tools import BaseTool
from db.mongo_client import clients_col, courses_col, orders_col

class ExternalAPITool(BaseTool):
    name: str = "ExternalAPI"
    description: str = "Use this to create clients or orders"

    def _run(self, action: str):
        if "create order for" in action:
            parts = action.split("for")[-1].strip().split("client")
            course = parts[0].strip()
            client = parts[1].strip()
            c_doc = clients_col.find_one({"name": client})
            s_doc = courses_col.find_one({"title": course})
            if not c_doc or not s_doc:
                return "Client or course not found"
            orders_col.insert_one({
                "client_id": c_doc["_id"],
                "course_id": s_doc["_id"],
                "status": "pending"
            })
            return "Order created"
        return "ExternalAPI Tool could not perform the action"
