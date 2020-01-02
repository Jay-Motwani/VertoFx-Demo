from sys import argv

from selenium import webdriver
from Base import Paths

global Browserarg
global urlarg
Browserarg, urlarg = argv

class triggerBrowser:
    def open_browser(self, urlarg, Browserarg):
        driver_path = Paths.GetBrowserPath(Browserarg)
        if Browserarg == "chrome":
            self.driver = webdriver.Chrome(executable_path=driver_path)

        self.driver.maximize_window()
        self.driver.get(urlarg)
        return self.driver

    def close_browser(self):
        self.driver.close()
