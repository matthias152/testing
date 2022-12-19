from selenium.webdriver.common.by import By

class MainPageLocators(object):
    complete_button = (By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div/div/table/tbody/tr/td[3]/a/button")
    delete_button = (By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div/div/table/tbody/tr/td[3]/button")
    date_button = (By.CLASS_NAME, "ant-picker-input")
    today_date = (By.CLASS_NAME, "ant-picker-today-btn")
    add_todo_button = (By.XPATH, "/html/body/div[1]/form/div[2]/button")