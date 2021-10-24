from bs4 import BeautifulSoup
import requests

html = requests.get("https://status.ix.br").content
soup = BeautifulSoup(html, "html.parser")

servico = soup.find_all("li", class_='list-group-item sub-component')

for i in range(len(servico)):
    name_ix = servico[i].text.strip()
    print(servico[i].text.strip().strip("Operacional").strip("Matriz de Comutação - ").strip(), ":", servico[i].div.text.strip().replace(" ", ""))
