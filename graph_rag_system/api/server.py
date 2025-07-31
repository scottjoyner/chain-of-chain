from fastapi import FastAPI, Request
from pydantic import BaseModel
from app import main as query_pipeline

app = FastAPI()

class QueryInput(BaseModel):
    query: str

@app.post("/query")
async def process_query(input: QueryInput):
    response = query_pipeline(input.query)
    return {"answer": response}
