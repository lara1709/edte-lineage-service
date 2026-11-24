from fastapi import FastAPI

app = FastAPI(
    title="EDTE Lineage Service",
    description="API for managing data lineage and URNs",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "EDTE Lineage Service is running"}