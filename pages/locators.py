from selenium.webdriver.common.by import By


class MainPageLocators():
    LINK_TO_PRODUCT_PAGE = (By.XPATH, "//ul[@id='browse']//ul//a")
    LOGIN_BTN = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REG_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BTN = (By.XPATH, "//form[@id='register_form']//button")

class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')

class CatalogPageLocators():
   # PRODUCT_BTN = (By.XPATH,"//div[@class = 'product_price']//button")
   # NAME_OF_BOOK = (By.XPATH, "//*[@class='product_pod']/h3/a[text() = 'The shellcoder's handbook']")

    #NAME_OF_BOOK = (By.XPATH, "//*[@class='product_pod']/h3/a]")
    NAME_OF_BOOK = (By.XPATH, "//*[@id='default']/div[2]/div/div/div/section/div/ol/li[1]/article/h3/a")
    PRICE_OF_BOOK = (By.XPATH, '//div[@class = "product_price"]/p')
    PRODUCT_BTN = (By.XPATH,"/html/body/div[2]/div/div/div/section/div/ol/li[1]/article/div[2]/form/button")


class BasketPageLocators():
    VIEW_SHOPPING_CART = (By.XPATH,'//*[@id="messages"]/div[3]/div/p[2]/a[1]')
   # PRICE_OF_BOOK_IN_CART = (By.XPATH, "//div[@class = 'basket-items']//h3/a[text() = 'The shellcoder's handbook']")
    PRICE_OF_BOOK_IN_CART = (By.XPATH, "//div[@class='basket-items']//div[4]/p")
    NAME_OF_BOOK_IN_CART = (By.XPATH, "//div[@class='basket-items']//h3/a")