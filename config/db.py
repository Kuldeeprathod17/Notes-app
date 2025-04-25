from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get MongoDB URI from environment variable
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://kuldeep:kuldeep_1710@cluster0.x5quxjp.mongodb.net/Notes")

# Create a connection pool
client = MongoClient(MONGO_URI, server_api=ServerApi('1'), maxPoolSize=50)
conn = client