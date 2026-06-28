from app.core.manager import model_manager
import time
from app.core.logger import logger


class EmbeddingService:


    def embed(self, texts):
        logger.info(f"Embedding {len(texts)} text(s).")
        start = time.time()

        model = model_manager.get_model()

        embeddings = model.encode(
    texts,
    normalize_embeddings=True,
    convert_to_numpy=True,
)

        elapsed = round((time.time() - start) * 1000, 2)
        logger.info(
    f"Generated {len(embeddings)} embeddings "
    f"in {elapsed:.2f} ms."
)

        return embeddings.tolist(), elapsed


embedding_service = EmbeddingService()