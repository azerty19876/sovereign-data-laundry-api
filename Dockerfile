# ==============================================================================
# COMPONENT: ENTERPRISE CONTAINERIZATION ARCHITECTURE (Dockerfile)
# ==============================================================================
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY backend.py frontend.py /app/

RUN pip install --no-cache-dir fastapi uvicorn streamlit requests pandas

EXPOSE 8000
EXPOSE 8501

CMD ["sh", "-c", "python backend.py & sleep 3 && streamlit run frontend.py --server.port=8501 --server.address=0.0.0.0"]
