import openai
from config import pc, PINECONE_INDEX_NAME, OPENAI_API_KEY
from mongodb import fetch_tender_chunks

openai.api_key = OPENAI_API_KEY

# Create Pinecone index if not exists
if PINECONE_INDEX_NAME not in pc.list_indexes():
    pc.create_index(name=PINECONE_INDEX_NAME, dimension=1536, metric="cosine")

index = pc.Index(PINECONE_INDEX_NAME)

def get_embedding(text):
    response = openai.Embedding.create(input=[text], model="text-embedding-ada-002")
    return response["data"][0]["embedding"]

def store_vectors():
    tenders = fetch_tender_chunks()
    
    for i, tender in enumerate(tenders):
        vector = get_embedding(tender)
        index.upsert([(str(i), vector, {"text": tender})])

    print("✅ Tender chunks stored in Pinecone.")

# Run this script once to push tender data to Pinecone
store_vectors()
