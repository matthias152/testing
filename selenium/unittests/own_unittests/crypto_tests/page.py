from lib2to3.pytree import Base
from pydoc import locate
from locators import *
from element import ElementByName

class LoginUsernameElement(ElementByName):
    locator = "username"

class LoginPasswordElement(ElementByName):
    locator = "password"

class BuyCryptoNameElement(ElementByName):
    locator = "cryptoNameBuy"

class BuyCryptoQuantityElement(ElementByName):
    locator = "quantityDollarsBuy"

class DepositElement(ElementByName):
    locator = "addBalanceFunds"


class HelpFunctions:
    def get_balance(balance_element):
        balance_element = balance_element.split()
        return balance_element[1][:-1]



class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def go_to_home_button(self):
        self.driver.find_element(By.LINK_TEXT, "CryptoSite").click()


class LoginPage(BasePage):
    login_field = LoginUsernameElement()
    password_field = LoginPasswordElement()

    def click_enter_button(self):
        self.driver.find_element(*MainPageLoginLocators.LOGIN_BUTTON).click()

    def is_results_found(self):
        return "Dont have an account?" not in self.driver.page_source


class WalletPage(BasePage):
    def check_for_ripple(self):
        ripple_quantity = self.driver.find_element(*WalletPageLocators.RIPPLE)
        return ripple_quantity

    def check_for_balance(self):
        balance = self.driver.find_element(*WalletPageLocators.BALANCE)
        return balance

    def go_to_add_more_funds(self):
        self.driver.find_element(*WalletPageLocators.ADD_MORE_FUNDS).click()

    def go_to_buy_cryptos(self):
        self.driver.find_element(*WalletPageLocators.BUY_CRYPTOS).click()


class BuyCryptoPage(BasePage):
    crypto_name = BuyCryptoNameElement()
    crypto_quantity = BuyCryptoQuantityElement()

    def click_buy_button(self):
        self.driver.find_element(*BuyCryptoLocators.BUY_BUTTON).click()


class DepositPage(BasePage):
    deposit = DepositElement()

    def click_deposit_button(self):
        self.driver.find_element(*DepositLocators.DEPOSIT_BUTTON).click()
