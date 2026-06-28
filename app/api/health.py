from fastapi import APIRouter

from app.schemas.health import HealthResponse
from app.core.config import settings
from app.core.logger import logger

router = APIRouter(tags=["Health"])


@router.get("/", response_model=HealthResponse)
def root():
    return HealthResponse(
        status="running",
        app=settings.APP_NAME,
        version=settings.API_VERSION,
    )


@router.get("/health", response_model=HealthResponse)
def health():
    return HealthResponse(
        status="healthy",
        app=settings.APP_NAME,
        version=settings.API_VERSION,
    )