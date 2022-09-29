from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_BUTTON = (By.NAME, "login-btn")
    USER_FIELD = (By.NAME, 'username')
    PSW_FIELD = (By.NAME, 'password')


class SearchResultsPageLocators(object):
    pass