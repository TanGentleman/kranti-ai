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
export VOLUME_NAME="feb28-open-webui"
export CONTAINER_NAME="feb28-open-webui"
export PORT=8001
docker run -d -p $PORT:8080 \
-e OFFLINE_MODE=True \
-e WEBUI_NAME=Kranti \
-e WEBUI_AUTH=false \
-e LLM_API_KEY=$SENSITIVE_KEY \
-e OPENAI_API_KEY=$SENSITIVE_KEY \
-e TASK_MODEL_EXTERNAL="gemini-flash-1.5-8b" \
-e DEFAULT_MODELS="sambanova-qwen-72b" \
-e ENABLE_OLLAMA_API=False \
-e ENABLE_COMMUNITY_SHARING=False \
-e ENABLE_MESSAGE_RATING=False \
-e ENABLE_TAGS_GENERATION=False \
-e RAG_EMBEDDING_ENGINE=ollama \
-e AUDIO_STT_ENGINE=openai \
-e OPENAI_API_BASE_URL=http://host.docker.internal:4000/v1 \
-v $VOLUME_NAME:/app/backend/data --name $CONTAINER_NAME ghcr.io/open-webui/open-webui:main
```

TEST OWUI
```
export SENSITIVE_KEY="MASTER-KEY-HERE"
export VOLUME_NAME="feb28-open-webui"
export CONTAINER_NAME="dev-open-webui"
export PORT=8002
```

# TODO: Support Kokoro as Docker Container
- [Kokoro-FastAPI](https://github.com/remsky/Kokoro-FastAPI)

# Helpful links:
- https://docs.openwebui.com/getting-started/env-configuration/
