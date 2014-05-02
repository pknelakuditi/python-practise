
import webbrowser

for  i in range(45):
 url='http://www.bing.com/search?setmkt=en-US&q=hello + %s'%i
 
 webbrowser.open(url)

