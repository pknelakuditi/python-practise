from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
#import time,unitest

username='kumardas1@outlook.com'
password='FuckingHell'



browser = webdriver.Firefox() # Get local session of firefox
url="https://login.live.com/"

browser.get(url) # Load page
#assert "miscrosoft" in browser.title
elem = browser.find_element_by_name("idDiv_PWD_UsernameTb") # Find the query box

"""find_element_by_xpath
find_element_by_css_selector
find_element_by_class_name
find_element_by_link_text"""
elem.send_keys(username + Keys.RETURN)



elem = browser.find_element_by_name(password+"idDiv_PWD_PasswordTb")
elem.send_keys(password + Keys.RETURN)


"""time.sleep(0.2) # Let the page load, will be added to the API
try:
    browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
except NoSuchElementException:
    assert 0, "can't find seleniumhq" """
    
signin=driver.find_element_by_id("idTd_PWD_SubmitCancelTbl")
signin.click()

#browser.close()
#print dir(webdriver)
# ./go //py:firefox_test:run
