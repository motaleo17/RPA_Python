import sys
from pywinauto import Application
import pyautogui
from pywinauto.findwindows import ElementNotFoundError
from conf import conf, controles
from pages.validaJanela import ValidaJanela
from datetime import datetime


pyautogui.PAUSE = 1 # Pausa entre comandos
pyautogui.FAILSAFE = True # Se mover o mouse para o canto da tela, o script para

#janela.print_control_identifiers()

estado = 0
status = 100
i = 0
data = "08/01/2026"


print("Iniciando Processamento")

while i < 100:
    print("estado - ", estado)
    if (estado == 0):
        print("Verificando se a aplicação já está aberta...")
        try:
            app = Application(backend="win32").connect(title_re=conf.janelaPrincipal)
            print("Aplicação já aberta")
            estado = 1
        except ElementNotFoundError:
            print("Aplicação não encontrada, abrindo...")
            app = Application(backend="win32").start(conf.atalho)
            estado = 1
    elif (estado == 1):
        validaPrincipal = ValidaJanela(app, conf.janelaPrincipal)
        janelaPrincipal = validaPrincipal.ativar_janela()
        if (janelaPrincipal):
            print(f"Janela ativa - {janelaPrincipal}")
            botao = janelaPrincipal.child_window(title=controles.NumeroUm, class_name="Button")
            if botao.exists(timeout=5):
                print("Botão existe, efetuando clique")
                botao.click()
                estado = 2
            else:
                print("Botão não existe")
                break
            estado = 2
        else:
            print("Nao foi possivel ativar a janela")
            status = 10
            break
    elif (estado == 2):
        validaBotaoUm = ValidaJanela(app, conf.janelaBotaoUm)
        janelaBotaUm = validaBotaoUm.ativar_janela()
        if (janelaBotaUm):
            print("Janela ativa")
            botao = janelaBotaUm.child_window(title="OK", class_name="Button")
            if botao.exists(timeout=5):
                print("Botão existe, efetuando clique")
                botao.click()
                estado = 3
            else:
                print("Botão não existe")
                break
        else:
            print("Nao foi possivel ativar a janela")
            status = 10
            break
    elif (estado == 3):
        if (janelaPrincipal):
            botao = janelaPrincipal.child_window(control_id=controles.data)
            if botao.exists(timeout=5):
                print(f"Inserindo data: {data}")
                campo_data = janelaPrincipal.child_window(control_id=controles.data)
                campo_data.click_input(coords=(10, 15))
                pyautogui.write(data, interval=0.1)
                estado = 4
            else:
                print("Botão não existe")
                break
        else:
            print("Nao foi possivel ativar a janela")
            status = 10
            break     
    elif (estado == 4):
        if (janelaPrincipal):
            print("Janela ativa")
            botao = janelaPrincipal.child_window(class_name=controles.TabProdutos)
            if botao.exists(timeout=5):
                print("Aba existe, ativando aba produtos")
                botao.select("Produtos")
                estado = 5
            else:
                print("Aba Produtos não existe")
                break
        else:
            print("Nao foi possivel ativar a janela - ", conf.janelaPrincipal)
            status = 10
            break
    elif (estado == 5):
        if (janelaPrincipal):
            print("Janela ativa")
            botao = janelaPrincipal.child_window(control_id=controles.CheckBox1)
            if botao.exists(timeout=5):
                print("Check Box 1 existe, validando se esta marcado")
                if botao.is_checked():
                    print("Check Box esta marcando")
                else:
                    print("Check box esta desmarcado, click para marcar")
                    botao.click_input()
                estado = 6
                break
            else:
                print("Botão Produtos não existe")
                break
        else:
            print("Nao foi possivel ativar a janela - ", conf.janelaPrincipal)
            status = 10
            break
    #elif (estado == 5):
    i+=1
        
sys.exit(0)
