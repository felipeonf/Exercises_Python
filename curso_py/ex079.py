import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.request.URLError:
    print('O site pudim não está disponível no momento!')
else:
    print('Consegui acessar o site pudim com sucesso!')