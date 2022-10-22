import time

from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators
from .catalog_page import CatalogPageLocators

class BasePage():

    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    def open_page(self):
        self.browser.get(self.link)

    def element_is_present(self, method, locator):
        try:
            self.browser.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True
    #
    # def go_to_login_page(self):
    #     self.browser.find_element(*MainPageLocators.LOGIN_BTN).click()

    def should_be_autorized_user(self):
        time.sleep(2)
        assert self.element_is_present(*BasePageLocators.USER_ICON)

    def add_product_in_busket(self):
        assert self.element_is_present(*CatalogPageLocators.PRODUCT_BTN)