from selenium.webdriver.common.by import By
from base.vertoUtil import vertoFxUtilities


class signIn:
    def __init__(self, driver):
        self.driver = driver
        self.email = "email"
        self.password = "password"
        self.ForgotPassword = "Forgot password?"
        self.SignInBtn = ".btn.btn-custom-navy.w-100[type='submit']"
        self.SignUp = "Sign up"
        self.OTP = "otp"
        self.ProceedBtn = ".btn.btn-custom-navy.w-100[type='submit']"
        self.ReSendOtpBtn = ".btn.btn-custom-navy-outline.w-100[type='button']"

    def sign_in(self, mail, password):
        utilities = vertoFxUtilities(self.driver)
        self.driver.find_element_by_name(self.email).send_keys(mail)
        self.driver.find_element_by_name(self.password).send_keys(password)
        utilities.clickElement(self.driver.find_element_by_css_selector(self.SignInBtn))
        utilities.dynamicWait(By.NAME, self.OTP)
        self.driver.find_element_by_name(self.OTP).send_keys("2342")
        utilities.clickElement(self.driver.find_element_by_css_selector(self.ProceedBtn))
        utilities.waitForProgressSpinner()
