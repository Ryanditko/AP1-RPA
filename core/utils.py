import json
import os


def carregar_posicoes(caminho):
    """Carrega o arquivo JSON com as posições da tela."""
    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def interpretar_coordenada(valor):
    """Transforma 'x,y' em tupla (x, y)."""
    partes = str(valor).split(",")
    return int(partes[0].strip()), int(partes[1].strip())