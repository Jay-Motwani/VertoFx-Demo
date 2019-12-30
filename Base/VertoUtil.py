from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class vertoFxUtilities:
    def __init__(self, driver):
        self.driver = driver

    def clickElement(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def dynamicWait(self, by, locator):
        waitTime = WebDriverWait(self.driver, 60)
        waitTime.until(EC.presence_of_element_located((by, locator)))

    def waitForProgressSpinner(self):
        waitTime = WebDriverWait(self.driver, 60)
        waitTime.until(EC.invisibility_of_element((By.CLASS_NAME, ".ngx-progress-bar.ngx-progress-bar-ltr")))
