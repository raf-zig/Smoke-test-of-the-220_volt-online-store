import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Cart_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    order_registration = "//h1[@class='mhbspace-20 text-center']"
    product_name = "//a[@id='cart-product-link-714791']"
    # Actions

    def get_order_registration(self):
        return self.driver.find_element(By.XPATH, self.order_registration)

    def get_product_name(self):
        return self.driver.find_element(By.XPATH, self.product_name)

    # Methods

    def order(self):
        self.assert_word(self.get_order_registration(), "Оформление заказа")
        self.assert_word(self.get_product_name(), "Смеситель для ванны с душем AM PM X-Joy F85A95000")