from pywinauto.findwindows import ElementNotFoundError
from pywinauto.timings import TimeoutError

class ValidaJanela:

    def __init__(self, app, title_re):
        self.app = app
        self.title_re = title_re

    def ativar_janela(self, timeout=20):
        """
        Localiza a janela pelo título, aguarda ficar visível,
        tenta ativá-la e valida se está ativa.
        Retorna o objeto da janela ou None em caso de falha.
        """
        try:
            janela = self.app.window(title_re=self.title_re)
            janela.wait("visible", timeout=timeout)

            if janela.is_minimized():
                janela.restore()

            janela.set_focus()

            if janela.is_active():
                return janela

            return None

        except (ElementNotFoundError, TimeoutError):
            return None