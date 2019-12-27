from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Click_Element(self, element):
    self.driver.execute_script("arguments[0].click();", element)

def DynamicWait(self, By, locator):
    element = WebDriverWait(self.driver, 60).until(
        EC.presence_of_element_located((By, locator)))

def WaitForProgressSpinner(self):
    element = WebDriverWait(self.driver, 60).until(
        EC.invisibility_of_element(self.driver.find_element_by_class_name("ngx-foreground-spinner center-center")))