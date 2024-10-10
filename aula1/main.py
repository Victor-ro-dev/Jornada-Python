# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
from time import sleep
import pandas as pd

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.3

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=686, y=425)

# entrar no link 
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
sleep(3)

# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=518, y=405)
# escrever o seu email
email = "pythonimpressionador@gmail.com"
pyautogui.write(email)
pyautogui.press("tab") # passando pro próximo campo
senha = "vtx123"
pyautogui.write(senha)
pyautogui.press("tab") # passando pro próximo campo
pyautogui.press("enter") # clique no botao de login
sleep(3)
pyautogui.click(x=1081, y=109) # fechar salvamento automático
sleep(2)

# Passo 3: Importar a base de produtos pra cadastrar
tabela = pd.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=474, y=287)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim






