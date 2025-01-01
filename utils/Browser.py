from selenium import webdriver
from utils.ConfigReader import ConfigReader


class Browser:
    driver = None

    @staticmethod
    def get_driver():

        if Browser.driver is None:
            browser = ConfigReader.get_property("Basic info", "browser")
            if browser == "chrome":
                Browser.driver = webdriver.Chrome()
            elif browser == "firefox":
                Browser.driver = webdriver.Firefox()
            elif browser == "edge":
                Browser.driver = webdriver.Edge()
            else:
                raise ValueError(f"Unsupported browser: {browser}")
        return Browser.driver



    @staticmethod
    def quit_driver():
            Browser.driver.quit()
            Browser.driver = None
