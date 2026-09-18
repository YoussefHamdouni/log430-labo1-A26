"""
User DAO (MongoDB)
"""
import os
from dotenv import load_dotenv
import pymongo
from bson.objectid import ObjectId
from models.user import User

class UserDAOMongo:
    def __init__(self):
        try:
            env_path = ".env"
            load_dotenv(dotenv_path=env_path)
            
            db_host = os.getenv("MONGODB_HOST")
            db_user = os.getenv("DB_USERNAME") 
            db_pass = os.getenv("DB_PASSWORD")
            mongo_uri = f"mongodb://{db_user}:{db_pass}@{db_host}:27017/"
            self.client = pymongo.MongoClient(mongo_uri)
            
            self.db = self.client["labo1"] 
            self.collection = self.db["users"]
        except Exception as e:
            print("Erreur MongoDB : " + str(e))

    def select_all(self):
        """ Select all users from MongoDB """
        users = []
        for doc in self.collection.find():
            users.append(User(str(doc["_id"]), doc["name"], doc["email"]))
        return users

    def insert(self, user):
        """ Insert given user into MongoDB """
        result = self.collection.insert_one({
            "name": user.name, 
            "email": user.email
        })
        return str(result.inserted_id)

    def update(self, user):
        """ Update an existing user in MongoDB """
        self.collection.update_one(
            {"_id": ObjectId(user.id)},
            {"$set": {"name": user.name, "email": user.email}}
        )

    def delete(self, user_id):
        """ Delete user from MongoDB with given user ID """
        self.collection.delete_one({"_id": ObjectId(user_id)})

    def delete_all(self): 
        """ Empty users collection in MongoDB """
        self.collection.delete_many({})
        
    def close(self):
        self.client.close()
