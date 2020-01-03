import os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from Base import Paths, ReadExcel
from Base.AuthorizeNewUser import Authorize
from Base.VertoUtil import Utilities



class SignUpproc:
    def __init__(self, driver):

        self.driver = driver
        self.signup = "Sign up"
        self.email = "email"
        self.password = "password"
        self.cpas = "confirmPassword"
        self.firstName = "firstName"
        self.lastName = "lastName"
        self.cc = "countryCode"
        self.phnnum = "phone"
        self.SignupBtn = ".btn.btn-custom-navy.w-100[type='submit']"
        self.RefralCode = " Have referral code? "
        self.ReSendOtpBtn = ".btn.btn-custom-navy-outline.w-100[type='button']"
        self.mails = ".even pointer ng-scope[ng-repeat='email in emails']"
        self.mailframe = "iframe#id='msg_body'"
        self.verlink = "Verify my e-mail"
        self.buscondd = "country"
        self.rbusname = "companyName"
        self.comnum = "companyNumber"
        self.busweb = "companyWebsite"
        self.address = "addressLine1"
        self.pin = "zipcode"
        self.city = "addressLine2"
        self.bustype = "companyType"
        self.buscat = "companyCategory"
        self.role = "companyRole"
        self.empnum = "companyNumberOfEmployees"
        self.nextbtn = ".btn.btn-sm.btn-custom-navy"
        self.conchkbx = ".mat-checkbox-inner-container"
        self.nextbdbtn = ".btn.btn-sm.btn-custom-navy.ng-star-inserted"
        self.docdd = "select.form-control"
        self.UploadInp = "input[accept='*']"
        self.UploadBtn = ".m-t-5.btn.btn-sm.btn-custom-navy"
        self.ownerfname = "ownerFirstName"
        self.ownerlname = "ownerLastName"
        self.ownertele = "ownerTelephone"
        self.owneremail = "ownerEmail"
        self.ownerdob = "ownerDob"
        self.ownerper = "percentOwnershipInCompany"
        self.personaladd1 = "personalAddressLine1"
        self.personalpin = "personalZipcode"
        self.personalcity = "personalAddressLine2"
        self.personcountry = "personalCountry"
        self.dashbflex = ".flex-1.bg-warning.padd-2"
        self.lgodd = "div.inline.v-mid.text-left"
        self.lgout = "a[href='/auth/logout']"




    def InitiateSignUP(self):
        global util
        util = Utilities()
        signupbtn = self.driver.find_element_by_link_text(self.signup)

        util.DynamicWait(signupbtn)
        util.Click_Element(signupbtn)
        util.DynamicWait(By.name, self.firstName)

    def FillActivationForm(self, fname, lname, email, cc, phn, pas):
        self.driver.find_element_by_name(self.firstName).send_keys(fname)
        self.driver.find_element_by_name(self.lastName).send_keys(lname)
        self.driver.find_element_by_name(self.email).send_keys(email)
        ccd = self.driver.find_element_by_name(self.cc)
        util.Click_Element(ccd)
        Select(ccd).select_by_value(cc)
        self.driver.find_element_by_name(self.phnnum).send_keys(phn)
        self.driver.find_element_by_name(self.password).send_keys(pas)
        self.driver.find_element_by_name(self.cpas).send_keys(pas)
        submit = self.driver.find_element_by_css_selector(self.SignupBtn)
        util.Click_Element(submit)
        util.WaitForProgressSpinner()

    def ConfirmMail(self, email):
        m = email.replace("@mailinator.com", "")
        mailurl = "https://www.mailinator.com/v3/index.jsp?zone=public&query="
        self.driver.get(mailurl)
        util.DynamicWait(self.mails)
        vmail = self.driver.find_element_by_css_selector(self.mails)
        util.Click_Element(vmail)
        util.DynamicWait(self.mailframe)
        self.driver.switch_to.frame(self.driver.find_element_by_css_selector(self.mailframe))
        util.DynamoWait(By.PARTIAL_LINK_TEXT, self.verlink)
        util.Click_Element(self.driver.find_element_by_partial_link_text(self.verlink))
        util.switch_window()

    def SelectBusCountry(self, buscon):
        bcdd = self.driver.find_element_by_name(self.buscondd)
        util.Click_Element(bcdd)
        Select(bcdd).select_by_value(buscon)
        util.DynamoWait(By.NAME, self.rbusname)

    def FillBusDetails(self, rbname, comnum, busweb, address, pin, city, bustype, buscat, role, empn):
        self.driver.find_element_by_name(self.rbusname).send_keys(rbname)
        self.driver.find_element_by_name(self.comnum).send_keys(comnum)
        self.driver.find_element_by_name(self.busweb).send_keys(busweb)
        nextbtn = self.driver.find_elements(By.CSS_SELECTOR, self.nextbtn)
        util.Click_Element(nextbtn[0])
        util.DynamoWait(By.NAME, self.address)
        self.driver.find_element_by_name(self.address).send_keys(address)
        self.driver.find_element_by_name(self.pin).send_keys(pin)
        self.driver.find_element_by_name(self.city).send_keys(city)
        nextbtn = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-sm.btn-custom-navy.m-l-10")
        util.Click_Element(nextbtn)
        util.DynamoWait(By.NAME, self.bustype)
        busty = self.driver.find_element_by_name(self.bustype)
        util.Click_Element(busty)
        Select(busty).select_by_visible_text(bustype)
        busca = self.driver.find_element_by_name(self.buscat)
        util.Click_Element(busca)
        Select(busca).select_by_visible_text(buscat)
        rol = self.driver.find_element_by_name(self.role)
        util.Click_Element(rol)
        Select(rol).select_by_visible_text(role)
        self.driver.find_element_by_name(self.empnum).send_keys(empn)
        verchkbx = self.driver.find_element_by_css_selector(self.conchkbx)
        util.Click_Element(verchkbx)
        nextbtn = self.driver.find_elements(By.CSS_SELECTOR, self.nextbtn)
        util.Click_Element(nextbtn[3])
        util.WaitForProgressSpinner()

    def CheckBenificiary(self, option):
        radbtn = self.driver.find_elements(By.CSS_SELECTOR, ".mat-radio-outer-circle")
        if option == "yes":
            util.Click_Element(radbtn[0])
            util.Click_Element(self.driver.find_element_by_css_selector(self.nextbdbtn))
            util.WaitForProgressSpinner()
        elif option == "no":
            util.Click_Element(radbtn[1])
            util.Click_Element(radbtn[2])
            util.Click_Element(self.driver.find_element_by_css_selector(self.nextbdbtn))
            util.WaitForProgressSpinner()
            util.DynamicWait(self.docdd)

    def Uploadfile(self, path):
        upldbtn = self.driver.find_element_by_css_selector(self.UploadBtn)
        UpldInp = self.driver.find_element_by_css_selector(self.UploadInp)
        UpldInp.send_keys(os.getcwd() + path)
        util.Click_Element(upldbtn)
        util.WaitForProgressSpinner()

    def UploadBusDocuments(self, doc1):
        docudd = self.driver.find_element_by_css_selector(self.docdd)
        util.Click_Element(docudd)
        Select(docudd).select_by_visible_text(doc1)
        self.Uploadfile("/Data/drip.png")
        util.WaitForProgressSpinner()

    def FillPersonalDetails(self, fname, lname, tel, dob, email, ownership, peradd, perin, city, country):
        assert self.driver.find_element_by_name(self.ownerfname).getAttribute("value") == fname
        assert self.driver.find_element_by_name(self.ownerfname).getAttribute("value") == lname
        assert self.driver.find_element_by_name(self.ownerfname).getAttribute("value") == tel
        assert self.driver.find_element_by_name(self.ownerfname).getAttribute("value") == email
        self.driver.find_element_by_name(self.ownerdob).send_keys(dob)
        self.driver.find_element_by_name(self.ownerdob).send_keys(Keys.ENTER)
        self.driver.find_element_by_name(self.ownerper).send_keys(ownership)

        util.Click_Element(self.driver.find_element_by_css_selector(self.nextbtn))
        util.DynamoWait(By.NAME, self.personaladd1)

        self.driver.find_element_by_name(self.personaladd1).send_keys(peradd)
        self.driver.find_element_by_name(self.personalpin).send_keys(perin)
        self.driver.find_element_by_name(self.personalcity).send_keys(city)
        countdd = self.driver.find_element_by_name(self.personcountry)
        util.Click_Element(countdd)
        Select(countdd).select_by_value(country)
        nextbtn = self.driver.find_elements(By.CSS_SELECTOR, self.nextbtn)
        util.Click_Element(nextbtn[1])
        util.WaitForProgressSpinner()

    def UploadPersonalDoc(self, doc1):
        docudd = self.driver.find_element_by_css_selector(self.docdd)
        util.Click_Element(docudd)
        Select(docudd).select_by_v==ible_text(doc1)
        self.Uploadfile("/Data/driphydro.jfif")
        util.WaitForProgressSpinner()

    def Logout(self):
        lgout = self.driver.find_element_by_css_selector(self.lgodd)
        util.Click_Element(lgout)
        util.DynamicWait(self.lgout)
        util.Click_Element(self.driver.find_element_by_css_selector(self.lgout))
        util.DynamicWait(self.email)

    def FillQuestionier(self, ans1, ans2):
        answ = self.driver.find_elements(By.CSS_SELECTOR, "input[placeholder='Answer']")
        answ[0].send_keys(ans1)
        answ[1].send_keys(ans2)
        util.Click_Element(self.driver.find_element_by_css_selector(self.nextbtn))
        util.WaitForProgressSpinner()
        util.DynamicWait(self.dashbflex)

        assert self.driver.find_element_by_css_selector(self.dashbflex).getAttribute(
            "background-color") == "rgb(243, 180, 36)";


class SigingUp:
    def __init__(self, driver):

        self.driver = driver
        self.nextbtn = ".btn.btn-sm.btn-custom-navy"
        self.UItext = ".text-gray.m-b-5"

    def readData(self):
        global Fname
        global Lname
        global email
        global password
        global concode
        global country
        global bname
        global compnumm
        global site
        global badd
        global zcode
        global city
        global btype
        global bcat
        global brol
        global emps
        global benowner
        global oper
        global birthd
        global bdoc
        global pdoc
        global pownerper
        global pdob
        global padd
        global pcon
        global pzip
        global pcity
        global phon
        global answ

        path = Paths.getfile("vertofx1")
        sheetname = "signup"
        email = ReadExcel.ReadingFile.getemails(path, sheetname)
        password = ReadExcel.ReadingFile.getpassword(path, sheetname)
        Fname = ReadExcel.ReadingFile.getFirstnanme(path, sheetname)
        Lname = ReadExcel.ReadingFile.getLastname(path, sheetname)
        concode = ReadExcel.ReadingFile.getCountrycode(path, sheetname)
        phon = ReadExcel.ReadingFile.getPhonenumber(path, sheetname)
        sheetname = "activationform"
        country = ReadExcel.ReadingFile.getCountry(path, sheetname)
        bname = ReadExcel.ReadingFile.getbname(path, sheetname)
        compnumm = ReadExcel.ReadingFile.getcomnum(path, sheetname)
        site = ReadExcel.ReadingFile.getwebsite(path, sheetname)
        badd = ReadExcel.ReadingFile.getaddress(path, sheetname)
        zcode = ReadExcel.ReadingFile.getzipcode(path, sheetname)
        city = ReadExcel.ReadingFile.getCity(path, sheetname)
        btype = ReadExcel.ReadingFile.getbtype(path, sheetname)
        bcat = ReadExcel.ReadingFile.getbcat(path, sheetname)
        brol = ReadExcel.ReadingFile.getbrole(path, sheetname)
        emps = ReadExcel.ReadingFile.getempst(path, sheetname)
        benowner = ReadExcel.ReadingFile.getbenOwner(path, sheetname)
        oper = ReadExcel.ReadingFile.getOwnerper(path, sheetname)
        birthd = ReadExcel.ReadingFile.getDOB()
        sheetname = "business_documents"
        bdoc = ReadExcel.ReadingFile.getdocs(path, sheetname)
        sheetname = "personalinfo"
        pownerper = ReadExcel.ReadingFile.getdocs(path, sheetname)
        pdob = ReadExcel.ReadingFile.getDOB(path, sheetname)
        padd = ReadExcel.ReadingFile.getaddress(path, sheetname)
        pcon = ReadExcel.ReadingFile.getCountry(path, sheetname)
        pzip = ReadExcel.ReadingFile.getzipcode(path, sheetname)
        pcity = ReadExcel.ReadingFile.getCity(path, sheetname)
        sheetname = "personal_doc"
        pdoc = ReadExcel.ReadingFile.getdocs(path, sheetname)
        sheetname = "answer"
        answ = ReadExcel.ReadingFile.getanswer(path, sheetname)

    def signup(self):
        self.readData()
        new_var = SignUpproc()
        new_var.InitiateSignUP()
        for i in range(0, len(Fname)):
            new_var.FillActivationForm(Fname[i], Lname[i], email[i], concode[i], phon[i], password[i])
            new_var.ConfirmMail(email[i])
            new_var.SelectBusCountry(country[i])
            new_var.FillBusDetails(bname[i], compnumm[i], site[i], badd[i], zcode[i], city[i], btype[i], bcat[i],
                                   brol[i], emps[i])
            new_var.CheckBenificiary(benowner[i])
            for j in range(0, len(bdoc)):
                new_var.UploadBusDocuments(bdoc[j])
            util.Click_Element(self.driver.find_element_by_css_selector(self.nextbtn))
            util.WaitForProgressSpinner()
            new_var.FillPersonalDetails(Fname[i], Lname[i], phon[i], pdob[i], email[i], pownerper[i], padd[i], pzip[i],
                                        pcity[i], pcon[i])
            for z in range(0, len(pdoc)):
                new_var.UploadPersonalDoc(pdoc[z])
            util.Click_Element(self.driver.find_element_by_css_selector(self.nextbtn))
            util.WaitForProgressSpinner()
            new_var.FillQuestionier(answ[0], answ[1])
            divheader = self.driver.find_elements(By.CSS_SELECTOR, self.UItext)

            assert divheader[0].text == "Company Name"
            assert divheader[1].text == "e-Wallet Balance"
            assert divheader[2].text == "My Open Orders"
            assert divheader[3].text == "My Offers"

            new_var.Logout()

    def AdminAuth(self):
        c3 = Authorize()
        for i in range(0, len(Fname)):
            c3.AdminLoginfun(email[i], Fname[i])
