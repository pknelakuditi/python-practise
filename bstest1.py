from bs4 import BeautifulSoup
import urllib2

opener=urllib2.urlopen("http://www.atozmp3.in/")

doc=opener.read()
ob=BeautifulSoup(doc)

#print ob.__doc__

#print ob.prettify()

#print ob.title
#print ob.title.name

#print ob.find_all('a')
#print ob.a
#print ob.find(rel="bookmark")
#print(ob.get_text()) #extracting text
"""import urllib2
mp3file = urllib2.urlopen("http://www.example.com/songs/mp3.mp3")
output = open('test.mp3','wb')
output.write(mp3file.read())
output.close()"""

for link in ob.find_all(rel="bookmark"):
	print link.get('href')
