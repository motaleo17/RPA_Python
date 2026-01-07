import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright
from browser.chrome import ChromeManager
from pages.home_page import HomePage
from pages.focus_page import FocusPage
from services.download_service import DownloadService

estado = 0
status = 100
data = sys.argv[1]
URL = sys.argv[2]

base_dir = Path(__file__).resolve().parent / "Relatorios" / data.replace("/", "-")
base_dir.mkdir(parents=True, exist_ok=True)
file_path = base_dir / "Relatorio_Focus.pdf"

with sync_playwright() as p:

    for _ in range(100):
        if estado == 0:
            print("Abrindo Chrome")
            chrome = ChromeManager(p)
            page = chrome.abrir(URL)
            if page:
                print("Chrome aberto com sucesso ...")
                estado = 1
            else:
                print("Erro na abertura do chrome")
                status = 11
                break

        elif estado == 1:
            print("Validando abertura e URL")
            if chrome.validar(URL):
                print("URL acessado com sucesso")
                estado = 2
            else:
                print(f"Erro ao acessar URL - {URL}")
                status = 22
                break

        elif estado == 2:
            print("Click na Lupa para iniciar pesquisa")
            home = HomePage(page)
            clicar_lupa = home.abrir_pesquisa()
            if clicar_lupa:
                estado = 3
            else:
                print(f"Erro ao clicar na lupa")
                status = 31
                break

        elif estado == 3:
            print("Digitando texto para pesquisar")
            digitar_texto = home.pesquisar("relatório de mercado")
            if digitar_texto:
                estado = 4
            else:
                print(f"Erro ao digitar texto na pesquisa")
                status = 31
                break

        elif estado == 4:
            print("Click botao pesquisar")
            click_pesquisar = home.confirmar_pesquisa()
            if click_pesquisar:
                estado = 5
            else:
                print(f"Erro ao clicar no botao para pesquisar")
                status = 31
                break

        elif estado == 5:
            print("Click link da pesquisa")
            focus = FocusPage(page)
            click_link = focus.abrir_resultado()
            if click_link:
                estado = 6
            else:
                print(f"Erro ao clicar no link da pesquisa")
                status = 31
                break

        elif estado == 6:
            print("Click no relatorio mais recente")
            click_relatorio = focus.abrir_relatorio()
            if click_relatorio:
                estado = 7
            else:
                print(f"Erro ao clicar no relatorio mais recente")
                status = 31
                break

        elif estado == 7:
            print("Obtendo link do href")
            link = focus.obter_link_pdf()
            if link:
                estado = 8
            else:
                print(f"Erro ao obter link")
                status = 31
                break

        elif estado == 8:
            print(f"Realizando Download")
            DownloadService.baixar_pdf(link, file_path)
            print("PDF salvo em:", file_path)
            status = 0
            break

        time.sleep(1)

    chrome.fechar()
    sys.exit(status)
