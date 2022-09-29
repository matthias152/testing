import unittest
from selenium import webdriver
import page
from sample_text import sampletext
import time


class Order(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://turbotlumaczenia.pl/")

    def test_check_price_and_time(self):
        main_page = page.MainPage(self.driver)
        main_page.click_enter_button()

        order_page = page.OrderPage(self.driver)
        order_page.change_options()
        order_page.text_field = sampletext
        time.sleep(5)

        est_time = order_page.is_estimated_time_found()
        price = order_page.is_price_found()

        self.assertTrue(est_time)
        self.assertTrue(price)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()        