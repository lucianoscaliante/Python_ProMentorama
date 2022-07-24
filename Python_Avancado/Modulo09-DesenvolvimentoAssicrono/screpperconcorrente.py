# importando bibliotecas
from asyncio import coroutine, get_event_loop
from time import time

from bs4 import BeautifulSoup
from requests import get

# variaveis para as urls
urls = ["https://www.mercadolivre.com.br/",
        "https://www.mercadolivre.com.br/ofertas/",
        "https://www.mercadolivre.com.br/c/calcados-roupas-e-bolsas/",
        "https://www.mercadolivre.com.br/c/animais",
        "https://www.mercadolivre.com.br/c/acessorios-para-veiculos/",
        "https://www.mercadolivre.com.br/c/agro/",
        "https://www.mercadolivre.com.br/c/antiguidades-e-colecoes/",
        "https://www.mercadolivre.com.br/c/calcados-roupas-e-bolsas/",
        "https://www.mercadolivre.com.br/c/alimentos-e-bebidas/",
        "https://www.mercadolivre.com.br/c/bebes/"
        ]


# função para realizar o screper concorrente
def scraper_concorrente():
    @coroutine
    def Web_scraper():
        loop = get_event_loop()
        lista_scraper = [loop.run_in_executor(None, get, url) for url in urls]
        print('Site de screpy Marcado Livre!')
        for scrape in lista_scraper:
            resposta = yield from scrape
            tag = BeautifulSoup(resposta.text, "html5lib")
            titulo = tag.find("title")
            print('Pagina pesquisada foi: ', titulo.text)

    loop = get_event_loop()
    loop.run_until_complete(Web_scraper())


# função de scraper comum
def screper_comun():
    for url in urls:
        print(get(url).ok)


start = time()
scraper_concorrente()
print(f"tempo total: {abs(int(time() - start))}")
