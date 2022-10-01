from selenium.webdriver.common.by import By

class MainPageLoginLocators(object):
    LOGIN_BUTTON = (By.NAME, "login-btn")


class WalletPageLocators(object):
    # text
    RIPPLE = (By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[2]/td[2]")
    BALANCE = (By.XPATH, "/html[1]/body[1]/div[1]/h2[1]")
    # buttons
    BUY_CRYPTOS = (By.PARTIAL_LINK_TEXT, 'Buy Cryptos')
    ADD_MORE_FUNDS = (By.PARTIAL_LINK_TEXT, 'Add More Funds!')


class BuyCryptoLocators(object):
    BUY_BUTTON = (By.XPATH, "/html[1]/body[1]/form[1]/input[4]")

class DepositLocators(object):
    DEPOSIT_BUTTON = (By.NAME, "deposit")