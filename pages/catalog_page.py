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

    # Getters

    def get_mixer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mixer)))

    # Actions

    def click_mixer(self):
        self.get_mixer().click()
        print("Click mixer")
