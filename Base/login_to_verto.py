import sys

import allure
from Base import Paths, ReadExcel
from Base.InitiateBrowser import triggerBrowser
from Pages.signInPage import signIn
import time

global browser1
global url
url = str(sys.argv[1])
browser1 = str(sys.argv[2])


class TestLogin:
    def readData(self):
        global email
        global password
        global otp
        path = Paths.getfile("vertofx1")
        sheetname = "credentials"
        email = ReadExcel.ReadingFile.getemails(path, sheetname)
        password = ReadExcel.ReadingFile.getpassword(path, sheetname)
        otp = ReadExcel.ReadingFile.getotp(path, sheetname)

    @allure.description("Launching browser and opening VertoFx")
    def test_browser_setup(self, url, browser1):
        global browser
        global driver

        url = Paths.GetUrl(url)

        driver = triggerBrowser()
        browser = driver.open_browser(url, browser1)
        browser_title = browser.title
        assert browser_title == "Verto Platform | B2B Currency Exchange Marketplace"

    @allure.description("Verifying that login is successful")
    def test_login(self):
        sign_in = signIn(browser)
        s = len(email)
        if s == 1:
            sign_in.sign_in(email[0], password[0], str(otp[0]))
        elif s > 1:
            for i in range(0, s):
                sign_in.sign_in(email[i], password[i], str(otp[i]))
        time.sleep(10)

    @allure.description("Closing browser")
    def test_close_browser(self):
        driver.close_browser()




if __name__ == "__main__":
    new_var = TestLogin()
    new_var.test_browser_setup(url, browser1)
    new_var.test_login()
    new_var.test_close_browser()
