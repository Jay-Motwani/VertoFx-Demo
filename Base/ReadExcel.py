
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
    global countryls
    countryls = []
    global bname
    bname = []
    global compnum
    compnum = []
    global website
    website = []
    global address
    address = []
    global pin
    pin = []
    global city
    city =[]
    global btype
    btype = []
    global bcat
    bcat =[]
    global brol
    brol = []
    global emp
    emp = []
    global benfowner
    benfowner = []
    global ownershp
    ownershp = []
    global DOB
    DOB = []
    global doc
    doc=[]
    global ans
    ans =[]
    global wname
    wname = []
    global amt
    amt = []




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

    def getCountry(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        countryls.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                cc = data.at[j, "country"]
                countryls.append(cc)
        return countryls

    def getbname(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        bname.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                cc = data.at[j, "business_name"]
                bname.append(cc)
        return bname

    def getcomnum(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        compnum.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                cc = data.at[j, "company_number"]
                compnum.append(cc)
        return compnum

    def getwebsite(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        website.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                cc = data.at[j, "business_website"]
                website.append(cc)
        return website

    def getaddress(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        address.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                cc = data.at[j, "address"]
                address.append(cc)
        return address

    def getzipcode(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        pin.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                cc = data.at[j, "zip_code"]
                pin.append(cc)
        return pin

    def getCity(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        city.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                cc = data.at[j, "city"]
                city.append(cc)
        return city

    def getbtype(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        btype.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                cc = data.at[j, "business_type"]
                btype.append(cc)
        return btype

    def getbcat(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        bcat.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                cc = data.at[j, "business_category"]
                bcat.append(cc)
        return bcat

    def getbrole(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        brol.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                cc = data.at[j, "role"]
                brol.append(cc)
        return brol

    def getempst(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        emp.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                cc = data.at[j, "emp_strength"]
                emp.append(cc)
        return emp

    def getbenOwner(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        benfowner.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                cc = data.at[j, "beneficial_owner"]
                benfowner.append(cc)
        return benfowner

    def getOwnerper(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        ownershp.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                cc = data.at[j, "ownership in company"]
                ownershp.append(cc)
        return ownershp

    def getDOB(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        DOB.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                cc = data.at[j, "date_of_birth"]
                DOB.append(cc)
        return DOB

    def getdocs(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        doc.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                cc = data.at[j, "doc"]
                doc.append(cc)
        return doc

    def getanswer(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        ans.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                cc = data.at[j, "answer1"]
                ans.append(cc)
        return ans

    def getwalletname(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        wname.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                cc = data.at[j, "doc"]
                wname.append(cc)
        return wname

    def getamount(path, sheetname):
        data = ReadingFile.getinput(path, sheetname)
        total_rows = ReadingFile.getallrows(path, sheetname)
        amt.clear()
        if total_rows > 0:
            for j in range(0, total_rows):
                cc = data.at[j, "doc"]
                amt.append(cc)
        return amt