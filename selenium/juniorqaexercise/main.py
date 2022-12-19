import unittest
from selenium import webdriver
import page
import time
import random
import string

class ToDoSite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        z = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=32))
        self.driver.get("http://ho-testertester.s3-website.eu-central-1.amazonaws.com/#" + z)
        time.sleep(2)

    def test_enter_successful(self):
        main_page = page.MainPage(self.driver)
        main_page_check = main_page.is_results_found()
        self.assertTrue(main_page_check)

    def test_length_less_than_5(self):
        main_page = page.MainPage(self.driver)  
        main_page.text_field = "abcd"
        less_than_5_check = main_page.is_less_than_5_found()
        self.assertTrue(less_than_5_check)

    def test_is_date_visible(self):
        main_page = page.MainPage(self.driver)  
        main_page.text_field = "abcdef"
        date_visible = main_page.is_date_visible()
        self.assertTrue(date_visible)

    def test_creating_todo_item(self):
        main_page = page.MainPage(self.driver)
        main_page.text_field = "justtesttodoitem"
        main_page.set_date_today()
        time.sleep(1)
        main_page.add_todo_item()
        time.sleep(2)

        complete_button_exist = main_page.is_complete_button_exist()
        delete_button_exist = main_page.is_delete_button_exist()

        self.assertTrue(complete_button_exist)
        self.assertTrue(delete_button_exist)

    def tearDown(self):
        self.driver.close()    


if __name__ == "__main__":
    unittest.main()