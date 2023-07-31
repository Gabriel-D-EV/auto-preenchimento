import pyautogui as pa
import time
import pandas as pd


pa.press("win")
pa.write("brave")
pa.press("enter")
time.sleep(5)
pa.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pa.press("enter")
time.sleep(3)


pa.click(x=625, y=312)
pa.write("Gabriel@gmail.com")
pa.press("tab")
pa.write("lolo")

pa.press("tab")
pa.press("enter")
time.sleep(2)


tabela = pd.read_csv("produtos.csv")

linha = 0
for linha in tabela.index:
    pa.click(x=587, y=207)
    pa.write(str(tabela.loc[linha, "codigo"]))
    pa.press("tab")
    pa.write(str(tabela.loc[linha, "marca"]))
    pa.press("tab")
    pa.write(str(tabela.loc[linha, "tipo"]))
    pa.press("tab")
    pa.write(str(tabela.loc[linha, "categoria"]))
    pa.press("tab")
    pa.write(str(tabela.loc[linha, "preco_unitario"]))
    pa.press("tab")
    pa.write(str(tabela.loc[linha, "custo"]))
    pa.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pa.write(str(tabela.loc[linha, "obs"]))
    pa.press("tab")
    pa.press("enter")
    pa.scroll(5000)
    time.sleep(1)
