import requests

from .base_page import BasePage
from .locators import CatalogPageLocators

class CatalogPage(BasePage):
    def should_be_catalog_page(self):
        self.should_be_catalog_link()
        #добавляем выбранный товар в карзину
        self.should_be_add_product_to_busket()

    def should_be_catalog_link(self):
        assert 'catalogue' in self.browser.current_url,"wrong url"

    def remember_name_of_book(self):
        self.browser.find_element(*CatalogPageLocators.NAME_OF_BOOK)

    def remember_price_of_book(self):
        self.browser.find_element(*CatalogPageLocators.PRICE_OF_BOOK)

    def should_be_add_product_to_basket(self):
        #assert\
        self.browser.find_element(*CatalogPageLocators.PRODUCT_BTN).click()

#    def all_books_get(self):
