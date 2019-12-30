from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Utilities:
    def __init__(self, driver):
        self.driver = driver

    def Click_Element(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def DynamicWait(self, By, locator):
        waittime = WebDriverWait(self.driver, 60)
        waittime.until(EC.presence_of_element_located((By, locator)))

    def WaitForProgressSpinner(self):
        if self.check_progrssspinner() is True:
            waittime = WebDriverWait(self.driver, 60)
            waittime.until(EC.invisibility_of_element(
                self.driver.find_element_by_css_selector(".ngx-foreground-spinner center-center")))

    def check_progrssspinner(self):
        try:
            self.driver.find_element_by_css_selector(".ngx-foreground-spinner center-center")
        except NoSuchElementException:
            return False
        return True
