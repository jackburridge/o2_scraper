from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Scraper:
    def __init__(self):
        self.driver = webdriver.Chrome("/usr/lib/chromium/chromedriver")
        self.driver.get("http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk")
        self.driver.implicitly_wait(2)


    def searchCountry(self,country):
        countryName = self.driver.find_element_by_id("countryName")
        countryName.clear()
        countryName.send_keys(country)
        countryName.send_keys(Keys.RETURN)
        time.sleep(1)


    def getLandlinePrice(self):
        paymonthly = self.driver.find_element_by_id("paymonthly")
        paymonthly.click()

        landlinePrice = self.driver.find_element_by_xpath("//*[@id=\"standardRatesTable\"]/tbody/tr[1]/td[2]")
        time.sleep(1)
        return landlinePrice.text

if __name__ == "__main__":
    s = Scraper()
    for country in ["Canada","Germany", "Iceland", "Pakistan", "Singapore", "South Africa"]:
        s.searchCountry(country)
        price = s.getLandlinePrice()
        print "Country:", country
        print "Price:" ,price