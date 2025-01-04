from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_btn = self.driver.find_element(By.ID, "react-burger-menu-btn")
        self.logout_btn = None
        self.filter_btn = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "product_sort_container"))
        )
        self.product_list = None


    def click_on_menu_btn(self):
        self.menu_btn.click()
        self.logout_btn = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "logout_sidebar_link"))
        )


    def click_on_logout_btn(self):
        self.logout_btn.click()


    def select_filter_option(self, filter_option):
        select = Select(self.filter_btn)
        select.select_by_value(filter_option)
        self.product_list = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
        )

    def get_product_name(self):
        product_elements = self.driver.find_elements(By.CSS_SELECTOR, "div[data-test='inventory-item-name']")
        if len(product_elements) > 0:
            return product_elements[0].text
        else:
            raise IndexError("A megadott index kívül esik a termékek listáján.")

    def check_expected_product(self, expected_product):
        first_product_name = self.get_product_name()
        if first_product_name != expected_product:
            return False
        else: return True
