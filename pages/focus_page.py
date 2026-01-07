class FocusPage:
    def __init__(self, page):
        self.page = page

    def abrir_resultado(self):
        link = self.page.get_by_role(
            "link",
            name="Focus - Relatório de Mercado"
        ).first

        if link.is_visible():
            link.click()
            return True
        return False

    def abrir_relatorio(self):
        link = self.page.get_by_role(
            "link",
            name="Relatório de Mercado"
        ).first

        if link.is_visible():
            link.click()
            return True
        return False

    def obter_link_pdf(self):
        link = self.page.get_by_role("link", name="Baixar (pdf)")
        if link.is_visible():
            return link.get_attribute("href")
        return None
