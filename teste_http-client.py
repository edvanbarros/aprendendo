import requests
import socket

url_user = input("Digite a URL: ")
url_user.replace("http","https")
site = requests.get(url_user)
remote_host = url_user.split("//")
ipaddr = socket.gethostbyname(remote_host[1])

print('URL:', site.url)
print('IP Address:', ipaddr,)
print('Tempo de Resposta:', site.elapsed.total_seconds())
print('Status HTTP:', site.status_code)
print('Server:', site.headers.get('Server'))