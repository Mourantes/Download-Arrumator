from pathlib import Path
import os
import shutil

def cria_pastas(pastas):

    print("Criando pastas...")
    for pasta in pastas:
        try:
            Path.mkdir(pasta)
            print(f"Pasta {pasta} criada")
        except FileExistsError:
            print(f"A pasta {pasta} já existe")
        
        
def move_arquivos():
    
    diretorio_original = Path(".")

    # Verificando arquivos no diretório
    for f in os.listdir(diretorio_original):

        # Validando se é um arquivo
        if os.path.isfile(f):
            src_path = os.path.join(diretorio_original, f)
        
            for key in pastas:
                extensao = pastas[key]
                if f.endswith(extensao):
                    dest_path = os.path.join(diretorio_original, key, f)
                    shutil.move(src_path, dest_path)
                    break

if __name__ == '__main__':
    # Dicionário de pastas e as extensões que lhe pertencem
    pastas = {
        "Documentos": (".pdf", ".txt", ".docx", ".doc", ".pptx", ".pbix", ".xlsx", ".xls", ".rtf"),
        "Fotos": (".jpeg", ".jpg", ".png", "gif", ".bmp", ".webp", ".heic", ".raw", ".tiff", ".svg"),
        "Áudios": (".wav", ".aiff", ".pcm", ".mp3", ".aac", ".ogg", ".wma", ".flac", ".alac", ".ape", ".m4a", ".dsf", ".dff"),
        "Vídeos": (".avi", ".wmv", ".mov", ".qt", ".mkv", ".mp4", ".avchd", ".flv", ".swf", ".webm"),
        "Executáveis": ".exe",
        "Arquivos Compactados": (".zip", ".rar", ".zip")
    }

cria_pastas(pastas)
move_arquivos()