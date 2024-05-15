import pyautogui
import time
import pandas as pd

usuario = "vinibeliza@gmail.com"
senha = "vini789456"
site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# pyautogui.click
# pyautogui.write
# pyautogui.press
pyautogui.PAUSE = 0.5
# Abrir o windows iniciar
pyautogui.press("win")

pyautogui.write("Brave")

pyautogui.press("enter")

time.sleep(3)

pyautogui.write(site)

pyautogui.press("enter")

time.sleep(3)

# print(pyautogui.position())
pyautogui.click(x=844, y=371)

pyautogui.write(usuario)

pyautogui.press("tab")

pyautogui.write(senha)

pyautogui.press("tab")

pyautogui.press("enter")

time.sleep(3)

df = pd.read_csv("produtos.csv")


for linha in df.index:       

    codigo = str(df.loc[linha, "codigo"])
    marca = str(df.loc[linha, "marca"])
    tipo = str(df.loc[linha, "tipo"])
    categoria = str(df.loc[linha, "categoria"])
    preco_unitario = str(df.loc[linha, "preco_unitario"])
    custo = str(df.loc[linha, "custo"])
    obs = str(df.loc[linha, "obs"])

    # Código do Produto
    pyautogui.click(x=743, y=248)
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # Marca do Produto
    pyautogui.write(marca)
    pyautogui.press("tab")

    # Tipo do Produto
    pyautogui.write(tipo)
    pyautogui.press("tab")

    # Categoria do Produto
    pyautogui.write(categoria)
    pyautogui.press("tab")

    # Preço Unitário do Produto
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    # Custo do Produto
    pyautogui.write(custo)
    pyautogui.press("tab")

    # OBS
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")

    pyautogui.press("enter")
    # pyautogui.scroll(200)
    pyautogui.press("Home")