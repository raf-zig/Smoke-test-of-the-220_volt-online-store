import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Mixer_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    product = "//h1[@class='head-1 card-main-title']"
    price = "//*[@id='price_per_m']"
    into_cart = "/html/body/div[3]/div[3]/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]"
    product_added_to_cart = "//p[@class='pre-checkout-title']"
    plus = "//*[@id='line714791']/li[3]/span/span/a[1]"
    minus = "//*[@id='line714791']/li[3]/span/span/a[2]"
    total_amount = "//*[@id='sum714791']"
    x_sign = "//*[@id='line714791']/li[5]/a"
    go_to_cart = "//div/a[contains(text(),'Перейти в корзину')]"

    # Getters

    def get_product(self):
        return self.driver.find_element(By.XPATH, self.product)

    def get_price(self):
        return self.driver.find_element(By.XPATH, self.price)

    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.into_cart)))

    def get_go_to_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart)))

    def get_product_added_to_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_added_to_cart)))

    def get_plus(self):
        return self.driver.find_element(By.XPATH, self.plus)

    def get_minus(self):
        return self.driver.find_element(By.XPATH, self.minus)

    def get_x_sign(self):
        return self.driver.find_element(By.XPATH, self.x_sign)

    def get_total_amount(self):
        return self.driver.find_element(By.XPATH, self.total_amount)

    # Actions

    def click_cart(self):
        self.get_cart().click()
        print("click cart")

    def click_plus(self):
        self.get_plus().click()
        print("click plus")

    def click_minus(self):
        self.get_minus().click()
        print("click minus")

    def click_x_sign(self):
        self.get_x_sign().click()
        print("click x_sign")

    def click_go_to_cart(self):
        self.get_go_to_cart().click()
        print("click go to cart")

    # Methods

    def put_in_cart(self):
        self.get_current_url()
        self.assert_word(self.get_product(), "Смеситель для ванны с душем AM PM X-Joy F85A95000")
        self.assert_word(self.get_price(), "19 990")
        self.click_cart()
        self.assert_word(self.get_product_added_to_cart(), "Товар добавлен в корзину")
        self.click_plus()
        time.sleep(3)
        self.assert_word(self.get_total_amount(), "39 980")
        self.click_minus()
        time.sleep(3)
        self.assert_word(self.get_total_amount(), "19 990")
        self.click_x_sign()
        time.sleep(3)
        self.click_cart()
        self.click_go_to_cart()
