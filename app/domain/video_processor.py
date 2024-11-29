from app.schemas.url_video import URLInput
import whisper
import subprocess
import yt_dlp
import tempfile
import os
import time


class VideoProcessor:
    def __init__(self):
        # Carrega o modelo Whisper na inicialização
        self.whisper_model = whisper.load_model("base")

    def download_video(self, url: str) -> str:
        """
        Faz o download do vídeo a partir da URL.
        """
        print(f"Downloading video from: {url}")
        start_time = time.time()
        temp_dir = tempfile.gettempdir()
        ydl_opts = {
            'outtmpl': os.path.join(temp_dir, '%(title)s.%(ext)s'),
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
            'quiet': True
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)
        end_time = time.time()
        print(f"Time to download video: {end_time - start_time:.2f} seconds")
        return file_path

    def extract_audio(self, video_path: str) -> str:
        """
        Extrai o áudio de um vídeo.
        """
        print(f"Extracting audio from video: {video_path}")
        start_time = time.time()
        audio_path = video_path.replace(".mp4", ".mp3")
        command = f"ffmpeg -i '{video_path}' -ar 16000 -ac 1 -q:a 0 -map a '{audio_path}' -y"
        subprocess.run(command, shell=True, check=True)
        end_time = time.time()
        print(f"Time to extract audio: {end_time - start_time:.2f} seconds")
        return audio_path

    def transcribe_audio(self, audio_path: str) -> str:
        """
        Transcreve o áudio usando o modelo Whisper.
        """
        print(f"Transcribing audio from: {audio_path}")
        start_time = time.time()
        result = self.whisper_model.transcribe(audio_path, language="pt")  # Força o uso do português
        end_time = time.time()
        print(f"Transcription completed in {end_time - start_time:.2f} seconds.")
        return result['text']

    def process_video(self, url_input: URLInput) -> str:
        """
        Processo completo: download do vídeo, extração de áudio e transcrição.
        """
        url = str(url_input.url)  # Garantia de que é string
        video_path = self.download_video(url)
        audio_path = self.extract_audio(video_path)
        transcription = self.transcribe_audio(audio_path)
        return transcription
