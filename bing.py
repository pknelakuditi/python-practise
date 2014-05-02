
import webbrowser

for  i in range(40):
 url='http://www.bing.com/search?setmkt=en-US&q=hello + %s'%i
 
 webbrowser.get('firefox').open(url)

