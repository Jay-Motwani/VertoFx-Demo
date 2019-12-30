
def GetBrowserPath(Browser):
    if Browser == "chrome":
        path = "../ExtFiles/chromedriver.exe"
        return path


def getfile(Filename):
    if Filename == "vertofx1":
        path = "../Data/Vertofx1.xlsx"
        return path

def GetUrl(Websitename):
    if Websitename == "uat":
        url = "https://uat.vertofx.com"
        return url