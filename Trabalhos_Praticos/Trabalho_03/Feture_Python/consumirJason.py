import tkinter as tk
from tkinter import filedialog

def escolher_arquivo_json():
    # Cria uma janela raiz (oculta)
    root = tk.Tk()
    root.withdraw()  # Oculta a janela raiz

    # Abre uma caixa de diálogo para seleção de arquivos
    file_path = filedialog.askopenfilename(
        title="Selecione o arquivo JSON",
        filetypes=[("JSON files", "*.json")],  # Filtra para mostrar apenas arquivos .json
        defaultextension=".json"
    )

    # Retorna o caminho do arquivo selecionado ou None se nenhum arquivo foi selecionado
    return file_path

