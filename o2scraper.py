from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class O2Scraper:
    def __init__(self):
        self.driver = webdriver.Chrome("/usr/lib/chromium/chromedriver")
        self.driver.get("http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk")

    def search_country(self, country):
        country_name = self.driver.find_element_by_id("countryName")
        country_name.clear()
        country_name.send_keys(country)
        country_name.send_keys(Keys.RETURN)
        # wait for tabs class to be set to unselectedtabs
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='tabs']/ul[contains(@class, 'unselectedtabs')]"))
        )

    def get_landline_price(self):
        pay_monthly = self.driver.find_element_by_id("paymonthly")
        pay_monthly.click()

        # waits for price to be visible before selecting it
        wait = WebDriverWait(self.driver, 10)
        landline_price = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='standardRatesTable']/tbody/tr[1]/td[2]"))
        )

        return landline_price.text

    def get_country_landline_price(self, country):
        self.search_country(country)
        return self.get_landline_price()

    def close(self):
        self.driver.close()


if __name__ == "__main__":
    s = O2Scraper()
    for country in ["Canada", "Germany", "Iceland", "Pakistan", "Singapore", "South Africa"]:
        print "Country:", country, ",Price:", s.get_country_landline_price(country)
    s.close()
