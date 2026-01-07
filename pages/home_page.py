class HomePage:
    def __init__(self, page):
        self.page = page

    def abrir_pesquisa(self):
        botao = self.page.get_by_role("button", name="Buscar no site")
        try:
            botao.wait_for(state="visible", timeout=60000)
            botao.click()
            return True
        except Exception as e:
            print(f"Botao da lupa nao foi encontrado: {e}")
            return False

    def pesquisar(self, texto):
        campo = self.page.get_by_role("textbox", name="Buscar")
        try:
            campo.wait_for(state="visible", timeout=60000)
            campo.fill(texto)
            return True
        except Exception as e:
            print(f"Campo de preencher a pesquisa nao foi identificado: {e}")
            return False

    def confirmar_pesquisa(self):
        botao = self.page.get_by_role("button", name="Buscar", exact=True)
        try:
            botao.wait_for(state="visible", timeout=60000)
            botao.click()
            return True
        except Exception as e:
            print(f"Campo de preencher a pesquisa nao foi identificado: {e}")
            return False
      
