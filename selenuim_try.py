from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()
print(type(browser))
browser.get('https://inventwithpython.com')
#browser.refresh()
link_elem = browser.find_element(By.LINK_TEXT, 'Bookshop.org')
print(type(link_elem))
print(link_elem.location)
link_elem.click()

#part 2 filling out forms

browser.get('https://autbor.com/example3.html')
user_elem = browser.find_element(By.ID, 'login_user')
user_elem.send_keys('university2019')
password_elem = browser.find_element(By.ID, 'login_pass')
password_elem.send_keys('carrot1.')
check_elem = browser.find_element(By.CSS_SELECTOR, 'input[type = checkbox]')
check_elem.click()
check_elem.submit()

