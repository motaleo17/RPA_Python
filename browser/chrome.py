class ChromeManager:
    def __init__(self, playwright):
        self.playwright = playwright
        self.browser = None
        self.context = None
        self.page = None

    def abrir(self, url):
        self.browser = self.playwright.chromium.launch(
            headless=False,
            args=["--start-maximized"]
        )
        self.context = self.browser.new_context(
            no_viewport=True,
            accept_downloads=True
        )
         # Adiciona o cookie de consentimento
        self.context.add_cookies([
            {
                "name": "bcb-aceitacookiev2",
                "value": "%7Bnecessary%3A%20true%2C%20performance%3A%20true%2C%20marketing%3A%20true%7D",
                "domain": ".bcb.gov.br",
                "path": "/"
            }
        ])
        self.page = self.context.new_page()

        self.page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=60000
        )
        return self.page

    def validar(self,url):
        return self.browser.is_connected() and url in self.page.url

    def fechar(self):
        if self.browser:
            self.browser.close()
