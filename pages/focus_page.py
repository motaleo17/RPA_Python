class FocusPage:
    def __init__(self, page):
        self.page = page

    def abrir_resultado(self):
        link = self.page.get_by_role(
            "link", 
            name="Focus - Relatório de Mercado"
        ).first

        try:
            # Ele vai tentar esperar o elemento ficar visível por até 5 segundos (5000ms)
            link.wait_for(state="visible", timeout=60000)
            link.click()
            return True
        except Exception as e:
            print(f"O link não apareceu no tempo esperado: {e}")
            return False

    def abrir_relatorio(self):
        link = self.page.get_by_role(
            "link",
            name="Relatório de Mercado"
        ).first

        try:
            link.wait_for(state="visible", timeout=60000)
            link.click()
            return True
        except Exception as e:
            print(f"O relatorio nao apareceu no tempo esperado: {e}")
            return False

    def obter_link_pdf(self):
        link = self.page.get_by_role("link", name="Baixar (pdf)")

        try:
            link.wait_for(state="visible", timeout=60000)
            print(f"link capturado: {link.get_attribute("href")}")
            return link.get_attribute("href")
        except Exception as e:
            print(f"Nao foi possivel capturar o href: {e}")
            return false
