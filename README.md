# 🚀 OpenEmbedd

**OpenEmbedd** is a lightweight, OpenAI-compatible embedding API built with **FastAPI** and **Sentence Transformers**. It provides a simple REST API for generating high-quality text embeddings, making it ideal for Retrieval-Augmented Generation (RAG), semantic search, recommendation systems, and AI applications.

The project is designed to be lightweight enough to run on free cloud platforms like **Render** and **Railway**, while maintaining a clean and modular architecture.

---

## ✨ Features

- ⚡ FastAPI-based REST API
- 🤖 Sentence Transformers for embedding generation
- 📦 Batch embedding support
- 🔄 OpenAI-style API design
- 🧩 Modular project architecture
- 📋 Pydantic request/response validation
- 📝 Structured logging
- ⚙️ Environment-based configuration
- ❤️ Health check endpoint
- 🚀 Ready for Docker and cloud deployment

---

## 📂 Project Structure

```text
OpenEmbedd/
│
├── app/
│   ├── api/
│   │   ├── embeddings.py
│   │   └── health.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── logger.py
│   │   └── model_manager.py
│   │
│   ├── schemas/
│   │   ├── embedding.py
│   │   └── health.py
│   │
│   ├── services/
│   │   └── embedding_service.py
│   │
│   └── main.py
│
├── tests/
├── .env
├── requirements.txt
└── README.md
```

---

## 🛠 Tech Stack

- Python
- FastAPI
- Uvicorn
- Sentence Transformers
- Hugging Face Transformers
- PyTorch
- Pydantic

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Vishnu917vj/OpenEmbedd.git

cd OpenEmbedd
```

Create a virtual environment:

### Windows

```powershell
python -m venv venv

venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Environment Variables

Create a `.env` file:

```env
APP_NAME=OpenEmbedd
API_VERSION=1.0.0
MODEL_NAME=BAAI/bge-small-en-v1.5
```

---

## ▶️ Running the API

```bash
uvicorn app.main:app --reload
```

The API will be available at

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Health Check

```
GET /health
```

Example Response

```json
{
  "status": "healthy",
  "model": "BAAI/bge-small-en-v1.5",
  "version": "1.0.0"
}
```

---
## Live Link

- Link : https://openembedd-production.up.railway.app/

---

## Generate Embeddings

```
POST /v1/embeddings
```

### Single Input

Request

```json
{
    "input":"What is Retrieval Augmented Generation?"
}
```

---

### Batch Input

```json
{
    "input":[
        "Artificial Intelligence",
        "Machine Learning",
        "Deep Learning"
    ]
}
```

---

### Example Response

```json
{
    "object":"list",
    "model":"BAAI/bge-small-en-v1.5",
    "created":1740000000,
    "dimensions":384,
    "inference_time_ms":9.42,
    "data":[
        {
            "index":0,
            "embedding":[
                0.021,
                -0.314,
                ...
            ]
        }
    ]
}
```

---

## 🏗 Architecture

```text
             Client

                │

                ▼

            FastAPI API

                │

                ▼

      Embedding Service

                │

                ▼

         Model Manager

                │

                ▼

     Sentence Transformer

                │

                ▼

         Embedding Vector
```

---

## 💡 Use Cases

OpenEmbedd can be used for:

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- AI Chatbots
- Recommendation Systems
- Document Search
- Similarity Search
- Knowledge Base Retrieval
- Vector Database Pipelines

---

## 🔮 Future Improvements

- Docker support
- Pinecone integration
- ChromaDB support
- FAISS support
- ONNX optimization
- Multiple embedding models
- Authentication
- Rate limiting
- Metrics & monitoring

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Vishnu Amarapu**

- GitHub: https://github.com/Vishnu917vj
- LinkedIn: [www.linkedin.com/in/vishnu-amarapu](https://www.linkedin.com/in/vishnu-amarapu-373a30212/)
- Portfolio: https://portfolio-ashen-three-7qiqa4kgdc.vercel.app/
