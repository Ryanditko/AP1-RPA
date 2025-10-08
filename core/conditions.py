import pyautogui
import math


def avaliar_condicao(cond, ultimo_sucesso):

    if cond is None or (isinstance(cond, float) and math.isnan(cond)):
        return True
    
    cond = str(cond).strip().lower()

    if cond == "ultimo_sucesso==true":
        return ultimo_sucesso
    elif cond == "ultimo_sucesso==false":
        return not ultimo_sucesso
    elif cond in ("true", "1", "sim"):
        return True
    elif cond in ("false", "0", "nao"):
        return False
    else:
        print(f"[Aviso] Condição desconhecida: {cond}")
        return False