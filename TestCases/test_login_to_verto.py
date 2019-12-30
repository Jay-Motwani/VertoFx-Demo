from base.initiateBrowser import triggerBrowser
from pages.signInPage import signIn
import pytest
import allure
import time


class TestLogin:
    @allure.description("Launching browser and opening VertoFx")
    @pytest.fixture()
    def test_browser_setup(self):
        global browser
        global driver
        driver = triggerBrowser()
        browser = driver.open_browser("https://uat.vertofx.com")
        browser_title = browser.title
        assert browser_title == "Verto Platform | B2B Currency Exchange Marketplace"
        yield
        driver.close_browser()

    @allure.description("Verifying that login is successful")
    def test_login(self, test_browser_setup):
        sign_in = signIn(browser)
        sign_in.sign_in("anil2012@mailinator.com", "Password@123")
        time.sleep(10)
