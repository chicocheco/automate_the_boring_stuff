from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('http://nostarch.com')
html_elem = browser.find_element_by_tag_name('html')
html_elem.send_keys(Keys.END)     # scrolls to bottom
# html_elem.send_keys(Keys.HOME)    # scrolls to from_top
