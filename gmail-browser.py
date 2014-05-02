
 
import webbrowser
from urllib import urlencode

credentials = {
    'username': 'pavannelakuditi',
    'password': 'nkpmv2011'}
url = "https://accounts.google.com/ServiceLogin?service=mail&continue=https://mail.google.com/mail/" + urlencode(credentials)



webbrowser.get('firefox').open(url)


