from builtins import print
import array

import pandas as pd


class ReadingFile:
    global sheet_n
    sheet_n = []
    global colarr
    colarr =[]

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
        colarr.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                email = data.at[j, "email"]
                colarr.append(email)

        return colarr


    def getFirstnanme(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        colarr.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                name = data.at[j, "first name"]
                colarr.append(name)

        return colarr


    def getpassword(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        colarr.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                passw = data.at[j, "password"]
                colarr.append(passw)
        return colarr

    def getotp(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        colarr.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                otpval = data.at[j, "otp"]
                colarr.append(otpval)
        return colarr


    def getLastname(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        colarr.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                lname = data.at[j, "last name"]
                colarr.append(lname)
        return colarr

    def getCountrycode(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        colarr.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                cc = data.at[j, "country code"]
                colarr.append(cc)
        return colarr

    def getPhonenumber(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        colarr.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                cc = data.at[j, "phone number"]
                colarr.append(cc)
        return colarr

