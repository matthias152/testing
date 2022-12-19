from locators import *
from element import ElementByXPath
import time

class MainPageTextField(ElementByXPath):
    locator = "/html/body/div[1]/form/div[1]/div/div/div[2]/div/div/span/input"


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    text_field = MainPageTextField()

    def is_results_found(self):
        return "Add TODO item" in self.driver.page_source

    def is_less_than_5_found(self):
        return "Length must be more than 5" in self.driver.page_source

    def is_date_visible(self):
        return "Select a date:" in self.driver.page_source

    def set_date_today(self):
        self.driver.find_element(*MainPageLocators.date_button).click()
        time.sleep(1)
        self.driver.find_element(*MainPageLocators.today_date).click()

    def add_todo_item(self):
        self.driver.find_element(*MainPageLocators.add_todo_button).click()

    def is_complete_button_exist(self):
        try:
            boolvalue = self.driver.find_element(*MainPageLocators.complete_button).is_displayed()
        except:
            boolvalue = False
        return boolvalue

    def is_delete_button_exist(self):
        try:
            boolvalue = self.driver.find_element(*MainPageLocators.delete_button).is_displayed()
        except:
            boolvalue = False
        return boolvalue
