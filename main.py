
from fastapi import FastAPI

app = FastAPI()

# Addition function
def addition(a: float, b: float):
    return a + b

# API endpoint
@app.get("/")
def home():
    return {"message": "Addition API is running"}

@app.get("/add")
def add_numbers(a: float, b: float):
    result = addition(a, b)

    return {
        "Number 1": a,
        "Number 2": b,
        "Addition": result
    }
