class HomePage:
    def __init__(self, page):
        self.page = page

    def abrir_pesquisa(self):
        botao = self.page.get_by_role("button", name="Buscar no site")
        if botao.is_visible():
            botao.click()
            return True
        return False

    def pesquisar(self, texto):
        campo = self.page.get_by_role("textbox", name="Buscar")
        if campo.is_visible():
            campo.fill(texto)
            return True
        return False

    def confirmar_pesquisa(self):
        botao = self.page.get_by_role("button", name="Buscar", exact=True)
        if botao.is_visible():
            botao.click()
            return True
        return False
