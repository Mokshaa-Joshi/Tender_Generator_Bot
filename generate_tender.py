import openai
from config import OPENAI_API_KEY
from vector_search import search_similar_tenders

openai_client = openai.OpenAI(api_key=OPENAI_API_KEY)

def generate_tender(query):
    chunks = search_similar_tenders(query)
    prompt = f"Generate a professional tender proposal based on these points:\n{''.join(chunks)}"

    response = openai_client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an expert in writing tenders."},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
