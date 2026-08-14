from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to LeetCode Company Tracker API 🚀"
    }

@app.get("/health")
def health():
    return {
        "status": "Backend is running"
    }