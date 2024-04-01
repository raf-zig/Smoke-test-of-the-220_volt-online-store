from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base

class Bathtub_faucet_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    mixers_for_bathroom = "//h1[@class='head-1']"
    price_slider = "//*[@id='price_slider']/div[2]"
    date_receipt_check_box = "//*[@id='delivery_state__more-than-two-days']"
    product_with_high_rating_check_box = "//*[@id='high_rating__1']"
    all_manufacturers_check_box = "//*[@id='filterForm']/div[1]/div[7]/ul/li[1]/span/label"
    shower_set_check_box = "//*[@id='filterForm']/div[1]/div[9]/ul/li[3]/span/label"
    type_of_installation = "//*[@id='filterForm']/div/div[10]/p/span/span/a"
    on_wall_check_box = "//*[@id='filterForm']/div/div[10]/ul/li[7]/span/label"
    type_of_management = "//*[@id='filterForm']/div/div[11]/p/span/span/a"
    manual_check_box = "//*[@id='filterForm']/div[1]/div[11]/ul/li[5]/span/label"
    rotation_of_spout = "//*[@id='filterForm']/div/div[12]/p/span/span/a"
    rotary_check_box = "//*[@id='p17364_1681917047']"
    shape_of_outflow = "//*[@id='filterForm']/div/div[13]/p/span/span/a"
    traditional_check_box = "//*[@id='filterForm']/div/div[13]/ul/li[4]/span/label"
    standard_of_connection = "//*[@id='filterForm']/div/div[18]/p/span/span/a"
    _1_2_check_box = "//*[@id='filterForm']/div/div[18]/ul/li[1]/span/label"
    mounting_holes = "//*[@id='filterForm']/div/div[19]/p/span/span/a"
    _2_hole = "//*[@id='p17361_450215437']"
    material = "//*[@id='filterForm']/div/div[21]/p/span/span/a"
    brass = "//*[@id='p4730_564374798']"
    coating_color = "//*[@id='filterForm']/div/div[23]/p/span/span/a"
    chrome = "//*[@id='filterForm']/div/div[23]/ul/li[3]/span/label"
    spout_length = "//*[@id='filterForm']/div/div[24]/p/span/span/a"
    spout_length_slider = "//*[@id='p17368_slider']/div[1]"
    collection = "//*[@id='filterForm']/div/div[30]/p/span/span/a"
    spirit_v_2_0 = "//*[@id='filterForm']/div/div[30]/ul/li[4]/span/label"
    homeland = "//*[@id='filterForm']/div/div[31]/p/span/span/a"
    germany = "//*[@id='p7064_4106596712']"
    select_model_button = "//*[@id='filterSubm']"
    mixer = "//div/a[@title='Смеситель для ванны с душем AM PM X-Joy F85A95000']"

    # Getters

    def get_mixers_for_bathroom(self):
       return self.driver.find_element(By.XPATH, self.mixers_for_bathroom)

    def get_price_slider(self):
       return self.driver.find_element(By.XPATH, self.price_slider)

    def get_date_receipt_check_box(self):
       return self.driver.find_element(By.XPATH, self.date_receipt_check_box)

    def get_product_with_high_rating_check_box(self):
       return self.driver.find_element(By.XPATH, self.product_with_high_rating_check_box)

    def get_all_manufacturers_check_box(self):
       return self.driver.find_element(By.XPATH, self.all_manufacturers_check_box)

    def get_shower_set_check_box(self):
       return self.driver.find_element(By.XPATH, self.shower_set_check_box)

    def get_type_of_installation(self):
       return self.driver.find_element(By.XPATH, self.type_of_installation)

    def get_on_wall_check_box(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.on_wall_check_box)))

    def get_type_of_management(self):
       return self.driver.find_element(By.XPATH, self.type_of_management)

    def get_manual_check_box(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.manual_check_box)))

    def get_rotation_of_spout(self):
       return self.driver.find_element(By.XPATH, self.rotation_of_spout)

    def get_rotary_check_box(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.rotary_check_box)))

    def get_shape_of_outflow(self):
       return self.driver.find_element(By.XPATH, self.shape_of_outflow)

    def get_traditional_check_box(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.traditional_check_box)))

    def get_standard_of_connection(self):
       return self.driver.find_element(By.XPATH, self.standard_of_connection)

    def get_1_2_check_box(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self._1_2_check_box)))

    def get_mounting_holes(self):
       return self.driver.find_element(By.XPATH, self.mounting_holes)

    def get_2_hole(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self._2_hole)))

    def get_spout_length(self):
       return self.driver.find_element(By.XPATH, self.spout_length)

    def get_spout_length_slider(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.spout_length_slider)))

    def get_collection(self):
       return self.driver.find_element(By.XPATH, self.collection)

    def get_spirit_v_2_0(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.spirit_v_2_0)))

    def get_homeland(self):
       return self.driver.find_element(By.XPATH, self.homeland)

    def get_germany(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.germany)))

    def get_select_model_button(self):
       return self.driver.find_element(By.XPATH, self.select_model_button)

    def get_mixer(self):
       return self.driver.find_element(By.XPATH, self.mixer)

    # Actions

    def change_price_slider(self):
        action = ActionChains(self.driver)
        price_slider = self.get_price_slider()
        action.click_and_hold(price_slider).move_by_offset(5, 0).release().perform()
        print("Change price slider")

    def click_date_receipt_check_box(self):
        self.get_date_receipt_check_box().click()
        print("click date receipt check box")

    def click_product_with_high_rating_check_box(self):
        self.get_product_with_high_rating_check_box().click()
        print("click product with high rating check box")

    def click_all_manufacturers_check_box(self):
        self.get_all_manufacturers_check_box().click()
        print("click all manufacturers check box")

    def click_shower_set_check_box(self):
        self.get_shower_set_check_box().click()
        print("click shower set check box")

    def click_type_of_installation(self):
        self.get_type_of_installation().click()
        print("click type of installation")

    def click_on_wall_check_box(self):
        self.get_on_wall_check_box().click()
        print("click on wall check box")

    def click_type_of_management(self):
        self.get_type_of_management().click()
        print("click type of management")

    def click_manual_check_box(self):
        self.get_manual_check_box().click()
        print("click manual check box")

    def click_rotation_of_spout(self):
        self.get_rotation_of_spout().click()
        print("click rotation of spout")

    def click_rotary_check_box(self):
        self.get_rotary_check_box().click()
        print("click rotary check box")

    def click_shape_of_outflow(self):
        self.get_shape_of_outflow().click()
        print("click shape of outflow")

    def click_traditional_check_box(self):
        self.get_traditional_check_box().click()
        print("click traditional check box")

    def click_standard_of_connection(self):
        self.get_standard_of_connection().click()
        print("click standard of connection")

    def click_1_2_check_box(self):
        self.get_1_2_check_box().click()
        print("click 1_2 check box")

    def click_mounting_holes(self):
        self.get_mounting_holes().click()
        print("click mounting holes")

    def click_2_hole(self):
        self.get_2_hole().click()
        print("click 2_hole")

    def click_spout_length(self):
        self.get_spout_length().click()
        print("click spout length")

    def change_spout_length_slider(self):
        action = ActionChains(self.driver)
        spout_length_slider = self.get_spout_length_slider()
        action.click_and_hold(spout_length_slider).move_by_offset(5, 0).release().perform()
        print("Change spout length slider")

    def click_collection(self):
        self.get_collection().click()
        print("click collection")

    def click_spirit_v_2_0(self):
        self.get_spirit_v_2_0().click()
        print("click spirit v_2_0")

    def click_homeland(self):
        self.get_homeland().click()
        print("click homeland")

    def click_germany(self):
        self.get_germany().click()
        print("click germany")

    def click_select_model_button(self):
        self.get_select_model_button().click()
        print("click select model button")

    def click_mixer(self):
        self.get_mixer().click()
        print("click mixer")

   # Methods

    def model_selection(self):
        self.get_current_url()
        self.assert_word(self.get_mixers_for_bathroom(), "Смесители для ванны")
        self.change_price_slider()
        self.click_date_receipt_check_box()
        self.click_product_with_high_rating_check_box()
        self.click_all_manufacturers_check_box()
        self.click_shower_set_check_box()
        self.click_type_of_installation()
        self.click_on_wall_check_box()
        self.click_type_of_management()
        self.click_manual_check_box()
        self.click_rotation_of_spout()
        self.click_rotary_check_box()
        self.click_shape_of_outflow()
        self.click_traditional_check_box()
        self.click_standard_of_connection()
        self.click_1_2_check_box()
        self.click_mounting_holes()
        self.click_2_hole()
        self.click_spout_length()
        self.change_spout_length_slider()
        self.click_collection()
        self.click_spirit_v_2_0()
        self.click_homeland()
        self.click_germany()
        self.click_select_model_button()
        self.click_mixer()

