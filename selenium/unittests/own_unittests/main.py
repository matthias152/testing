import unittest
from selenium import webdriver
import page
import time


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("http://127.0.0.1:8000/")

    def test_login(self):
        main_page = page.MainPage(self.driver)
        # self.assertTrue(main_page.is_title_matches())
        # self.assertTrue(main_page.not_login_error())
        # main_page.search_text_element = "matt"
        # main_page.search_text_element = "1526"
        main_page.login_user()
        main_page.click_go_button()
        # login_success_page = page.LoginSuccessPage(self.driver)
        # self.assertTrue(login_success_page.is_results_found())
        time.sleep(3)
    
    def tearDown(self):
        time.sleep(3)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()