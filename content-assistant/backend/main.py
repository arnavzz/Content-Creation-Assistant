from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from groq_api import generate_content

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
async def generate_content(request: PromptRequest):
    try:
        result = generate_content(request.prompt)
        return
    except Exception as e:
        raise HTTPException(status_code=500, detail = str(e)) 
    
