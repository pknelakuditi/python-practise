from bs4 import BeautifulSoup
import requests

url="http://stanford.edu/class/archive/cs/cs106b/cs106b.1142/lectures.shtml"
resp=requests.get(url)
b=BeautifulSoup(resp.content) 
print b.prettify
