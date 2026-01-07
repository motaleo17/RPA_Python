import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright
from browser.chrome import ChromeManager
from pages.home_page import HomePage
from pages.focus_page import FocusPage
from services.download_service import DownloadService

estado = 0
data = sys.argv[1]
URL = sys.argv[2]

base_dir = Path(__file__).resolve().parent / "Relatorios" / data.replace("/", "-")
base_dir.mkdir(parents=True, exist_ok=True)
file_path = base_dir / "Relatorio_Focus.pdf"

with sync_playwright() as p:
    chrome = ChromeManager(p)

    for _ in range(100):
        if estado == 0:
            page = chrome.abrir(URL)
            estado = 1

        elif estado == 1:
            if chrome.validar():
                home = HomePage(page)
                estado = 2

        elif estado == 2:
            if home.abrir_pesquisa():
                estado = 3

        elif estado == 3:
            if home.pesquisar("relatório de mercado"):
                estado = 4

        elif estado == 4:
            if home.confirmar_pesquisa():
                focus = FocusPage(page)
                estado = 5

        elif estado == 5:
            if focus.abrir_resultado():
                estado = 6

        elif estado == 6:
            if focus.abrir_relatorio():
                estado = 7

        elif estado == 7:
            link = focus.obter_link_pdf()
            if link:
                estado = 8

        elif estado == 8:
            DownloadService.baixar_pdf(link, file_path)
            print("PDF salvo em:", file_path)
            break

        time.sleep(1)

    chrome.fechar()
