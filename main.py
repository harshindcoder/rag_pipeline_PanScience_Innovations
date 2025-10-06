from fastapi import FastAPI, UploadFile, Form
from utils.pdf_parser import parse_pdf
from utils.vectorstore import add_to_chroma, query_chroma

from pymongo import MongoClient
import requests
import os

app = FastAPI()

#MongoDB setup
#mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_client = MongoClient("mongodb://mongo:27017/")
db = mongo_client["rag_db"]
collection = db["pdf_metadata"]

from bson import ObjectId
#Upload and parse document
@app.post("/upload")
async def upload_pdf(file: UploadFile):
    os.makedirs("data/uploads", exist_ok=True)
    file_path = f"data/uploads/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())
    
    # Parse PDF
    text, metadata = parse_pdf(file_path)
    
    # Add to Chroma
    add_to_chroma(file.filename, text)
    
    # Insert into MongoDB and convert ObjectId to string
    doc_id = collection.insert_one(metadata).inserted_id
    metadata["_id"] = str(doc_id)

    return {"status": "success", "metadata": metadata}

@app.post("/ask")
async def ask_question(question: str = Form(...)):
    results = query_chroma(question)
    context = results["documents"][0] if results["documents"] else ""

    #Query local Ollama Mistral model

    payload = {
        "model" : "mistral",
        "prompt" : f"Answer the question based on context:\n\nContext:{context}\n\nQuestion:{question}"
    }

    response = requests.post("http://host.docker.internal:11434/api/generate",json=payload,stream = True)
    #response = requests.post("http://ollama:11434/api/generate", json=payload, stream=True)
    answer = ""
    for line in response.iter_lines():
        if line:
            chunk = line.decode("utf-8")
            if '"response":' in chunk:
                answer += chunk.split('"response":')[1].split(",")[0].split("\"")[1]
    
    return {"question":question, "answer":answer}
