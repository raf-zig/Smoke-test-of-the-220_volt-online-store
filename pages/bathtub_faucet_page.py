from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base

import time

class Bathtub_faucet_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    price_slider = "//*[@id='price_slider']/div[2]"
    date_receipt_check_box = "//*[@id='delivery_state__more-than-two-days']"

    # Getters

    def get_price_slider(self):
       return self.driver.find_element(By.XPATH, self.price_slider)

    def get_date_receipt_check_box(self):
       return self.driver.find_element(By.XPATH, self.date_receipt_check_box)

    # Actions
    def change_price_slider(self):
        action = ActionChains(self.driver)
        price_slider = self.get_price_slider()
        action.click_and_hold(price_slider).move_by_offset(20, 0).release().perform()
        print("Change price slider")

    def click_date_receipt_check_box(self):
        self.get_date_receipt_check_box().click()
        print("click date receipt check box")

    # Methods
    def model_selection(self):
        self.change_price_slider()
        self.click_date_receipt_check_box()