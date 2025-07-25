from fastapi import FastAPI

app = FastAPI(title="PRAI", description="A basic FastAPI application", version="0.1.0")


@app.get("/")
async def read_root():
    """Root endpoint that returns a welcome message."""
    return {"message": "Hello from PRAI!"}


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    """Get an item by ID with optional query parameter."""
    return {"item_id": item_id, "q": q}
