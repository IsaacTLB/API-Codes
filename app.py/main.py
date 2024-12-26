# Import dependencies
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import scraper, regex 
from models.request import ScrapeRequestModel, RegexRequestModel
from models.response import ScrapeResponseModel, RegexResponseModel

# Logger setup function
from utils.logging_config import setup_logging

# Initialize FastAPI app
app = FastAPI()

# CORS settings
origins = [
    "http://localhost:3000",  # Link for local frontend development
    "https://frontend.example.com",  # Link for deployed frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup logger
logger = setup_logging("app_logger")

# Include routers
app.include_router(scraper.router, prefix="/scraper", tags=["Scraper"])
app.include_router(regex.router, prefix="/regex", tags=["Regex"])

@app.on_event("startup")
async def startup():
    """Handle application startup tasks."""
    logger.info("Application startup")

@app.on_event("shutdown")
async def shutdown():
    """Handle application shutdown tasks."""
    logger.info("Application shutdown")
