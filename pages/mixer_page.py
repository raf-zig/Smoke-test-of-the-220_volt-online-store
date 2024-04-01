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

    into_cart = "/html/body/div[3]/div[3]/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]"
    go_to_cart = "//div/a[contains(text(),'Перейти в корзину')]"

    # Getters

    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.into_cart)))
    def get_go_to_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart)))
    # Actions

    def click_cart(self):
        self.get_cart().click()
        print("click in cart")

    def click_go_to_cart(self):
        self.get_go_to_cart().click()
        print("click go to cart")

    # Methods

    def put_in_cart(self):
        self.click_cart()
        self.click_go_to_cart()
