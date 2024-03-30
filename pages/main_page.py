from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base

import time

class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    catalog = "/html/body/header/div[2]/div[1]/ul/li/a"

    # Getters

    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))

    # Actions

    def click_catalog(self):
        self.get_catalog().click()
        print("Click catalog")

# Methods





