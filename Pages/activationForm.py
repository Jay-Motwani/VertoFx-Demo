from selenium.webdriver.support.select import Select

global first_name
first_name = "firstName"
global last_name
last_name = "lastName"
global email
email = "email"
global country_code
country_code = "countryCode"
global contact_number
contact_number = "phone"
global password
password = "password"
global confirm_password
confirm_password = "confirmPassword"


def enter_username(driver, firstname, lastname):
    driver.find_element_by_name(first_name).send_keys(firstname)
    driver.find_element_by_name(last_name).send_keys(lastname)


def enter_email(driver, email):
    driver.find_element_by_name(email).send_keys(email)


def select_country_code(driver, country_code):
    select = Select(driver.find_element_by_name(country_code))
    select.select_by_value(country_code)


def enter_contact_number(driver, contact_number):
    driver.find_element_by_name(contact_number).send_keys(contact_number)


def enter_password(driver, password):
    driver.find_element_by_name(password).send_keys(password)


def enter_confirm_password(driver, confirm_password):
    driver.find_element_by_name(confirm_password).send_keys(confirm_password)
