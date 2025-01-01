from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_btn = self.driver.find_element(By.ID, "react-burger-menu-btn")
        self.logout_btn = None


    def click_on_menu_btn(self):
        self.menu_btn.click()
        self.logout_btn = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "logout_sidebar_link"))
        )


    def click_on_logout_btn(self):
        self.logout_btn.click()