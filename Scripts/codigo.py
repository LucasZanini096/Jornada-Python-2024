import pandas as pd
import pyautogui
import time


#importar base de dados
tabela = pd.read_csv('produtos.csv')
print(tabela)


#define o tempo de espera entre os comandos do Pyautogui

pyautogui.PAUSE = 0.5

#abrir sistema (no nosso caso o chrome)
pyautogui.press("win") #Pressiona uma determinada tecla do teclado
pyautogui.write("chrome") #Escreve o conteúdo do argumento da função
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=791, y=532)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.click(x=955, y=700)

for linha in tabela.index: #Retorna o index de determiando elemento da tabela
    pyautogui.click()
    pyautogui.write(str(tabela.loc[linha, "codigo"])) #pega da tabela o elemento da linha atual e da coluna "código"
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.pres("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))

pyautogui.click()
pyautogui.scroll()




