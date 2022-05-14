from bs4 import  BeautifulSoup
import requests
url="https://devilnovels.com/chaotic-sword-god/chaotic-sword-god-csg-capitulo-1"
pagina = requests.get(url)
soup =BeautifulSoup(pagina.content, 'html.parser')
print(soup.get_text())