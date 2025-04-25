from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get MongoDB URI from environment variable


MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://localhost:27017/")

# Create MongoDB client with SSL configuration
client = MongoClient(
    MONGO_URI,
    server_api=ServerApi('1'),
    maxPoolSize=50,
    ssl=True,
    tlsAllowInvalidCertificates=True  # This is for development only
)

# Get database
db = client.Notes

# Get collection
conn = db.notes