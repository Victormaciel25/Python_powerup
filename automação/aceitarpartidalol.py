import pyautogui
import time
from PIL import Image

pyautogui.press('win')
time.sleep(1)
pyautogui.write('lol')
time.sleep(1)
pyautogui.press('enter')
time.sleep(40)
pyautogui.click(x=436, y=195)
time.sleep(2)
pyautogui.click(x=508, y=730)
time.sleep(1)
pyautogui.click(x=854, y=839)
time.sleep(4)
pyautogui.click(x=849, y=835)

imagem = Image.open("partida-encontrada.jpg")
target_color = (31,39,44,255)
pixel_color = imagem.getpixel((944, 731))

if pixel_color == target_color:
   pyautogui.click(x=946, y=714)







