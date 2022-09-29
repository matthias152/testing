from locators import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
    locator = "username"
    # locator = "password"


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    search_text_element = SearchTextElement()

    def login_user(self):
        user_element = self.driver.find_element(*MainPageLocators.USER_FIELD)
        psw_element = self.driver.find_element(*MainPageLocators.PSW_FIELD)
        user_element.send_keys("matt")
        psw_element.send_keys("1526")

    def is_title_matches(self):
        return "CryptoSite" in self.driver.title

    def not_login_error(self):
        return "Please enter a correct username and password. Note that both fields may be case-sensitive." not in self.driver.page_source

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        element.click()


class LoginSuccessPage(BasePage):
    def is_results_found(self):
        return "Dont have an account?" not in self.driver.page_source