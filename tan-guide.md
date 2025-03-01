Docker Compose for Litellm:
```
cd litellm
docker compose -f tan-docker-compose-litellm.yml up
```

Docker Compose for Langfuse:
```
cd langfuse
docker compose -f tan-docker-compose-langfuse.yml up
```

Docker Run for Open-WebUI:
```
export SENSITIVE_KEY="MASTER-KEY-HERE"
export CUSTOM_DOCKER_NAME="feb28-open-webui"
docker run -d -p 8001:8080 \
-e WEBUI_NAME=Kranti \
-e WEBUI_AUTH=false \
-e LLM_API_KEY=$SENSITIVE_KEY \
-e OPENAI_API_KEY=$SENSITIVE_KEY \
-e TASK_MODEL_EXTERNAL="gemini-flash-1.5-8b" \
-e DEFAULT_MODELS="sambanova-qwen-72b" \
-e ENABLE_OLLAMA_API=False \
-e ENABLE_COMMUNITY_SHARING=False \
-e ENABLE_MESSAGE_RATING=False \
-e RAG_EMBEDDING_ENGINE=ollama \
-e AUDIO_STT_ENGINE=openai \
-e OPENAI_API_BASE_URL=http://host.docker.internal:4000/v1 \
-v $CUSTOM_DOCKER_NAME:/app/backend/data --name $CUSTOM_DOCKER_NAME ghcr.io/open-webui/open-webui:main
```

# TODO: Add Kokoro container (see https://github.com/eduardolat/kokoro-web or similar)
