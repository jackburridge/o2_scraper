from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/usr/lib/chromium/chromedriver")
driver.get("http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk")

countryName = driver.find_element_by_id("countryName")
countryName.clear()
countryName.send_keys("Canada")
countryName.send_keys(Keys.RETURN)