import json
import os


def carregar_posicoes(caminho):

    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def interpretar_coordenada(valor):

    partes = str(valor).split(",")
    return int(partes[0].strip()), int(partes[1].strip())