
import pandas as pd


class ReadingFile:
    global sheet_n
    sheet_n = []
    global emaillist
    emaillist = []
    global passlist
    passlist = []
    global otplist
    otplist = []
    global fnamelist
    fnamelist = []
    global lnamelist
    lnamelist = []
    global cclist
    cclist = []
    global phnumlist
    phnumlist = []


    def datam(p, sheetname):
        Data = pd.read_excel(p, sheetname)
        return Data

    def getallrows(p, sheetname):
        Data = ReadingFile.datam(p, sheetname)
        tot_rows = len(Data.axes[0])
        return tot_rows

    def getinput(path, sheetname):

        xl = pd.ExcelFile(path)
        all_sheets = xl.sheet_names

        d = len(all_sheets)

        for i in range(0, d):
            name = all_sheets[i]
            sheet_n.append(name)

            if sheetname in sheet_n:
                data = ReadingFile.datam(path, sheetname)
        return data

    def getemails(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        emaillist.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                email = data.at[j, "email"]
                emaillist.append(email)

        return emaillist


    def getFirstnanme(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        fnamelist.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                name = data.at[j, "first name"]
                fnamelist.append(name)

        return fnamelist


    def getpassword(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        passlist.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                passw = data.at[j, "password"]
                passlist.append(passw)
        return passlist

    def getotp(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        otplist.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                otpval = data.at[j, "otp"]
                otplist.append(otpval)
        return otplist


    def getLastname(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        lnamelist.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                lname = data.at[j, "last name"]
                lnamelist.append(lname)
        return lnamelist

    def getCountrycode(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        cclist.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                cc = data.at[j, "country code"]
                cclist.append(cc)
        return cclist

    def getPhonenumber(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        phnumlist.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                cc = data.at[j, "phone number"]
                phnumlist.append(cc)
        return phnumlist
