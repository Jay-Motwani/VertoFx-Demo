from selenium import webdriver


class triggerBrowser:
    def open_browser(self, url):
        driver_path = "../ExtFiles/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.maximize_window()
        self.driver.get(url)
        return self.driver

    def close_browser(self):
        self.driver.close()
