from selenium.webdriver import chrome

def StartBrowser():
    global driver
    path = "ExtFiles/chromedriver.exe"
    driver = chrome(executable_path=path)
    driver.get("uat.vertofx.com")
    driver.maximize_window()
    return driver

def CloseBrowser():
    driver.close