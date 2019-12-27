from selenium.webdriver.support.select import Select


class ActivationForm():
    def __init__(self, driver):
        self.driver = driver
        self.first_name = "firstName"
        self.last_name = "lastName"
        self.email = "email"
        self.country_code = "countryCode"
        self.contact_number = "phone"
        self.password = "password"
        self.confirm_password = "confirmPassword"

    def enter_username(self, firstname, lastname):
        self.driver.find_element_by_name(self.first_name).send_keys(firstname)
        self.driver.find_element_by_name(self.last_name).send_keys(lastname)
        print("First and lastname fields are populated")

    def enter_email(self, email):
        self.driver.find_element_by_name(self.email).send_keys(email)
        print("Email field populated")

    def select_country_code(self, country_code):
        select = Select(self.driver.find_element_by_name(self.country_code))
        select.select_by_value(country_code)
        print("Country code selected")

    def enter_contact_number(self, contact_number):
        self.driver.find_element_by_name(self.contact_number).send_keys(contact_number)
        print("Contact number filed is populated")

    def enter_password(self, password):
        self.driver.find_element_by_name(self.password).send_keys(password)
        print("Password filed is populated")

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element_by_name(self.confirm_password).send_keys(confirm_password)
        print("Confirm password filed is populated")