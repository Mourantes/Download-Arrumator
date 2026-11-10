from pathlib import Path
import os
import shutil

def cria_pastas():

    print("Criando pastas...")

    try:
        Path.mkdir("./Mídia")
        print("Pasta de Mídias criada.")

    except FileExistsError:
        print("A pasta de Mídias já existe.")

    try:
        Path.mkdir("./Documentos")
        print("Pasta de Documentos criada.")
        
    except FileExistsError:
        print("A pasta de Documentos já existe.")

    try:
        Path.mkdir("./Executáveis")
        print("Pasta de Executáveis criada.")
        
    except FileExistsError:
        print("A pasta de Executáveis já existe.")

    try:
        Path.mkdir("./Fotos")
        print("Pasta de Fotos criada.")
        
    except FileExistsError:
        print("A pasta de Fotos já existe.")

    try:
        Path.mkdir("./Arquivos compactados")
        print("Pasta de Arquivos compactados criada.")
        
    except FileExistsError:
        print("A pasta de Arquivos compactados já existe.")
        
        
def move_arquivos():

    # ========================================================
    # IDENTIFICANDO DIRETÓRIOS
    # ========================================================
    diretorio_original = Path(".")
    dir_docs = Path("./Documentos")
    dir_mid = Path("./Mídia")
    dir_fot = Path("./Fotos")
    dir_exec = Path("./Executáveis")
    dir_zip = Path("./Arquivos compactados")

    for f in diretorio_original.glob("*"):
        
        # Validando se é um arquivo
        if os.path.isfile(f):

            #==================================================
            # Identificando tipos de arquivo de texto
            #==================================================
            if f.suffix == '.pdf':
                shutil.move(f"./{f}", f"{dir_docs}/{f}")

            elif f.suffix == '.txt':
                shutil.move(f"./{f}", f"{dir_docs}/{f}")

            elif f.suffix == '.docx':
                shutil.move(f"./{f}", f"{dir_docs}/{f}")

            elif f.suffix == '.doc':
                shutil.move(f"./{f}", f"{dir_docs}/{f}")

            elif f.suffix == '.pptx':
                shutil.move(f"./{f}", f"{dir_docs}/{f}")

            elif f.suffix == '.pdf':
                shutil.move(f"./{f}", f"{dir_docs}/{f}")

            elif f.suffix == '.pbix':
                shutil.move(f"./{f}", f"{dir_docs}/{f}")

            elif f.suffix == '.xlsx':
                shutil.move(f"./{f}", f"{dir_docs}/{f}")

            elif f.suffix == '.xls':
                shutil.move(f"./{f}", f"{dir_docs}/{f}")

            elif f.suffix == '.rtf':
                shutil.move(f"./{f}", f"{dir_docs}/{f}")

            # ================================================
            # Identificando arquivos de fotos
            # ================================================

            if f.suffix == '.jpeg':
                shutil.move(f"./{f}", f"{dir_fot}/{f}")

            elif f.suffix == '.jpg':
                shutil.move(f"./{f}", f"{dir_fot}/{f}")

            elif f.suffix == '.png':
                shutil.move(f"./{f}", f"{dir_fot}/{f}")

            elif f.suffix == '.gif':
                shutil.move(f"./{f}", f"{dir_fot}/{f}")

            # ================================================
            # Identificando arquivos de mídia
            # ================================================

            if f.suffix == '.mp3':
                shutil.move(f"./{f}", f"{dir_mid}/{f}")

            if f.suffix == '.mp4':
                shutil.move(f"./{f}", f"{dir_mid}/{f}")

            if f.suffix == '.m4a':
                shutil.move(f"./{f}", f"{dir_mid}/{f}")

            if f.suffix == '.mpeg':
                shutil.move(f"./{f}", f"{dir_mid}/{f}")

            if f.suffix == '.mp3':
                shutil.move(f"./{f}", f"{dir_mid}/{f}")

            # ================================================
            # Identificando arquivos executáveis
            # ================================================

            if f.suffix == '.exe':
                shutil.move(f"./{f}", f"{dir_exec}/{f}")

            # ================================================
            # Identificando arquivos compactados
            # ================================================

            if f.suffix == '.zip':
                shutil.move(f"./{f}", f"{dir_zip}/{f}")

            if f.suffix == '.rar':
                shutil.move(f"./{f}", f"{dir_zip}/{f}")

            if f.suffix == '.7z':
                shutil.move(f"./{f}", f"{dir_zip}/{f}")


cria_pastas()
move_arquivos()