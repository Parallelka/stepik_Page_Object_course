from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_add_to_basket_form()

    def should_be_add_to_basket_form(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_FORM), "Basket form is not presented"

    def add_to_basket(self):
        button = self.browser.find_element(By.XPATH, "//*[@class='btn btn-lg btn-primary btn-add-to-basket']")
        button.click()

    #def should_be_price_basket_match_price(self):
       # price_basket = self.browser.find_element(By.XPATH, "//*[@class='basket-mini pull-right hidden-xs']")
       # price_basket_text = price_basket.text
       # print(price_basket_text)
       # price = self.browser.find_element(By.XPATH, "//*[@class='price_color']")
       # price_text = price.text
        #print(price_text)
        #assert price_basket_text == price_text, "Should be match"





