import os
from yt_dlp import YoutubeDL

playlist_url = "https://youtube.com/playlist?list=PLgrA8aw870-uklyb7j4ZyWPoYuH2ekDRx&si=OZ40TCbjE9BD8I3q"

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'musicas/%(uploader)s - %(title)s.%(ext)s',  # Formato de saída
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'download_archive': 'pai.txt',  # Evita duplicatas / nome do arquivo onde a lista de musica baixadas fica
    'ignoreerrors': True,  # Ignora erros de download
}

def rename_files():
    folder = 'musicas'
    for filename in os.listdir(folder):
        # Verifica se o nome do autor contém "Topic" e remove essa parte
        if " - Topic" in filename:
            new_filename = filename.replace(" - Topic", "")
            os.rename(os.path.join(folder, filename), os.path.join(folder, new_filename))

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])

# Após o download, renomeia os arquivos removendo "Topic" do nome do autor
rename_files()
