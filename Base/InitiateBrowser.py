import sys

from selenium import webdriver
from Base import Paths


global browser
global url
url = str(sys.argv[2])
browser = str(sys.argv[1])

class triggerBrowser:
    def open_browser(self, url, browser):
        driver_path = Paths.GetBrowserPath(Browserarg)
        if browser == "chrome":
            self.driver = webdriver.Chrome(executable_path=driver_path)

        self.driver.maximize_window()
        self.driver.get(url)
        return self.driver

    def close_browser(self):
        self.driver.close()
