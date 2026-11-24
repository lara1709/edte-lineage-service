from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.lineage_service import process_urn
from app.neo4j_client import create_driver

app = FastAPI(
    title="EDTE Lineage Service",
    description="API for managing data lineage and URNs",
    version="1.0.0"
)

class URNRequest(BaseModel):
    urn: str

@app.get("/")
def root():
    return {"message": "EDTE Lineage Service is running"}

@app.post("/urns")
def create_urn(request: URNRequest):
    driver = create_driver()

    try:
        canonical_urn = process_urn(driver, request.urn)

        return {
            "message": "URN successfully stored",
            "canonical_urn": canonical_urn
        }

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    finally:
        driver.close()
