import pytest
import time

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.catalog_page import CatalogPage

#from .pages.base_page import BasePage

link = 'http://selenium1py.pythonanywhere.com/ru/'

# class TestMainPage():
#
#     @pytest.mark.open_page
#     @pytest.mark.smoke

# 1 variant
#     def test_1(self, browser):
#         browser.get(link)
#
#     def test2(self, browser):
#         browser.get(link)
#         time.sleep(5)
# 2 variant

@pytest.mark.smoke
def test_guest_can_go_to_catalogue(browser):
    # создает экземпляр главной страницы - Main Page
    page = MainPage(browser, link)
    # открывает страницу
    page.open_page()
    # проверяет, что на главной странице присутствует ссылка на страницу товаров
    page.should_be_link_to_product_page()
    # переходит на страницу с товарами
    page.go_to_product_page()

# Тест проверяет, что пользователь может перейти с главной страницы сайта на страницу авторизации
@pytest.mark.regression
def test_guest_go_to_login_page(browser):
    #link = 'http://selenium1py.pythonanywhere.com/ru/'
    page = MainPage(browser, link)
    page.open_page()
    page.go_to_login_page()
    time.sleep(2)
    page = LoginPage(browser, link)
    page.should_be_login_page()

# Тест проверяет, что пользователь может зарегистрироваться
def test_user_сan_autorize(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # открывает страницу авторизации
    page.open_page()
    # регистрирует нового пользователя
    page.register_user(email=str(time.time()) + '@mail.org', password='QAZ123edc!')
    # проверяет, что пользователь авторизован
    time.sleep(2)
    page.should_be_autorized_user()

def test_user_add_item_to_card(browser):
    page = MainPage(browser,link)
    page.open_page()
    page.go_to_product_page()
    time.sleep(2)
    page = CatalogPage(browser, link)
 #   page.should_be_link_to_product_page()
    time.sleep(2)
    page.should_be_add_product_to_busket()
    time.sleep(2)




