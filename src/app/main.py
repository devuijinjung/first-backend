from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title=os.getenv("APP_NAME", "first-backend"))

@app.get("/")
def root():
    return {"message": "hello backend", "env": os.getenv("ENV", "dev")}

@app.get("/health")
def health():
    return {"status": "ok"}
