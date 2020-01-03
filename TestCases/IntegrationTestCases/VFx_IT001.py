import sys
import allure
from urllib3.util import request

from Base.SignUP import SigingUp
from Base.login_to_verto import TestLogin

global browser
global url

url = ""
browser = ""


class SignUp_Flow:

    def pytest_addoption(parser):
        parser.addoption("--url", action="store")
        parser.addoption("--browser", action="store")

    @allure.description("Sign up for verto")
    def test_signup(self):
        cl = TestLogin()
        cl.test_browser_setup(url, browser)
        c2 = SigingUp()
        c2.signup()
        c2.AdminAuth()


if __name__ == "__main__":

    obj = SignUp_Flow()
    obj.test_signup()
