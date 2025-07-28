import logging
from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from prai.routers.api.github.users import router as github_users_router

logging.basicConfig(level=logging.DEBUG)

app = FastAPI(title="PRAI", description="A basic FastAPI application", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development; adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get the static directory path
static_dir = Path(__file__).parent / "static"


# Define API routes first
@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


# Include the GitHub API router
app.include_router(github_users_router)


# Mount static files (this needs to be after API routes but before catch-all)
if static_dir.exists():
    app.mount("/assets", StaticFiles(directory=static_dir / "assets"), name="assets")


# Serve specific root-level static files (like vite.svg, favicon.ico, etc.)
@app.get("/vite.svg")
async def serve_vite_svg():
    """Serve the vite.svg file."""
    vite_svg = static_dir / "vite.svg"
    if vite_svg.exists():
        return FileResponse(vite_svg)
    return {"error": "File not found"}


# Serve the SPA - this should be last to catch all non-API/non-asset routes
@app.get("/{full_path:path}")
async def serve_spa(full_path: str):
    """Serve the single-page application for all non-API routes."""
    # full_path is unused but required for the path parameter
    index_file = static_dir / "index.html"
    if index_file.exists():
        return FileResponse(index_file)
    else:
        return {"message": "Frontend not built yet. Run 'task build' first."}
