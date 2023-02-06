from pages.main_page import MainPage
from pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    product_page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    product_page.open()  # открываем страницу
    product_page.should_be_add_to_basket_form()
    product_page.add_to_basket()
    time.sleep(2)

    product_page.solve_quiz_and_get_code()
    time.sleep(10)
    product_page.should_be_price_basket_match_price()