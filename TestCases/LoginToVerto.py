from Base import InitiateBrowser
from Pages import Sign_In_Page


def Login():
    driver = InitiateBrowser.StartBrowser()
    Sign_In_Page.SignIn.Sign_In("anil2611@mailinator.com","Password@123")
    print("Singed in.")
