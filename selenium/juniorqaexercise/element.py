from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class ElementByXPath(object):

    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(By.XPATH, self.locator))
        driver.find_element(By.XPATH, self.locator).clear()
        driver.find_element(By.XPATH, self.locator).send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(By.XPATH, self.locator))
        element = driver.find_element(By.XPATH, self.locator)
        return element.get_attribute("value")