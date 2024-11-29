from fastapi import FastAPI
from app.routes.video_routes import router as video_router

app = FastAPI(
    title="Video Data Extract",
    description="A microservice for extracting data from YouTube and Kwai",
    version="1.0.0"
)

# Inclui as rotas de vídeo
app.include_router(video_router, prefix="/video", tags=["Video Processing"])

@app.get("/")
def read_root():
    return {"message": "Video Data Extract API is running!"}