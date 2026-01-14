import os
from pywinauto import Desktop
from pywinauto.findwindows import ElementNotFoundError

class AbrirPasta:
    def __init__(self, diretorio, tituloJanela):
        self.diretorio = diretorio
        self.titulo = tituloJanela

    def abrir_diretorio(self):
        try:
            if not os.path.isdir(self.diretorio):
                raise FileNotFoundError("Diretório não encontrado")

            os.startfile(self.diretorio)
            janela = Desktop(backend="uia").window(title_re=self.titulo)
            janela.set_focus()
            return True

        except Exception as e:
            print("Erro ao abrir diretório:", e)
            return False

    def fechar_diretorio(self):
        try:
            janela = Desktop(backend="uia").window(title_re=self.titulo)
            janela.close()
            return True
        except ElementNotFoundError:
            print("Janela do Explorer não encontrada")
            return False
        
      
