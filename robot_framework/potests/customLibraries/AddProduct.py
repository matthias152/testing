from robot.api.deco import library, keyword
from robot.libraries.BuiltIn import BuiltIn
import time

@library
class AddProduct:

    @property
    def selLib(self):
        return BuiltIn().get_library_instance("SeleniumLibrary")

    @keyword
    def add_items_to_cart(self, product):
        self.selLib.mouse_over("//img[@alt='"+product+"']")
        time.sleep(1)
        self.selLib.click_element("(//span[contains(text(),'Add to Cart')])")
        self.selLib.wait_until_page_contains("You need to choose options for your item.")
        self.selLib.click_element("//div[@id='option-label-size-143-item-168']")
        self.selLib.click_element("//div[@id='option-label-color-93-item-50']")
        self.selLib.click_element("//span[normalize-space()='Add to Cart']")
        self.selLib.wait_until_page_contains("You added Proteus Fitness Jackshirt to your shopping cart.")

            
