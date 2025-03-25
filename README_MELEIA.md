# 🎵 yt-dlp Playlist Downloader  

Um script em Python para baixar músicas de playlists do YouTube, converter para MP3 e organizar os arquivos automaticamente. Ele também renomeia os arquivos removendo " - Topic" dos nomes de alguns canais.  

## Requisitos  

Antes de rodar o script, você precisa ter:  

- **Python 3** instalado → "https://www.python.org/downloads/"  
- **yt-dlp** instalado → "https://github.com/yt-dlp/yt-dlp"  
- **FFmpeg** instalado → "https://ffmpeg.org/download.html"  

## Instalação  

1. **Clone o repositório**  
   ```bash
   git clone https://github.com/Miguelfranci/downloader_youtubeplaylists.git
   cd downloader_youtubeplaylists
   ```  

2. **Instale as dependências**  
   ```bash
   pip install yt-dlp
   ```  

3. **Instale o FFmpeg**  
   - **Windows**: Guia de instalação = "https://github.com/BtbN/FFmpeg-Builds/releases"  
   - **Linux (Debian/Ubuntu)**:  
     ```bash
     sudo apt install ffmpeg
     ```  
   - **MacOS**:  
     ```bash
     brew install ffmpeg
     ```  

## Como Usar  

1. Abra o arquivo `.py` e troque a variável `playlist_url` pela URL da sua playlist.  
2. Execute o script:  
   ```bash
   python dlp.py
   ```  
3. O áudio será salvo na pasta **musicas/** e arquivos duplicados serão ignorados.  

## Contribuições  

Se quiser sugerir algo, manda um PR ou abre uma issue. Toda ajuda é bem-vinda!, sou um dev junior e so fiz para aprender como funciona o youtube.py qualquer melhoria é bem vinda

