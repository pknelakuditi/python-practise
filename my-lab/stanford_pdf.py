from bs4 import BeautifulSoup
import urllib2
import requests
opener=urllib2.urlopen("http://stanford.edu/class/archive/cs/cs106b/cs106b.1142/lectures.shtml")

doc=opener.read()
ob=BeautifulSoup(doc)
lst=[]
for link in ob.find_all('a'):
	lst.append(link.get('href')) 
ls=[]
for i in lst:
	if 'pdf' in i:
		ls.append(i)
		
#print ls

def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url)
    with open(local_filename, 'wb') as f:
       
                f.write(r.content)
                f.flush()
    return local_filename
  
for i in ls:  
  download_file("http://stanford.edu/class/archive/cs/cs106b/cs106b.1142/"+i)
