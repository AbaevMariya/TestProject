from .base_page import BasePage
from .locators import CatalogPageLocators

class CatalogPage(BasePage):
    def should_be_catalog_page(self):
        self.should_be_catalog_link()
        #добавляем выбранный товар в карзину
        self.should_be_add_product_to_busket()

    def should_be_catalog_link(self):
        assert 'catalogue' in self.browser.current_url,"wrong url"

    def should_be_add_product_to_busket(self):
        assert self.element_is_present(*CatalogPageLocators.PRODUCT_BTN)