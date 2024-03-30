from pages.catalog_page import Catalog_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from selenium import webdriver

def test_select_product():
    driver = webdriver.Chrome()
    print("Start Test")

    login = Login_page(driver)
    login.authorization()
    mp = Main_page(driver)
    mp.click_catalog()
    driver.execute_script("window.scrollTo(0, 350)")
    cp = Catalog_page(driver)
    cp.choosing_bathtub_faucet()
    print("finish")
    driver.quit()

















































