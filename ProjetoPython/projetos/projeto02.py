import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title= "Selecione uma pasta")

lista_arquivos = os.listdir(caminho)

locais = {
    "imagens": [".png",".jpg"],
    "planilhas": [".xlsx"],
    "pdfs": [".pdf"],
    "csv": [".csv"]
}

for projetos in lista_arquivos:
    
    nome, extensao = os.path.splitext(f"{caminho}/{projetos}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
                os.rename(f"{caminho}/{projetos}", f"{caminho}/{pasta}/{projetos}") 
           