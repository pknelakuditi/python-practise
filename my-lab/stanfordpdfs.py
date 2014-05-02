import urllib
import re
opener = urllib.FancyURLopener({})

day=[]

def readme(url):
 count=1
 f = opener.open(url)
 files= f.read()
 links=re.findall(r'\d\d-\d\d',files)

 for i in links:
            #urllib.urlretrieve(i,str(count)+".zip")
            #print i
            if i not in day:
		
	        print  "cool"
		day.append(i)
            count+=1
 for i in day:
  print "links"
  print i


readme("http://stanford.edu/class/archive/cs/cs106b/cs106b.1142/lectures/")
