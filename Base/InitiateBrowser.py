from selenium import webdriver
from Base import Paths

class triggerBrowser:
    def open_browser(self, url, browser):
        driver_path = Paths.GetBrowserPath(browser)
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.maximize_window()
        self.driver.get(url)
        return self.driver

    def close_browser(self):
        self.driver.close()
