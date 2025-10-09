# We have multiple locators available in Selenium to identify the elements in the web page.
# ID, Name, Class Name, Tag Name, Link Text, Partial Link Text, CSS Selector, XPATH
# We can use any of these locators to identify the elements in the web page.
# But we should use the locators in the following order:
# ID > Name > CSS Selector > XPATH
# We should avoid using Class Name, Tag Name, Link Text, Partial Link Text as they are not reliable.
# We should use the locators which are unique and stable.
# We should avoid using the locators which are dynamic and change frequently.
import time

from selenium import webdriver
from selenium.webdriver.ie.service import Service


# To check the locators I am using rahulshettyacademy website. And will be using all the locators available in selenium.

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/locatorspractice/")
time.sleep(3)



