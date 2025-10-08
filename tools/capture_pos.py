import pyautogui, time, json
from pathlib import Path

print("Você tem 5 segundos para posicionar o mouse sobre o ponto desejado...")
time.sleep(5)
x, y = pyautogui.position()
print(f"Coordenadas capturadas: {x}, {y}")


nome = input("Digite um nome para essa posição: ")
try:
    data_dir = Path(__file__).resolve().parent.parent / "data"
    positions_file = data_dir / "positions.json"
    with positions_file.open("r", encoding="utf-8") as f:
        posicoes = json.load(f)
except FileNotFoundError:
    posicoes = {}

posicoes[nome] = [x, y]

with positions_file.open("w", encoding="utf-8") as f:
    json.dump(posicoes, f, indent=4, ensure_ascii=False)
print("Posição salva com sucesso!")