import csv 
import requests
from bs4 import BeautifulSoup

# URL da página que queremos fazer scraping
url = "https://www.imdb.com/chart/top/"


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

# Conexão: Enviar uma solicitação GET para a URL
response = requests.get(url, headers=headers)

# Verificar se a solicitação foi bem-sucedida (status 200)
if response.status_code == 200:
    # Parse a página com o BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Encontre os elementos HTML que contêm os títulos de notícias
    imdbs = soup.find_all("div", class_="sc-b85248f1-0 bCmTgE cli-children")
    
    # Crie arquivo CSV
    file = open('export_data.csv', 'w', newline='', encoding='utf-8')
    writer = csv.writer(file)
    headers = ['Nome do Filme', 'Ano de Produção', 'Nota do Filme']
    writer.writerow(headers)
    
    # Loop pelos elementos e imprimir os títulos
    for imdb in imdbs:
        # Extrair o título do filme
        title = imdb.find("h3", class_="ipc-title__text").text.strip()
        
        # Extrair o ano de produção do filme
        year = imdb.find("span", class_="sc-b85248f1-6 bnDqKN cli-title-metadata-item").text.strip()
                
        # Extrair a nota do filme
        stars = imdb.find("span", class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating").text.strip()
        
        # Escrever as informações no arquivo CSV
        row = [title, year, stars]
        writer.writerow(row)
        
    file.close()
    print("Dados exportados para export_data.csv.")

else:
    print("Falha ao acessar a página:", response.status_code)
