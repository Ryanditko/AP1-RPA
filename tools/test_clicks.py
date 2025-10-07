import pyautogui

print("Teste de clique — mova o mouse para onde quiser e pressione ENTER.")
input("Pressione ENTER para clicar...")
x, y = pyautogui.position()
pyautogui.click(x, y)
print(f"Clique realizado em ({x},{y})")