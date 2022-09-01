from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("http://127.0.0.1:8000/")

username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')

username.send_keys('matt')
password.send_keys('1526')

login = driver.find_element(By.NAME, 'login-btn').click()

deposit = driver.find_element(By.PARTIAL_LINK_TEXT, 'Add More Funds!').click()
deposit_field = driver.find_element(By.NAME, 'addBalanceFunds')

deposit_field.send_keys('100')

deposit_submit = driver.find_element(By.NAME, "deposit").click()
