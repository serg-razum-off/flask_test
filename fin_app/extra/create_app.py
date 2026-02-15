from fastapi import FastAPI
from fin_app.settings.config import HOST, PORT
from contextlib import asynccontextmanager
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for FastAPI application."""
    logger.info(f"\n\n >> 🚀 Project is starting up on {HOST}:{PORT}")
    try:
        yield
    finally:
        logger.info(f"\n\n >> ❌ Project is shutting down on {HOST}:{PORT}")


def create_app() -> FastAPI:
    """Create FastAPI financial tracker application."""
    app = FastAPI(
        title="Financial Tracker",
        description="Financial tracker application",
        version="0.1.0",
        lifespan=lifespan,
    )
    return app
