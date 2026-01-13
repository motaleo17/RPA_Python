class HomePage:
    def __init__(self, page):
        self.page = page

    def abrir_pesquisa(self):
        botao = self.page.get_by_role("button", name="Buscar no site")
        botao2 = self.page.get_by_role("button", name="Fechar")

        if botao.count() > 0:
            botao.wait_for(state="visible", timeout=60000)
            botao.click()
            return True

        elif botao2.count() > 0:
            botao2.wait_for(state="visible", timeout=60000)
            botao2.click()
            return True

        else:
            print("Nenhum botão de pesquisa foi encontrado")
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
      
