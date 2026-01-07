import requests

class DownloadService:
    @staticmethod
    def baixar_pdf(url, file_path):
        response = requests.get(url)
        response.raise_for_status()

        with open(file_path, "wb") as f:
            f.write(response.content)
