from Base import Paths, ReadExcel
from Base.InitiateBrowser import triggerBrowser
from Pages.signInPage import signIn
import pytest
import allure
import time


class TestLogin:
    @allure.description("Launching browser and opening VertoFx")
    @pytest.fixture(scope="session")
    def test_browser_setup(self):
        global browser
        global driver
        global email
        global password
        global otp

        path = Paths.getfile("vertofx1")
        url = Paths.GetUrl("uat")
        sheetname = "credentials"
        email = ReadExcel.ReadingFile.getemails(path, sheetname)
        password = ReadExcel.ReadingFile.getpassword(path, sheetname)
        otp = ReadExcel.ReadingFile.getotp(path, sheetname)

        driver = triggerBrowser()
        browser = driver.open_browser(url, "chrome")
        browser_title = browser.title
        assert browser_title == "Verto Platform | B2B Currency Exchange Marketplace"
        yield
        driver.close_browser()

    @allure.description("Verifying that login is successful")
    def test_login(self):
        sign_in = signIn(browser)
        sign_in.sign_in(email, password, otp)
        time.sleep(10)


if __name__ == '__main__':
    new_var = TestLogin()
    new_var.test_login()