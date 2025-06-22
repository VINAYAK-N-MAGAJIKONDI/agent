from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime, timedelta

uri = "mongodb+srv://vinayak:8BVKwdb2sT4dlqqG@cluster0.ww5e8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'), tls=True, tlsAllowInvalidCertificates=True)



try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["qest"] 




required_collections = ["clients", "orders", "payments", "courses", "classes", "attendance"]
existing_collections = db.list_collection_names()

for collection in required_collections:
    if collection not in existing_collections:
        db.create_collection(collection)
        print(f"Created collection: {collection}")

clients_col = db["clients"]
orders_col = db["orders"]
payments_col = db["payments"]
courses_col = db["courses"]
classes_col = db["classes"]
attendance_col = db["attendance"]

# Insert sample data if collections are empty
if clients_col.count_documents({}) == 0:
    client_id = clients_col.insert_one({
        "name": "Priya Sharma",
        "email": "priya@example.com",
        "phone": "9876543210",
        "status": "inactive",
        "joined_date": datetime.utcnow() - timedelta(days=40)
    }).inserted_id
    client2_id = clients_col.insert_one({
        "name": "Amit Verma",
        "email": "amit@example.com",
        "phone": "9123456789",
        "status": "active",
        "joined_date": datetime.utcnow() - timedelta(days=10)
    }).inserted_id
else:
    client_doc = clients_col.find_one({})
    client_id = client_doc["_id"] if client_doc else None
    client2_id = client_id

if courses_col.count_documents({}) == 0:
    course_id = courses_col.insert_one({
        "title": "Yoga Beginner",
        "instructor": "Anjali Mehta",
        "status": "active"
    }).inserted_id
    course2_id = courses_col.insert_one({
        "title": "Pilates Pro",
        "instructor": "Rohit Singh",
        "status": "active"
    }).inserted_id
else:
    course_doc = courses_col.find_one({})
    course_id = course_doc["_id"] if course_doc else None
    course2_id = course_id

if classes_col.count_documents({}) == 0:
    today = datetime.utcnow()
    classes_col.insert_many([
        {
            "course_id": course_id,
            "title": "Yoga Session 1",
            "start_date": today,
            "instructor": "Anjali Mehta",
            "status": "scheduled"
        },
        {
            "course_id": course2_id,
            "title": "Pilates Session 1",
            "start_date": today + timedelta(days=1),
            "instructor": "Rohit Singh",
            "status": "scheduled"
        }
    ])

if orders_col.count_documents({}) == 0:
    order_id = orders_col.insert_one({
        "client_id": client_id,
        "course_id": course_id,
        "status": "pending"
    }).inserted_id
    order2_id = orders_col.insert_one({
        "client_id": client2_id,
        "course_id": course2_id,
        "status": "completed"
    }).inserted_id
else:
    order_doc = orders_col.find_one({})
    order_id = order_doc["_id"] if order_doc else None
    order2_id = order_id

if payments_col.count_documents({}) == 0:
    payments_col.insert_one({
        "order_id": order_id,
        "amount_paid": 1000,
        "due_amount": 0,
        "payment_date": datetime.utcnow() - timedelta(days=5)
    })
    payments_col.insert_one({
        "order_id": order2_id,
        "amount_paid": 2000,
        "due_amount": 500,
        "payment_date": datetime.utcnow() - timedelta(days=2)
    })

if attendance_col.count_documents({}) == 0:
    attendance_col.insert_one({
        "course_id": course_id,
        "class_title": "Yoga Session 1",
        "client_id": client_id,
        "present": True
    })
    attendance_col.insert_one({
        "course_id": course2_id,
        "class_title": "Pilates Session 1",
        "client_id": client2_id,
        "present": False
    })



