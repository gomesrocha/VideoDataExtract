from fastapi import APIRouter, HTTPException
from app.schemas.url_video import URLInput
from app.domain.video_processor import VideoProcessor
import logging

# Configuração de logs
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Instancia o processador de vídeos
video_processor = VideoProcessor()

# Criação do roteador
router = APIRouter()

@router.post("/validate-url")
async def validate_url(input_data: URLInput):
    """
    Valida se a URL está correta.
    """
    return {"url": input_data.url}


@router.post("/extract-data/")
async def extract_data(input_data: URLInput):
    """
    Endpoint para processar vídeo a partir de uma URL.
    """
    try:
        transcription = video_processor.process_video(input_data)
        return {"transcription": transcription}
    except Exception as e:
        logger.error(f"Error during video processing: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
