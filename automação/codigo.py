# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer login
# Passo 3: Importar a base de dados de produtos
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o cadastro para todos os produtos

import pyautogui # Para instalar: pip install pyautogui
import time
# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> atalho (combinação de teclas)

pyautogui.PAUSE = 0.5

# Abrir o chrome
time.sleep(3)
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.click(x=1028, y=613)
pyautogui.click(x=1896, y=54) # nova aba
pyautogui.click(x=1615, y=91)

# Entrar no link
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')

# Esperar o site carregar
time.sleep(2)

# Passo 2: Fazer login
pyautogui.click(x=782, y=368)
pyautogui.write('meulogin@gmail.com')
pyautogui.press('tab')
pyautogui.write('minhasenha')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('enter')

# Passo 3: Importar a base de dados de produtos
import pandas # Para instalar: pip install pandas numpy openpyxl

tabela = pandas.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:

    # Passo 4: Cadastrar 1 produto
    pyautogui.click(x=693, y=251)

    codigo = (str(tabela.loc [linha, 'codigo']))
    marca = (str(tabela.loc [linha, 'marca']))
    tipo = (str(tabela.loc [linha, 'tipo']))
    categoria = (str(tabela.loc [linha, 'categoria']))
    preco = (str(tabela.loc [linha, 'preco_unitario']))
    custo = (str(tabela.loc [linha, 'custo']))
    obs = (str(tabela.loc[linha, 'obs']))


    # Preencher os campos
    pyautogui.write (str(codigo))
    pyautogui.press('tab')
    pyautogui.write(marca)
    pyautogui.press('tab')
    pyautogui.write(tipo)
    pyautogui.press('tab')
    pyautogui.write(categoria)
    pyautogui.press('tab')
    pyautogui.write(preco)
    pyautogui.press('tab')
    pyautogui.write(custo)
    pyautogui.press('tab')

    if obs == 'nan':
        pyautogui.write('')
    else:
        pyautogui.write(obs)


    # Apertar para enviar
    pyautogui.press('tab')
    pyautogui.press('enter')

    # Scrollar pra cima
    pyautogui.scroll(-600000)
    time.sleep(1)
    pyautogui.scroll(600000)

# Passo 5: Repetir o cadastro para todos os produtos

