from sys import argv

import allure

from Base import Paths, ReadExcel
from Base.SignUP import SigingUp
from Base.login_to_verto import TestLogin
from Base.AuthorizeNewUser import Authorize


global Browserarg
global urlarg
Browserarg, urlarg = argv

class SignUp:

    @allure.description("Sign up for verto")
    def test_signup(self):
         cl = TestLogin()
         cl.test_browser_setup(urlarg, Browserarg)
         c2 = SigingUp()
         c2.signup()
         c2.AdminAuth()

         



