import time

from pages.bathroom_mixers_page import Bathtub_faucet_page
from pages.catalog_page import Catalog_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from selenium import webdriver

from pages.mixer_page import Mixer_page

def test_select_product():
    driver = webdriver.Chrome()
    print("Start Test")
    login = Login_page(driver)
    login.authorization()
    mp = Main_page(driver)
    mp.click_catalog()
    driver.execute_script("window.scrollTo(0, 500)")
    cp = Catalog_page(driver)
    cp.choosing_bathtub_faucet()
    bp = Bathtub_faucet_page(driver)
    bp.model_selection()
    mxp = Mixer_page(driver)
    mxp.put_in_cart()
    time.sleep(5)
    print("Finish")
    driver.quit()


















































