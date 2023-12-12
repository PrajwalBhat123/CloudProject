from flask import Flask
from flask_pymongo import PyMongo
from flask_pymongo import MongoClient
import os
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY", "default_secret_key")
app.config["debug"]=True
app.config["MONGO_URI"] = "mongodb+srv://mdsuraj2002:surajmd28@cluster0.tlnduoq.mongodb.net/"
print("app")
# mongodb database


mongo_uri = "mongodb+srv://mdsuraj2002:surajmd28@cluster0.tlnduoq.mongodb.net/your_database_name"
client = MongoClient(mongo_uri)
db = client.get_database()
print(db.get_collection)
mongodb_client = PyMongo(app)
#db = mongodb_client.db
print(db.get_collection)
from application import routes

