from pymongo import MongoClient


client = MongoClient("mongodb+srv://imatik:atik1234@cluster0.qclfrmt.mongodb.net/?appName=Cluster0")

db = client.todo_db

collection_name = db["todos_collection"]