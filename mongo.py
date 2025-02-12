from pymongo import MongoClient
from config import MONGO_URI

def get_mongo_connection():
    client = MongoClient(MONGO_URI)
    return client["GMDC_RFPs"]

def fetch_tender_chunks():
    db = get_mongo_connection()
    collection = db["tender_chunks"]
    results = collection.find()
    return [doc["content"] for doc in results]
