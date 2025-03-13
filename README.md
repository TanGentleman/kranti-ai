# Kranti-AI

Kranti-AI is a full-stack web application that leverages a suite of Docker containers to provide an integrated AI platform with advanced language model capabilities, observability, and custom workflows.

## Overview

Kranti-AI combines several powerful components:

- **Open-WebUI**: A customized user interface for interacting with AI models
- **LiteLLM**: Proxy server for managing AI model requests
- **Langfuse**: Observability and tracing for AI interactions
- **Kokoro**: Custom TTS (Text-to-Speech) service

## Quick Start

### Running Kranti-AI

1. Start all required containers:
   ```bash
   docker start \
   dev-owui-helper \
   litellm-helper-litellm-1 \
   litellm-helper-db-1 \
   langfuse-helper-redis-1 \
   langfuse-helper-minio-1 \
   langfuse-helper-clickhouse-1 \
   langfuse-helper-postgres-1 \
   langfuse-helper-langfuse-web-1 \
   langfuse-helper-langfuse-worker-1 \
   kokoro-helper
   ```

2. Access the application at: http://localhost:8002

### Installation

#### LiteLLM Setup

```bash
cd litellm-helper
docker compose -f tan-docker-compose-litellm.yml up
```

#### Langfuse Setup
```bash
cd langfuse-helper
docker compose -f tan-docker-compose-langfuse.yml -p dev-langfuse up
```

#### Open-WebUI Setup
```bash
export SENSITIVE_KEY="MASTER-KEY-HERE"
export VOLUME_NAME="mar12-open-webui"
export CONTAINER_NAME="owui-helper"
export PORT=8001
docker run -d -p $PORT:8080 \
-e OFFLINE_MODE=True \
-e WEBUI_NAME=Kranti \
-e WEBUI_AUTH=False \
-e OPENAI_API_BASE_URL=http://host.docker.internal:4000/v1 \
-e OPENAI_API_KEY=$SENSITIVE_KEY \
-e TASK_MODEL_EXTERNAL="gemini-2.0-flash" \
-e DEFAULT_MODELS="deepseek-v3" \
-e ENABLE_OLLAMA_API=False \
-e ENABLE_COMMUNITY_SHARING=False \
-e ENABLE_MESSAGE_RATING=False \
-e ENABLE_TAGS_GENERATION=False \
-e RAG_EMBEDDING_ENGINE=openai \
-e RAG_EMBEDDING_MODEL=m2-bert-80M-8k \
-e AUDIO_STT_ENGINE=openai \
-e AUDIO_TTS_ENGINE=openai \
-e AUDIO_TTS_OPENAI_API_BASE_URL=http://host.docker.internal:4000/v1 \
-e AUDIO_TTS_OPENAI_API_KEY=$SENSITIVE_KEY \
-e AUDIO_TTS_MODEL=kokoro-tts \
-e AUDIO_TTS_VOICE=af_bella \
-v $VOLUME_NAME:/app/backend/data --name $CONTAINER_NAME ghcr.io/open-webui/open-webui:main
```

#### Kokoro TTS Setup
```bash
docker run -p 8880:8880 --name kokoro-helper ghcr.io/remsky/kokoro-fastapi-cpu:v0.2.2
```

## Architecture

Kranti-AI consists of the following key components:

1. **Open-WebUI**:
   - Frontend interface for user interactions
   - Backend integration with other services
   - Customizable workflows

2. **Langfuse**:
   - Observability and monitoring
   - Request/response tracing
   - Performance analytics

3. **LiteLLM**:
   - Proxy server for AI model requests
   - Load balancing
   - API standardization

4. **Kokoro**:
   - Text-to-Speech capabilities
   - Voice synthesis

## Deployment

The application can be deployed as individual Docker containers (as shown above) or as a Kubernetes cluster for production environments. See the implementation plan for detailed Kubernetes deployment manifests.

## Resources for future work:

- [Open-WebUI Documentation](https://docs.openwebui.com/getting-started/env-configuration/)
- [Open-WebUI API Endpoints](https://docs.openwebui.com/getting-started/api-endpoints/)
- [Open-WebUI Plugin Functions](https://docs.openwebui.com/features/plugin/functions/filter/)
- [HTTPS with Nginx Tutorial](https://docs.openwebui.com/tutorials/https-nginx)

## Development

This project is under active development. Current focus areas include:
- Kubernetes deployment optimization
- Custom server integration
- Advanced workflow capabilities

## License

MIT License