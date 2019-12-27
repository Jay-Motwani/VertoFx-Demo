from Base import VertoUtil


class SignIn():
    def __init__(self, driver):
        self.driver = driver
        self.email = "email"
        self.password = "password"
        self.ForgotPassword = "Forgot password?"
        self.SignInBtn = ".btn btn-custom-navy w-100[type='submit']"
        self.SignUp = "Sign up"
        self.OTP = "otp"
        self.ProceedBtn = ".btn btn-custom-navy w-100[type='submit']"
        self.ReSendOtpBtn = ".btn btn-custom-navy-outline w-100[type='button']"

    def Sign_In(self, email, password):
        self.driver.find_element_by_name(self.email).sendkeys(email)
        self.driver.find_element_by_name(self.password).sendkeys(password)
        VertoUtil.Click_Element(self, self.driver.find_element_by_css_selector(self.SignInBtn))
        VertoUtil.DynamicWait(self, self.driver.find_element_by_name(self.OTP))
        self.driver.find_element_by_name(self.OTP).sendkeys("2342")
        VertoUtil.Click_Element(self, self.driver.find_element_by_css_selector(self.ProceedBtn))
        VertoUtil.WaitForProgressSpinner(self)

