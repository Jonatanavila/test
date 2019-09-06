from urllib.request import urlopen 
from bs4 import BeautifulSoup

var= "games"
url="http://gen.lib.rus.ec/search.php?req="+var+"&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def"
documento=urlopen(url)

sopa= BeautifulSoup(documento.read(),'lxml')
listadeFilas=sopa.findAll("tr")
print (listadeFilas[3].get_text())
