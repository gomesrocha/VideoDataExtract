# VideoDataExtract
Microservice project to extract data from youtube and kwai videos, using Python with FastAPI


## Executing in Docker
docker build -t videodataextract .

docker run -p 8000:8000 videodataextract


## Executando com uv
uv run uvicorn app.main:app --port 8000 --reload
