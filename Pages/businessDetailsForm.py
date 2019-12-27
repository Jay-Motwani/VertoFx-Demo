from selenium.webdriver.support.select import Select


class BusinessDetailsForm():
    def __init__(self, driver):
        self.driver = driver
        self.country = "//select[@name='country']"
        self.business_name = "//input[@name='companyName']"
        self.company_number = "//input[@name='companyNumber']"
        self.company_website = "//input[@name='companyWebsite']"
