import sys
from sys import argv



global browser
global url
url = str(sys.argv[2])
browser = str(sys.argv[1])

def GetBrowserPath(browser):
    if browser == "chrome":
        path = "../ExtFiles/chromedriver.exe"
        return path
    else:
        path = "../ExtFiles/chromedriver.exe"
        return path


def getfile(Filename):
    if Filename == "vertofx1":
        path = "../Data/Vertofx1.xlsx"
        return path

def GetUrl(url):
    if url == "uat":
        url1 = "https://uat.vertofx.com"
        return url1
    else:
        url = "https://uat.vertofx.com"
        return url