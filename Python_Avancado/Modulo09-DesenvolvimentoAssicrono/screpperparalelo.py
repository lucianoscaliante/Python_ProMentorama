# importando as bibliotecas Multiprocessing
from multiprocessing import Pool

# importando a biblioteca BS4 e a Resquests como metodo get
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


# função para scraper paralelo
def Scraper_paralelo(urls):
    resposta = get(urls)
    tag = BeautifulSoup(resposta.text, "html5lib")
    titulo = tag.find("title")
    print('Pagina pesquisada foi: ', titulo.text)


# iniciando as funções do scraper
paralelo = Pool(10)
paralelo.map(Scraper_paralelo, urls)
paralelo.terminate()
paralelo.join()
