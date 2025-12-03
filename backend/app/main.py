from fastapi import FastAPI

app = FastAPI(title="AI ATS API", version="0.1.0")

@app.get("/")
async def root():
    return {"message": "AI ATS Backend is running"}

@app.get("/health")
async def health():
    return {"status": "ok"}
