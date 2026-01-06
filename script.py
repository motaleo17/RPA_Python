import sys
from pywinauto import Application
from pywinauto.findwindows import ElementNotFoundError
from conf import conf

estado = 0
i = 0

print("Iniciando Processamento")

while i < 100:
    if estado == 0:
        print("Verificando se a aplicação já está aberta...")
        try:
            app = Application(backend="uia").connect(title_re=conf.janelaPrincipal)
            print("Aplicação já aberta")
            estado = 1
        except ElementNotFoundError:
            print("Aplicação não encontrada, abrindo...")
            app = Application(backend="uia").start(conf.atalho)
            estado = 1

    elif estado == 1:
        janela = app.window(title_re=conf.janelaPrincipal)
        janela.wait("visible", timeout=20)
        janela.set_focus()

        if janela.is_active():
            print("Janela ativa")
            estado = 2

    elif estado == 2:
        botao = janela.child_window(auto_id="3", control_type="Button")

        if botao.exists(timeout=5):
            print("Botão existe, efetuando clique")
            botao.click()
        else:
            print("Botão não existe")

        break

    i += 1

sys.exit(0)
