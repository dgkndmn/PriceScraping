import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestPriceComparison(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_pricecomparison(self):
        self.driver.maximize_window()

        self.driver.get("https://trendyol.com")
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located((By.ID, "onetrust-accept-btn-handler")))
        cookie_button = self.driver.find_element(By.ID, 'onetrust-accept-btn-handler')
        ActionChains(self.driver).move_to_element(cookie_button).click(cookie_button).perform()
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "V8wbcUhU")))
        searchbar = self.driver.find_element(By.CLASS_NAME, "V8wbcUhU")
        searchbar.click()
        searchbar.send_keys("iphone 15")
        searchbar.send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "prc-box-dscntd")))
        trendyol_price = self.driver.find_element(By.CLASS_NAME, "prc-box-dscntd")
        trendyol_phone = self.driver.find_element(By.CLASS_NAME, "prdct-desc-cntnr-name.hasRatings")
        print(f"Trendyol --> {trendyol_phone.text}: {trendyol_price.text}")


        self.driver.get("https://www.hepsiburada.com/ara?q=iphone+15")
        try:
            WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '[data-test-id="price-current-price"]')))
            WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '[data-test-id="product-card-name"]')))
        except Exception as e:
            print(f"Error waiting for elements {e}")
            self.driver.quit()

        hepsiburada_price = self.driver.find_elements(By.CSS_SELECTOR, '[data-test-id="price-current-price"]')
        hepsiburada_phone = self.driver.find_elements(By.CSS_SELECTOR, '[data-test-id="product-card-name"]')
        hepsiburada_phonedict = {}

        for i in range(len(hepsiburada_phone)):
            phone_name = hepsiburada_phone[i].text
            phone_price = hepsiburada_price[i].text
            hepsiburada_phonedict[phone_name] = phone_price

        for name, price in hepsiburada_phonedict.items():
            if "iPhone 15 128 GB" in name:
                print(f"Hepsiburada --> {name}: {price}")
                break





        self.driver.get("https://www.mediamarkt.com.tr/tr/search.html?query=iphone%2015&t=1722592363779&queryMeta%5Bga_query%5D=iphone%2015&queryMeta%5BqueryHash%5D=72954355f77c68b8a94b2b2f7994a2c6d34f0bcaea1cfa5d76169f9ca842dcac&queryMeta%5BqueryRequestId%5D=72954355f77c68b8a94b2b2f7994a2c6d34f0bcaea1cfa5d76169f9ca842dcac")
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "sc-3f2da4f5-0.fLePRG")))
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "sc-3f2da4f5-0.dievjx.sc-dd1a61d2-2.efAprc")))
        mm_phonename = self.driver.find_elements(By.CLASS_NAME, "sc-3f2da4f5-0.fLePRG")
        mm_phoneprice = self.driver.find_elements(By.CLASS_NAME, "sc-3f2da4f5-0.dievjx.sc-dd1a61d2-2.efAprc")
        phonedict = {}
        for i in range(len(mm_phonename)):
            phone_name = mm_phonename[i].text
            phone_price = mm_phoneprice[i].text
            phonedict[phone_name] = phone_price

        for name, price in phonedict.items():
            if "iPhone 15 128 GB" in name:
                print(f"Mediamarkt --> {name}: {price}")
                break


        self.driver.get("https://teknosa.com")
        WebDriverWait(self.driver, 120).until(expected_conditions.visibility_of_element_located((By.ID, "search-input")))
        searchbar = self.driver.find_element(By.ID, "search-input")
        searchbar.send_keys("iphone 15")
        searchbar.send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 120).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "prc.prc-last")))
        teknosa_price = self.driver.find_element(By.CLASS_NAME, "prc.prc-last")
        teknosa_phone = self.driver.find_element(By.CLASS_NAME, "prd-title.prd-title-style")
        print(f"Teknosa --> {teknosa_phone.text}: {teknosa_price.text}")





    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
