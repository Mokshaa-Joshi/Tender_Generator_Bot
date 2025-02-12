import openai
from config import pc, PINECONE_INDEX_NAME, OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY
index = pc.Index(PINECONE_INDEX_NAME)

def get_embedding(text):
    response = openai.Embedding.create(input=[text], model="text-embedding-ada-002")
    return response["data"][0]["embedding"]

def search_similar_tenders(query, top_k=5):
    query_vector = get_embedding(query)
    results = index.query(vector=query_vector, top_k=top_k, include_metadata=True)
    return [match["metadata"]["text"] for match in results["matches"]]

# Example usage:
# print(search_similar_tenders("construction project"))
