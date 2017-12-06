from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")
 
 #maximize window
driver.maximize_window()

driver.get("https://try.typesift.com/login")
assert "TypeSift" in driver.title
