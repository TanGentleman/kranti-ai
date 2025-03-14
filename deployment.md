# Citation: https://www.youtube.com/watch?v=Vljxmh1aUyw
# Deployment guide

1. Enter https://console.cloud.google.com/run?project=kranti-ai&cloudshell=true
2. In shell:
```
REPOSITORY_NAME=ollama-cloud
gcloud artifacts repositories create $REPOSITORY_NAME \
--repository-format=docker \
--location=us-west1
gcloud auth configure-docker us-west1-docker.pkg.dev

mkdir ollama
touch Dockerfile
<EDIT DOCKERFILE HERE>
PROJECT_ID=kranti-project
gcloud builds submit \
--tag us-centrall-docker.pkg.dev/$PROJECT_ID/$REPOSITORY_NAME/o1lama-gemma-3
--machine-type e2-standard-2

mkdir openwebui
docker pull ghcr.io/open-webui/open-webui:main
docker tag ghcr.io/open-webui/open-webui:main us-central1-docker.pkg.dev/$PROJECT_ID/$REPOSITORY_NAME/openwebui
```

REPOSITORY_NAME=custom-owui