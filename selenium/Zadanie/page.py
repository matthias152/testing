from element import OrderPageElement
from locators import MainPageLocators, OrderPageLocators


class TextField(OrderPageElement):
    locator = "content"


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    def click_enter_button(self):
        self.driver.find_element(*MainPageLocators.ENTER_BUTTON).click()


class OrderPage(BasePage):

    text_field = TextField()

    def change_options(self):
        self.driver.find_element(*OrderPageLocators.LANG_CHANGE).click()
        self.driver.find_element(*OrderPageLocators.EN_LANG).click()
        self.driver.find_element(*OrderPageLocators.DE_LANG).click()
        self.driver.find_element(*OrderPageLocators.PROOF_CHECK).click()

    def is_price_found(self):
        return "zł" in self.driver.page_source

    def is_estimated_time_found(self):
        return "godzin" or "godziny" in self.driver.page_source