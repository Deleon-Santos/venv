import requests
from bs4 import BeautifulSoup

url_base = 'https://mercadolivre.com.br/'

produto = input('Qual o item você deseja pesquisar? ')

response = requests.get(url_base + produto )
if response.status_code == 200:
    # Processe o conteúdo da página
    soup = BeautifulSoup(response.text, 'html.parser')
else:
    print(f"Erro ao acessar a página: {response.status_code}")

site = BeautifulSoup(response.text, 'html.parser')

produto = site.find('div', attrs={'class': 'ui-search-result__content'})
if produto is not None:
    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})
else:
    print("Produto não encontrado")
titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})
link = produto.find('a', attrs={'class': 'ui-search-link'})

# Verificando se o preço existe
real = produto.find('span', attrs={'class': 'price-tag-fraction'})
centavos = produto.find('span', attrs={'class': 'price-tag-cents'})

# Se não tiver centavos, coloca 00
if centavos:
    preco = real.text + "," + centavos.text
else:
    preco = real.text + ",00"

# Exibindo as informações
print('Título do produto:', titulo.text)
print('Link do produto:', link['href'])
print('Preço do produto: R$', preco)
