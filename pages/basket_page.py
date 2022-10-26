from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import CatalogPageLocators


class BasketPage(BasePage):
    def view_shopping_cart(self):
        self.browser.find_element(*BasketPageLocators.VIEW_SHOPPING_CART).click()

    def compair_price_of_book(self):
        if (CatalogPageLocators.PRICE_OF_BOOK == self.browser.find_element(*BasketPageLocators.PRICE_OF_BOOK_IN_CART)):
            assert 'This is added book', "wrong book"

    def compair_name_of_book(self):
        if (CatalogPageLocators.NAME_OF_BOOK == self.browser.find_element(*BasketPageLocators.NAME_OF_BOOK_IN_CART)):
            assert 'This is added book', "wrong book"