import datetime
import time

from pages.bathroom_mixers_page import Bathtub_faucet_page
from pages.cart_page import Cart_page
from pages.catalog_page import Catalog_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.mixer_page import Mixer_page
from selenium import webdriver
from utilities.conftest import set_up

def test_select_product(set_up):
    driver = webdriver.Chrome()
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
    cp = Cart_page(driver)
    cp.order()
    now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
    name_screenshot = 'screenshot' + now_date + '.png'
    time.sleep(2)
    driver.save_screenshot('../screen/' + name_screenshot)
    cp.delete_item()
    time.sleep(2)
    driver.quit()


















































