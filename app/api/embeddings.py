from fastapi import APIRouter

from app.schemas.embedding import (
    EmbeddingRequest,
    EmbeddingResponse,
    EmbeddingData,
    Usage,
)

from app.services.embedding_service import embedding_service
from app.core.config import settings
import time
from app.core.logger import logger


router = APIRouter(prefix="/v1", tags=["Embeddings"])


@router.post("/embeddings", response_model=EmbeddingResponse)
def create_embedding(request: EmbeddingRequest):

    texts = request.input

    if isinstance(texts, str):
        texts = [texts]
    logger.info(
    f"Received embedding request with {len(texts)} input(s)."
)
    vectors, inference_time = embedding_service.embed(texts)

    data = []

    for index, vector in enumerate(vectors):
        data.append(
            EmbeddingData(
                index=index,
                embedding=vector,
            )
        )
    logger.info(
    "Embedding request completed successfully."
)
    return EmbeddingResponse(
    data=data,
    model=settings.MODEL_NAME,
    created=int(time.time()),
    usage=Usage(
        prompt_tokens=0,
        total_tokens=0,
    ),
)