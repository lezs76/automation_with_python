from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")


#maximize window
driver.maximize_window()

driver.get("https://try.typesift.com/login")
assert "TypeSift" in driver.title



#Check Request a licance is on the page
if driver.find_element_by_xpath("/html/body/app/login/div[2]/div/div[4]/a"):
    print("Button is there")
else:
    print("No button")


#username
driver.find_element_by_name("username").send_keys("lezs76@gmail.com")
#Password
driver.find_element_by_name("password").send_keys("Raining!1")
#Click Login
driver.find_element_by_xpath("/html/body/app/login/div[2]/div/div[3]/button").click()

time.sleep(10)

if driver.current_url == "https://try.typesift.com/frontpage":
  driver.get_screenshot_as_file("C:\Users\lezs7\Documents\SeleniumScripts\screenshot\LPS_good_url.png")
# print("Log in worked")
else:
#  print("DID NOT WORK")
    driver.get_screenshot_as_file("C:\Users\lezs7\Documents\SeleniumScripts\screenshot\LPS_bad_url.png")

#enter test in the search box and click enter "\n" = enter
driver.find_element_by_id("top-search-box").send_keys("Total" + "\n")


if driver.find_elements_by_xpath("//*[contains(text(), 'Total')]"):
    driver.get_screenshot_as_file("C:\Users\lezs7\Documents\SeleniumScripts\screenshot\LPS_Total_On_Page.png")
else:
     driver.get_screenshot_as_file("C:\Users\lezs7\Documents\SeleniumScripts\screenshot\LPS_Total_NOT_On_page.png")