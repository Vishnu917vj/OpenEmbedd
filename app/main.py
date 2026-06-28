from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.embeddings import router as embedding_router

from app.core.config import settings
from app.core.manager import model_manager


@asynccontextmanager
async def lifespan(app: FastAPI):

    model_manager.load_model()

    yield

    print("Shutting down OpenEmbed...")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.API_VERSION,
    lifespan=lifespan,
)

app.include_router(health_router)
app.include_router(embedding_router)