from selenium.webdriver.common.by import By


class MainPageLocators(object):
    ENTER_BUTTON = (By.XPATH, "/html/body/div[1]/div[2]/div/section[1]/div[1]/div/a")


class OrderPageLocators(object):
    LANG_CHANGE = (By.CLASS_NAME, "tname")
    EN_LANG = (By.ID, "Row_1en")
    DE_LANG = (By.ID, "Row_16de")
    PROOF_CHECK = (By.ID, "proofreading")