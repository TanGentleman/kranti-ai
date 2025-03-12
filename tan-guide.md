Running Kranti-AI:

1. Run App Shortcut (or terminal command below)
```
docker start \
dev-owui-helper \
litellm-helper-litellm-1 \
litellm-helper-db-1 \
langfuse-helper-redis-1 \
langfuse-helper-minio-1 \
langfuse-helper-clickhouse-1 \
langfuse-helper-postgres-1 \
langfuse-helper-langfuse-web-1 \
langfuse-helper-langfuse-worker-1
```

2. Open http://localhost:8002


Installation:

Docker Compose for Litellm:
```
cd litellm-helper
docker compose -f tan-docker-compose-litellm.yml up
```

Docker Compose for Langfuse:
```
cd langfuse-helper
docker compose -f tan-docker-compose-langfuse.yml -p dev-langfuse up
```

Docker Run for Open-WebUI:
```
export SENSITIVE_KEY="MASTER-KEY-HERE"
export VOLUME_NAME="mar5-open-webui"
export CONTAINER_NAME="owui-helper"
export PORT=8001
docker run -d -p $PORT:8080 \
-e OFFLINE_MODE=True \
-e WEBUI_NAME=Kranti \
-e WEBUI_AUTH=False \
-e OPENAI_API_KEY=$SENSITIVE_KEY \
-e TASK_MODEL_EXTERNAL="gemini-2.0-flash" \
-e DEFAULT_MODELS="sambanova-R1-Distill-Llama" \
-e ENABLE_OLLAMA_API=False \
-e ENABLE_COMMUNITY_SHARING=False \
-e ENABLE_MESSAGE_RATING=False \
-e ENABLE_TAGS_GENERATION=False \
-e RAG_EMBEDDING_ENGINE=openai \
-e RAG_EMBEDDING_MODEL=m2-bert-80M-8k \
-e RAG_OPENAI_API_KEY=$SENSITIVE_KEY \
-e AUDIO_STT_ENGINE=openai \
-e OPENAI_API_BASE_URL=http://host.docker.internal:4000/v1 \
-v $VOLUME_NAME:/app/backend/data --name $CONTAINER_NAME ghcr.io/open-webui/open-webui:main
```


# TODO: Support Kokoro as Docker Container
- [Kokoro-FastAPI](https://github.com/remsky/Kokoro-FastAPI)

# Helpful links:
- https://docs.openwebui.com/getting-started/env-configuration/
- https://docs.openwebui.com/getting-started/api-endpoints/
- https://docs.openwebui.com/features/plugin/functions/filter/
- https://docs.openwebui.com/tutorials/https-nginx
