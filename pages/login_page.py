from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
import time

class Login_page(Base):
    url = "https://ufa.220-volt.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    login_symbol = "/html/body/header/div[2]/div[1]/div[2]/div[1]/a/span[1]/i"
    email = "//*[@id='user_email']"
    password = "//*[@id='user_password']"
    continue_button = "//*[@id='link_login']"
    word_under_login_symbol = "/html/body/header/div[2]/div[1]/div[2]/div[1]/a/span[2]"

    # Getters

    def get_login_symbol(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_symbol)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_password1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    def get_word_under_login_symbol(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_under_login_symbol)))

    # Actions

    def click_login_symbol(self):
        self.get_login_symbol().click()
        print("Click login button")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input email")

    def input_password(self, password):
        self.get_password1().send_keys(password)
        print("Input password")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Click continue button")

    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_login_symbol()
        self.input_email("ziravin@yandex.ru")
        self.input_password("rncv1996")
        self.click_continue_button()
        time.sleep(1)
        self.assert_word_under_login_symbol(self.get_word_under_login_symbol())


