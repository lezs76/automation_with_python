from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")


#maximize window
driver.maximize_window()

driver.get("https://try.typesift.com/login")
assert "TypeSift" in driver.title

#Check Request a licance is on the page
driver.find_element_by_xpath("/html/body/app/login/div[2]/div/div[4]/a")
print("Request a licance is there")

#username

driver.find_element_by_name("username").send_keys("lezs76@gmail.com")
#Password
driver.find_element_by_name("password").send_keys("Raining!1")
#Click Login
driver.find_element_by_xpath("/html/body/app/login/div[2]/div/div[3]/button").click()

time.sleep(10)

if driver.current_url == "https://try.typesift.com/frontpage":
   print("Log in worked")
else:
    print("DID NOT WORK")
driver.get_screenshot_as_file("C:\Users\lezs7\Documents\SeleniumScripts\screenshot\LPS_bad_url.png")

#enter test in the search box and click enter "\n" = enter
driver.find_element_by_id("top-search-box").send_keys("Total" + "\n")

#driver.find_element_by_class_name("chart-title")

if driver.page_source.contains("Total Sales"):
    print("Total Sales on page")
else:
    print("Total Sales NOT on page")

