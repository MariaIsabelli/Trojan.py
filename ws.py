from bs4 import BeautifulSoup 
import requests 

site = requests.get(**site**).content 
#conteudo do site recebendo o conteudo da requisição http. 

soup =  BeautifulSoup(site, 'html.parser')
# soup esta baixando o html do site.

print(soup.prettify())
#transforma o html em string eo print exibi e html.
