from selenium.webdriver.common.by import By
from base.base_class import Base

class Cart_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    order_registration = "//h1[@class='mhbspace-20 text-center']"
    product_name = "//a[@id='cart-product-link-714791']"
    total_amount = "//*[@id='sum714791']"
    x_sign = "//a[@class='btn-del']"

    # Actions

    def get_order_registration(self):
        return self.driver.find_element(By.XPATH, self.order_registration)

    def get_product_name(self):
        return self.driver.find_element(By.XPATH, self.product_name)

    def get_total_amount(self):
        return self.driver.find_element(By.XPATH, self.total_amount)

    def get_x_sign(self):
        return self.driver.find_element(By.XPATH, self.x_sign)

    # Methods

    def order(self):
        self.get_current_url()
        self.assert_word(self.get_order_registration(), "Оформление заказа")
        self.assert_word(self.get_product_name(), "Смеситель для ванны с душем AM PM X-Joy F85A95000")
        self.assert_word(self.get_total_amount(), "19 990")

    def delete_item(self):
        self.get_x_sign().click()
