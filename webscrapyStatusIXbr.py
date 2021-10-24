from bs4 import BeautifulSoup
import requests

html = requests.get("https://status.ix.br").content
soup = BeautifulSoup(html, "html.parser")

servico = soup.find_all('div', class_='group-items hide')

name_ix0 = servico[0].li.text.strip()
name_ix1 = servico[1].li.text.strip()
name_ix2 = servico[2].li.text.strip()
name_ix3 = servico[3].li.text.strip()
print(name_ix0[:41], ":", servico[0].li.small.text)
print(name_ix1[:43], ":", servico[1].li.small.text)
print(name_ix2[:41], ":", servico[2].li.small.text)
print(name_ix3[:17], ":", servico[3].li.small.text)
