from fastapi import FastAPI
from app.api import analyzer

app = FastAPI(
    title="GitHub Repository Analyzer",
    description="Analyze GitHub repositories with detailed insights",
    version="1.0.0"
)

# Include the analyzer router
app.include_router(analyzer.router, prefix="/api", tags=["analyzer"])

@app.get("/")
def read_root():
    return {
        "message": "GitHub Analyzer API is running!",
        "docs": "/docs"
    }