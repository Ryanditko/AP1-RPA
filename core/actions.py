import time
import pyautogui
from core import interpretar_coordenada

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.25


def clicar(nome_ou_coord, posicoes):

    try:
        if isinstance(nome_ou_coord, str) and nome_ou_coord in posicoes:
            x, y = posicoes[nome_ou_coord]
        elif "," in str(nome_ou_coord):
            x, y = interpretar_coordenada(nome_ou_coord)
        else:
            return False, f"Posição '{nome_ou_coord}' não encontrada."

        pyautogui.click(x, y)
        return True, f"Clique realizado em ({x},{y})."
    except Exception as e:
        return False, f"Erro ao clicar: {e}"


def digitar_texto(texto):
    try:
        pyautogui.write(str(texto), interval=0.03)
        return True, f"Texto digitado: {texto}"
    except Exception as e:
        return False, f"Erro ao digitar: {e}"


def pressionar_tecla(tecla):
    try:
        if "+" in str(tecla):
            teclas = [t.strip() for t in tecla.split("+")]
            pyautogui.hotkey(*teclas)
        else:
            pyautogui.press(tecla)
        return True, f"Tecla '{tecla}' pressionada."
    except Exception as e:
        return False, f"Erro ao pressionar tecla: {e}"


def esperar(segundos):
    try:
        s = float(segundos)
        time.sleep(s)
        return True, f"Aguardado {s} segundos."
    except Exception as e:
        return False, f"Erro ao esperar: {e}"


def rolar_tela(qtd):
    try:
        pyautogui.scroll(int(qtd))
        return True, f"Rolagem de tela: {qtd} unidades."
    except Exception as e:
        return False, f"Erro ao rolar tela: {e}"