import os
from dotenv import load_dotenv
from pinecone import Pinecone

# Load environment variables from .env
load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")  # e.g., "gcp-starter"
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")  # Your Pinecone index name
MONGO_URI = os.getenv("MONGO_URI")

# Initialize Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY)
