from fastapi import FastAPI
app=FastAPI(title="SmartBank AI")
@app.get("/health")
def health_check():
    return{"state":"healthy",
           "service": "SmartBank-AI"}