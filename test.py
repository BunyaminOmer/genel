import requests

class TargetSite:
    def __init__(self, url):
        self.url = url

    @property
    def url_bilgisi(self):
        return self.url

    @property
    def request_method(self):
        return 'HTTPS'

class RequestService:
    def __init__(self, urller):
        self.urller = urller

    def istekleri_yap(self):
        for url in self.urller:
            # Her bir hedef sitesi için istek yap
            target_site = TargetSite(url)
            response = requests.get(target_site.url_bilgisi)
            
            # Yanıt içeriğini ekrana yazdır
            print(f"Hedef Site: {target_site.url_bilgisi}")
            print(f"Request Method: {target_site.request_method}")
            print(f"Yanıt İçeriği:\n{response.text}\n")

# Kullanım örneği:
urller = ("https://www.w3schools.com", "https://www.deneme.com")
request_service = RequestService(urller)
request_service.istekleri_yap()