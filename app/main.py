from fastapi import FastAPI
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from dotenv import load_dotenv
import os

from app.routes import upload, analyze
from app.utils.logger import setup_logger
from fastapi.exceptions import RequestValidationError
from app.utils.errors import validation_exception_handler

# Load environment variables
load_dotenv()

logger = setup_logger("main")

# Lifespan for startup/shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    PORT = int(os.getenv("PORT", 8000))
    HOST = os.getenv("HOST", "localhost") 


    logger.info("Server starting up!")
    logger.info(f"Base API path: http://{HOST}:{PORT}/")
    logger.info(f"API documentation available at: http://{HOST}:{PORT}/docs")
    
    yield  
    logger.info("Server shutting down!")


app = FastAPI(
    title="Veefyed – Image Analysis API",
    description="""
Backend service for mobile clients to:
- Upload images
- Perform mock AI analysis
- Receive structured JSON responses

Designed to demonstrate backend API design and integration.
""",
    version="1.0.0",
    contact={
        "name": "Your Name",
        "email": "your@email.com",
    },
    lifespan=lifespan
)


app.add_exception_handler(RequestValidationError, validation_exception_handler)


app.include_router(upload.router, prefix="/v1/upload", tags=["Upload"])
app.include_router(analyze.router, prefix="/v1/analyze", tags=["Analyze"])


@app.get("/", summary="API Landing Page", description="Welcome to the Image Analysis API. Check /docs for full API specifications.")
def landing():
    HOST = os.getenv("HOST", "localhost")
    PORT = int(os.getenv("PORT", 8000))
    logger.info("Landing page accessed")
    return JSONResponse(
        content={
            "message": "Welcome to the Veefyed Image Analysis API!",
            "instructions": f"Visit http://{HOST}:{PORT}/docs for API specifications and try-it-out."
        }
    )
