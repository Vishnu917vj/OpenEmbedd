import time
import torch

from sentence_transformers import SentenceTransformer

from app.core.config import settings
from app.core.logger import logger


class ModelManager:

    def __init__(self):
        self.embedding_model = None

    def get_device(self):

        if hasattr(torch, "xpu") and torch.xpu.is_available():
            return "xpu"

        if torch.cuda.is_available():
            return "cuda"

        return "cpu"

    def load_model(self):

        if self.embedding_model is not None:
            return

        device = self.get_device()

        logger.info(f"Using device: {device}")

        start = time.time()

        self.embedding_model = SentenceTransformer(
            settings.MODEL_NAME,
            device=device,
        )

        logger.info(
            f"Model loaded in {time.time() - start:.2f} seconds."
        )

    def get_model(self):

        if self.embedding_model is None:
            raise RuntimeError("Embedding model not loaded.")

        return self.embedding_model


model_manager = ModelManager()