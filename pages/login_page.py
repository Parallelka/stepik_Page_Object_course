from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators

class LoginPage(BasePage):
    
    def should_be_login_page(self):

        #register_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        #register_form.click() пока не используется

        login_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        login_form.click()

       # def should_be_login_page(self):
        #    self.should_be_login_url()
        #    self.should_be_login_form()
         #   self.should_be_register_form()
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def should_be_login_url(self):
        assert "login" in browser.current_url, "Login is not presented"  # проверка того, что в текущем url содержится строка login






   