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


@app.get("/companies")
def get_companies():
    return {
        "companies": ["Google", "Microsoft", "Amazon"]
    }


@app.get("/companies/{company_name}")
def get_company(company_name: str):
    return {
        "company": company_name,
        "message": "Company found"
    }