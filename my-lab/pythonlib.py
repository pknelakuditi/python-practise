
url='https://docs.python.org/2/library/index.html'

from bs4 import BeautifulSoup
import requests


resp=requests.get(url)
b=BeautifulSoup(resp.content) 
link=b.find_all('li','toctree-l2')
for i in link:
 print i.get_text()
 """giving a error while >output.txt:UnicodeEncodeError: 'ascii' codec can't encode character u'\xe9' in position 7: ordinal not in range(128) """
