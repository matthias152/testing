import unittest
from selenium import webdriver
import page
import time


class CryptoSite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:8000/")
        login_page = page.LoginPage(self.driver)
        login_page.login_field = "matt"
        login_page.password_field = "1526"
        login_page.click_enter_button()

    def test_login_successful(self):
        login_page = page.LoginPage(self.driver)
        login_check = login_page.is_results_found()
        self.assertTrue(login_check)

    def test_crypto_buy(self):

        wallet_page = page.WalletPage(self.driver)
        ripple_before = wallet_page.check_for_ripple()
        balance_before = wallet_page.check_for_balance()
        ripple_before_quantity = float(ripple_before.text)
        balance_before_quantity = page.HelpFunctions.get_balance(balance_before.text)
        wallet_page.go_to_buy_cryptos()

        buy_page = page.BuyCryptoPage(self.driver)
        buy_page.crypto_name = "ripple"
        buy_page.crypto_quantity = "10"

        buy_page.click_buy_button()
        buy_page.go_to_home_button()

        ripple_after = wallet_page.check_for_ripple()
        balance_after = wallet_page.check_for_balance()
        ripple_after_quantity = float(ripple_after.text)
        balance_after_quantity = page.HelpFunctions.get_balance(balance_after.text)

        self.assertTrue(ripple_before_quantity < ripple_after_quantity)
        self.assertTrue(float(balance_after_quantity) < float(balance_before_quantity))

    def test_balance_add(self):
        wallet_page = page.WalletPage(self.driver)
        balance_before = wallet_page.check_for_balance()
        balance_before_quantity = page.HelpFunctions.get_balance(balance_before.text)
        wallet_page.go_to_add_more_funds()

        deposit_page = page.DepositPage(self.driver)
        deposit_page.deposit = "20"
        deposit_page.click_deposit_button()
        deposit_page.go_to_home_button()

        balance_after = wallet_page.check_for_balance()
        balance_after_quantity = page.HelpFunctions.get_balance(balance_after.text)

        self.assertTrue(float(balance_after_quantity) == float(balance_before_quantity) + 20)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()