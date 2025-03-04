# Together.ai Models

> Last updated: March 4, 2025

## Serverless Models

### Chat Models

> If you're not sure which chat model to use, we currently recommend Llama 3.3 70B Turbo (meta-llama/Llama-3.3-70B-Instruct-Turbo) to get started.

> Note: Models marked as "Turbo" are quantized to FP8 and those marked as "Lite" are INT4. All other models are at full precision (FP16).

| Organization | Model Name | API Model String | Context Length | Quantization |
|--------------|------------|------------------|----------------|--------------|
| DeepSeek | DeepSeek-R1 | deepseek-ai/DeepSeek-R1 | 128000 | FP8 |
| DeepSeek | DeepSeek R1 Distill Llama 70B | deepseek-ai/DeepSeek-R1-Distill-Llama-70B | 131072 | FP16 |
| DeepSeek | DeepSeek R1 Distill Qwen 1.5B | deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B | 131072 | FP16 |
| DeepSeek | DeepSeek R1 Distill Qwen 14B | deepseek-ai/DeepSeek-R1-Distill-Qwen-14B | 131072 | FP16 |
| DeepSeek | DeepSeek-V3 | deepseek-ai/DeepSeek-V3 | 16384 | FP8 |
| Meta | Llama 3.3 70B Instruct Turbo | meta-llama/Llama-3.3-70B-Instruct-Turbo | 131072 | FP8 |
| Meta | Llama 3.1 8B Instruct Turbo | meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo | 131072 | FP8 |
| Meta | Llama 3.1 70B Instruct Turbo | meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo | 131072 | FP8 |
| Meta | Llama 3.1 405B Instruct Turbo | meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo | 130815 | FP8 |
| Meta | Llama 3 8B Instruct Turbo | meta-llama/Meta-Llama-3-8B-Instruct-Turbo | 8192 | FP8 |
| Meta | Llama 3 70B Instruct Turbo | meta-llama/Meta-Llama-3-70B-Instruct-Turbo | 8192 | FP8 |
| Meta | Llama 3.2 3B Instruct Turbo | meta-llama/Llama-3.2-3B-Instruct-Turbo | 131072 | FP16 |
| Meta | Llama 3 8B Instruct Lite | meta-llama/Meta-Llama-3-8B-Instruct-Lite | 8192 | INT4 |
| Meta | Llama 3 70B Instruct Lite | meta-llama/Meta-Llama-3-70B-Instruct-Lite | 8192 | INT4 |
| Meta | Llama 3 8B Instruct Reference | meta-llama/Llama-3-8b-chat-hf | 8192 | FP16 |
| Meta | Llama 3 70B Instruct Reference | meta-llama/Llama-3-70b-chat-hf | 8192 | FP16 |
| Nvidia | Llama 3.1 Nemotron 70B | nvidia/Llama-3.1-Nemotron-70B-Instruct-HF | 32768 | FP16 |
| Qwen | Qwen 2.5 Coder 32B Instruct | Qwen/Qwen2.5-Coder-32B-Instruct | 32768 | FP16 |
| Qwen | QwQ-32B-Preview | Qwen/QwQ-32B-Preview | 32768 | FP16 |
| Microsoft | WizardLM-2 8x22B | microsoft/WizardLM-2-8x22B | 65536 | FP16 |
| Google | Gemma 2 27B | google/gemma-2-27b-it | 8192 | FP16 |
| Google | Gemma 2 9B | google/gemma-2-9b-it | 8192 | FP16 |
| databricks | DBRX Instruct | databricks/dbrx-instruct | 32768 | FP16 |
| Google | Gemma Instruct (2B) | google/gemma-2b-it | 8192 | FP16 |
| Gryphe | MythoMax-L2 (13B) | Gryphe/MythoMax-L2-13b | 4096 | FP16 |
| Meta | LLaMA-2 Chat (13B) | meta-llama/Llama-2-13b-chat-hf | 4096 | FP16 |
| mistralai | Mistral Small 3 Instruct (24B) | mistralai/Mistral-Small-24B-Instruct-2501 | 32768 | FP16 |
| mistralai | Mistral (7B) Instruct | mistralai/Mistral-7B-Instruct-v0.1 | 8192 | FP16 |
| mistralai | Mistral (7B) Instruct v0.2 | mistralai/Mistral-7B-Instruct-v0.2 | 32768 | FP16 |
| mistralai | Mistral (7B) Instruct v0.3 | mistralai/Mistral-7B-Instruct-v0.3 | 32768 | FP16 |
| mistralai | Mixtral-8x7B Instruct (46.7B) | mistralai/Mixtral-8x7B-Instruct-v0.1 | 32768 | FP16 |
| mistralai | Mixtral-8x22B Instruct (141B) | mistralai/Mixtral-8x22B-Instruct-v0.1 | 65536 | FP16 |
| NousResearch | Nous Hermes 2 - Mixtral 8x7B-DPO (46.7B) | NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO | 32768 | FP16 |
| Qwen | Qwen 2.5 7B Instruct Turbo | Qwen/Qwen2.5-7B-Instruct-Turbo | 32768 | FP8 |
| Qwen | Qwen 2.5 72B Instruct Turbo | Qwen/Qwen2.5-72B-Instruct-Turbo | 32768 | FP8 |
| Qwen | Qwen 2 Instruct (72B) | Qwen/Qwen2-72B-Instruct | 32768 | FP16 |
| Qwen | Qwen2 VL 72B Instruct | Qwen/Qwen2-VL-72B-Instruct | 32768 | FP16 |
| upstage | Upstage SOLAR Instruct v1 (11B) | upstage/SOLAR-10.7B-Instruct-v1.0 | 4096 | FP16 |

### Image Models

> Use the Images endpoint for Image Models.

| Organization | Model Name | Model String for API | Default Steps |
|--------------|------------|---------------------|---------------|
| Black Forest Labs | Flux.1 [schnell] (free)* | black-forest-labs/FLUX.1-schnell-Free | N/A |
| Black Forest Labs | Flux.1 [schnell] (Turbo) | black-forest-labs/FLUX.1-schnell | 4 |
| Black Forest Labs | Flux.1 Dev | black-forest-labs/FLUX.1-dev | 28 |
| Black Forest Labs | Flux.1 Canny | black-forest-labs/FLUX.1-canny | 28 |
| Black Forest Labs | Flux.1 Depth | black-forest-labs/FLUX.1-depth | 28 |
| Black Forest Labs | Flux.1 Redux | black-forest-labs/FLUX.1-redux | 28 |
| Black Forest Labs | Flux1.1 [pro] | black-forest-labs/FLUX.1.1-pro | - |
| Black Forest Labs | Flux.1 [pro] | black-forest-labs/FLUX.1-pro | - |
| Stability AI | Stable Diffusion XL 1.0 | stabilityai/stable-diffusion-xl-base-1.0 | - |

> *Note: Due to high demand, FLUX.1 [schnell] Free has a model specific rate limit of 10 img/min. Flux Pro 1 and Flux Pro 1.1 are limited to users Build Tier 2 and above.

#### How FLUX Pricing Works
For FLUX models (except for pro), pricing is based on:
- Size of generated images (in megapixels)
- Number of steps used (if exceeding default steps)

Formula to calculate cost:
Cost = MP × Price per MP × (Steps ÷ Default Steps)

Where:
- MP = (Width × Height ÷ 1,000,000)
- Price per MP = Cost for generating one megapixel at the default steps
- Steps = The number of steps used for the image generation. This is only factored in if going above default steps.

### Vision Models

> If you're not sure which vision model to use, we currently recommend Llama 3.2 11B Turbo (meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo) to get started.

| Organization | Model Name | API Model String | Context Length |
|--------------|------------|------------------|----------------|
| Meta | (Free) Llama 3.2 11B Vision Instruct Turbo* | meta-llama/Llama-Vision-Free | 131072 |
| Meta | Llama 3.2 11B Vision Instruct Turbo | meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo | 131072 |
| Meta | Llama 3.2 90B Vision Instruct Turbo | meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo | 131072 |
| Qwen | Qwen2 Vision Language 72B Instruct | Qwen/Qwen2-VL-72B-Instruct | 32768 |

> *Free model has reduced rate limits compared to paid version of Llama 3.2 Vision 11B named Llama-3.2-11B-Vision-Instruct-Turbo

### Audio Models

> Use the Audio endpoint for audio models.

| Organization | Model Name | Model String for API |
|--------------|------------|---------------------|
| Cartesia | Cartesia/Sonic | Cartesia/Sonic |

### Code Models

> Use the Completions endpoint for Code Models.

| Organization | Model Name | Model String for API | Context Length |
|--------------|------------|---------------------|----------------|
| Qwen | Qwen 2.5 Coder 32B Instruct | Qwen/Qwen2.5-Coder-32B-Instruct | 32768 |

### Language Models

> Use the Completions endpoint for Language Models.

| Organization | Model Name | Model String for API | Context Length |
|--------------|------------|---------------------|----------------|
| Meta | LLaMA-2 (70B) | meta-llama/Llama-2-70b-hf | 4096 |
| mistralai | Mistral (7B) | mistralai/Mistral-7B-v0.1 | 8192 |
| mistralai | Mixtral-8x7B (46.7B) | mistralai/Mixtral-8x7B-v0.1 | 32768 |

### Moderation Models

> Use the Completions endpoint to run a moderation model as a standalone classifier, or use it alongside any of the other models above as a filter to safeguard responses from 100+ models, by specifying the parameter "safety_model": "MODEL_API_STRING"

| Organization | Model Name | Model String for API | Context Length |
|--------------|------------|---------------------|----------------|
| Meta | Llama Guard (7B) | Meta-Llama/Llama-Guard-7b | 4096 |

### Embedding Models

| Model Name | Model String for API | Model Size | Embedding Dimension | Context Window |
|------------|---------------------|------------|---------------------|----------------|
| M2-BERT-80M-2K-Retrieval | togethercomputer/m2-bert-80M-2k-retrieval | 80M | 768 | 2048 |
| M2-BERT-80M-8K-Retrieval | togethercomputer/m2-bert-80M-8k-retrieval | 80M | 768 | 8192 |
| M2-BERT-80M-32K-Retrieval | togethercomputer/m2-bert-80M-32k-retrieval | 80M | 768 | 32768 |
| UAE-Large-v1 | WhereIsAI/UAE-Large-V1 | 326M | 1024 | 512 |
| BGE-Large-EN-v1.5 | BAAI/bge-large-en-v1.5 | 326M | 1024 | 512 |
| BGE-Base-EN-v1.5 | BAAI/bge-base-en-v1.5 | 102M | 768 | 512 |

### Rerank Models

> Our Rerank API has built-in support for the following models, that we host via our serverless endpoints.

| Organization | Model Name | Model Size | Model String for API | Max Doc Size (tokens) | Max Docs |
|--------------|------------|------------|---------------------|----------------------|----------|
| Salesforce | LlamaRank | 8B | Salesforce/Llama-Rank-v1 | 8192 | 1024 |
