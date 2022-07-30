from getpass import getpass
from selenium import webdriver
# importing useful packages.

username = input("Enter you username:-")
password = getpass("Enter your Password:-")

driver = webdriver.Chrome('C:\gitsem2\COMP593-Lab6\chromedriver.exe')
driver.get("https://www.one-key.gov.on.ca/iaalogin/IAALogin.jsp")

driver.maximize_window()

username_textbox = driver.find_element_by_name('ldap_user')
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_name('ldap_password')
password_textbox.send_keys(password)

login_button = driver.find_element_by_name('Login')
login_button.submit()

driver.get("https://forms.mgcs.gov.on.ca/en/dataset/026-0178")

download = driver.find_elements_by_class_name('btn btn-primary resource-url-analytics resource-type-None resource-list-download-button')
driver.find_element_by_link_text('Download').click()