from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Scraper:
    def __init__(self):
        self.driver = webdriver.Chrome("/usr/lib/chromium/chromedriver")
        self.driver.get("http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk")

    def searchCountry(self, country):
        countryName = self.driver.find_element_by_id("countryName")
        countryName.clear()
        countryName.send_keys(country)
        countryName.send_keys(Keys.RETURN)
        # wait for tabs class to be set to unselectedtabs
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='tabs']/ul[contains(@class, 'unselectedtabs')]"))
        )

    def getLandlinePrice(self):
        paymonthly = self.driver.find_element_by_id("paymonthly")
        paymonthly.click()

        # waits for price to be visible before selecting it
        wait = WebDriverWait(self.driver, 10)
        landlinePrice = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='standardRatesTable']/tbody/tr[1]/td[2]"))
        )

        return landlinePrice.text


if __name__ == "__main__":
    s = Scraper()
    for country in ["Canada", "Germany", "Iceland", "Pakistan", "Singapore", "South Africa"]:
        s.searchCountry(country)
        price = s.getLandlinePrice()
        print "Country:", country, ",Price:", price
