from fastapi import FastAPI
from pydantic import BaseModel

from ai_service import review_code

app = FastAPI(title="AI Code Reviewer Backend")


class CodeRequest(BaseModel):
    code: str


@app.get("/")
def home():
    return {"status": "Backend server is running successfully!"}


@app.post("/review")
def process_code_review(request: CodeRequest):
    review_result = review_code(request.code)
    return {"review": review_result}