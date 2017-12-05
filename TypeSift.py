from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Test one - find via google
driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")

#maximize window
driver.maximize_window()

driver.get("http://www.google.com")
driver.find_element_by_name("q").send_keys("Type Sift")
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
driver.quit

#Test Two log in
driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")

driver.get("https://www.typesift.com/")
assert "TypeSift" in driver.title
driver.quit

driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")

#maximize window
driver.maximize_window()

driver.get("https://try.typesift.com/login")
assert "TypeSift" in driver.title

#username
driver.find_element_by_name("username").send_keys("lezs76@gmail.com")
#Password
driver.find_element_by_name("password").send_keys("Raining!1")
#Click Login
driver.find_element_by_xpath("/html/body/app/login/div[2]/div/div[3]/button").click()

if driver.current_url == "https://try.typesift.com/frontpage":
    print("Log in worked")
else:
    print("DID NOT WORK")


driver.quit 