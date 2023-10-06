import pyautogui
import time
from PIL import Image
time.sleep(2)
print(pyautogui.position())

pyautogui.scroll(-600)
time.sleep(1)
pyautogui.scroll(600)

imagem = Image.open("partida-encontrada.jpg")
x, y = 944, 731
target_color = (31,39,44,255) 
print(target_color)
