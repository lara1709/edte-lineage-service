from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="EDTE Lineage Service",
    description="API for managing data lineage and URNs",
    version="1.0.0"
)

class URNRequests(BaseModel):
    urn: str

@app.get("/")
def root():
    return {"message": "EDTE Lineage Service is running"}