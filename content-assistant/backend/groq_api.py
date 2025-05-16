import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY =  os.getenv("GROQ_API_KEY")
MODEL =  "llama3-70b-8192"
HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

def generate_content(prompt: str) -> str:
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful AI content assistant that specializes in writing and editing. Your goal is to assist content creators by generating, refining, and optimizing various content types, including blog posts, social media captions, email newsletters, and video scripts. Ensure the content aligns with the specified tone, audience, and SEO best practices."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    response = requests.post(headers=HEADERS, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Groq API Error: {response.status_code} - {response.text}")
