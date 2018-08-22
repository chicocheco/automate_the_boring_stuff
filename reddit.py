

from selenium import webdriver


browser = webdriver.Firefox()
browser.get('https://www.reddit.com/')
elem_user = browser.find_element_by_name('user')
elem_user.send_keys('chicocheco')
elem_user = browser.find_element_by_name('passwd')
elem_user.send_keys('tanicka21')
elem_user.submit()

