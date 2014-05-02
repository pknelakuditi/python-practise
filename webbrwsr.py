'''import os
try:
 os.system('/usr/bin/google-chrome')
except Exception:
 pass'''
 
import webbrowser
url = 'http://docs.python.org/'
url2='http://google.com'

#webbrowser.open(url, new=0, autoraise=True)

webbrowser.get('firefox').open('http://www.google.com')
print "get,open"
#name='mozilla'
#webbrowser.register(name, constructor, instance=None)


#webbrowser.open_new(url)

