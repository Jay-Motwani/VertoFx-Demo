from  sys import argv


global Browserarg
global urlarg
Browserarg, urlarg = argv

def GetBrowserPath(Browserarg):
    if Browserarg == "chrome":
        path = "../ExtFiles/chromedriver.exe"
        return path
    else:
        path = "../ExtFiles/chromedriver.exe"
        return path


def getfile(Filename):
    if Filename == "vertofx1":
        path = "../Data/Vertofx1.xlsx"
        return path

def GetUrl(urlarg):
    if urlarg == "uat":
        url = "https://uat.vertofx.com"
        return url
    else:
        url = "https://uat.vertofx.com"
        return url