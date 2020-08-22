import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com')
except urllib.error.URLError:
    print('erro')
else:
    print('Tudo Ok')
    print(site.read()) #ler o site


