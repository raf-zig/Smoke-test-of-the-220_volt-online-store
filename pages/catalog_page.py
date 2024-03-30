from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base

import time

class Catalog_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    mixer = "/html/body/div[3]/div/div[2]/div/div[12]/div/div/ul/li[1]/a/span"
    for_bash = "/html/body/div[3]/div/div[2]/div/div[12]/div/div/ul/li[1]/ul/li[3]/a"
    price_slider = "//*[@id='price_slider']/div[2]"

    # Getters

    def get_mixer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mixer)))

    def get_for_bash(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.for_bash)))

    def get_price_slider(self):
        return self.driver.find_element(By.XPATH, self.price_slider)
    # Actions

    def click_mixer(self):
        self.get_mixer().click()
        print("Click mixer")
        #time.sleep(1)

    def click_for_bash(self):
        self.get_for_bash().click()
        print("Click for bash")
        #time.sleep(1)

   # Methods

    def choosing_bathtub_faucet(self):
        self.click_mixer()
        self.click_for_bash()
