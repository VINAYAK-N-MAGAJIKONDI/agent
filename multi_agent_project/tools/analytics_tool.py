from crewai.tools import BaseTool
from db.mongo_client import clients_col, payments_col, orders_col, attendance_col, courses_col
from datetime import datetime, timedelta

class DashboardAnalyticsTool(BaseTool):
    name: str = "DashboardAnalyticsTool"
    description: str = "Get revenue, client insights, top courses, and attendance reports."

    def _run(self, prompt: str):
        prompt = prompt.lower()

        if "revenue" in prompt:
            now = datetime.now()
            start = datetime(now.year, now.month, 1)
            payments = payments_col.find({"payment_date": {"$gte": start}})
            return sum(p.get("amount_paid", 0) for p in payments)

        if "outstanding" in prompt and "payment" in prompt:
            payments = payments_col.find({"due_amount": {"$gt": 0}})
            return sum(p.get("due_amount", 0) for p in payments)

        if "inactive client" in prompt:
            one_month_ago = datetime.utcnow() - timedelta(days=30)
            return clients_col.count_documents({"joined_date": {"$lt": one_month_ago}, "status": "inactive"})

        if "new client" in prompt:
            now = datetime.utcnow()
            start = datetime(now.year, now.month, 1)
            return clients_col.count_documents({"joined_date": {"$gte": start}})

        if "top course" in prompt:
            pipeline = [
                {"$group": {"_id": "$course_id", "count": {"$sum": 1}}},
                {"$sort": {"count": -1}},
                {"$limit": 3}
            ]
            top = list(orders_col.aggregate(pipeline))
            titles = []
            for c in top:
                course_doc = courses_col.find_one({"_id": c["_id"]})
                if course_doc and "title" in course_doc:
                    titles.append(course_doc["title"])
            return titles

        if "attendance" in prompt:
            course = prompt.split("for")[-1].strip() if "for" in prompt else ""
            course_doc = courses_col.find_one({"title": {"$regex": course, "$options": "i"}}) if course else None
            if not course_doc:
                return "Course not found"
            total = attendance_col.count_documents({"course_id": course_doc["_id"]})
            present = attendance_col.count_documents({"course_id": course_doc["_id"], "present": True})
            if total == 0:
                return "No attendance data"
            return f"{(present / total) * 100:.2f}% attendance for {course}"

        return "DashboardAnalyticsTool could not understand the prompt."
