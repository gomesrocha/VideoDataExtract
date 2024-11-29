Aqui está um modelo de README para o seu projeto, organizado e claro:

---

# **Video Data Extract API**

## **Descrição**
O **Video Data Extract API** é um microsserviço desenvolvido em Python usando o framework **FastAPI**, projetado para processar vídeos do YouTube e Kwai. Ele oferece funcionalidades para:
- Validar URLs fornecidas.
- Extrair dados de vídeos, incluindo o áudio e a transcrição usando o modelo **Whisper**.

Este projeto é ideal para soluções que requerem extração e análise de conteúdo de vídeos de plataformas populares.

---

## **Funcionalidades**
1. **Validação de URL**:
   - Endpoint que verifica se a URL fornecida pertence a plataformas suportadas (YouTube e Kwai).

2. **Extração de Dados**:
   - Faz o download do vídeo.
   - Extrai o áudio do vídeo.
   - Transcreve o áudio usando o modelo de linguagem **Whisper**.

---

## **Tecnologias Utilizadas**
- **FastAPI**: Framework para construir APIs rápidas e performáticas.
- **Pydantic**: Validação de dados de entrada.
- **Whisper**: Modelo de transcrição de áudio.
- **yt-dlp**: Ferramenta para download de vídeos.
- **FFmpeg**: Processamento de áudio e vídeo.
- **Python 3.12**: Linguagem de programação principal.

---
Aqui está a seção adicionada sobre como executar o projeto usando **Docker**:

---

## **Execução via Docker**

### Pré-requisitos
- **Docker** instalado em sua máquina. Para instruções de instalação, consulte a [documentação oficial](https://docs.docker.com/get-docker/).


2. Construa a imagem Docker:
   ```bash
   docker build -t video-data-extract .
   ```

### Executar o Contêiner
1. Rode o contêiner com a imagem criada:
   ```bash
   docker run -d -p 8000:8000 --name video-data-extract video-data-extract
   ```

2. Agora, a aplicação estará acessível em:
   - [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) para a documentação interativa.
   - [http://127.0.0.1:8000/](http://127.0.0.1/) para a página inicial.

3. **Endpoints Disponíveis**:
   - **`POST /video/validate-url`**:
     - Valida se a URL fornecida é de um domínio suportado.
     - **Entrada**:
       ```json
       {
         "url": "https://www.youtube.com/shorts/V764-x5kDHU"
       }
       ```
     - **Saída**:
       ```json
       {
         "url": "https://www.youtube.com/shorts/V764-x5kDHU"
       }
       ```

   - **`POST /video/extract-data`**:
     - Faz o download do vídeo, extrai o áudio e transcreve o conteúdo.
     - **Entrada**:
       ```json
       {
         "url": "https://www.youtube.com/shorts/V764-x5kDHU"
       }
       ```
     - **Saída**:
       ```json
       {
         "transcription": "Transcrição do áudio extraído."
       }
       ```
### Parar e Remover o Contêiner
- **Parar o contêiner**:
  ```bash
  docker stop video-data-extract
  ```

- **Remover o contêiner**:
  ```bash
  docker rm video-data-extract
  ```


---

## **Estrutura do Projeto**
```
app/
├── domain/
│   └── video_processor.py      # Lógica de extração e processamento de vídeos
├── routes/
│   └── video_routes.py         # Endpoints da API
├── schemas/
│   └── url_video.py            # Validação de entrada (Pydantic)
├── main.py                     # Configuração do FastAPI e inicialização
```

---

## **Contribuindo**
1. Faça um fork do repositório.
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Commit suas mudanças:
   ```bash
   git commit -m "Adicionei minha feature"
   ```
4. Faça o push para a branch:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.

---

## **Licença**
Este projeto é licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais informações.

---
