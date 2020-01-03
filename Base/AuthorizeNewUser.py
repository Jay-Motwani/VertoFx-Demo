from Base.VertoUtil import Utilities
from Base.login_to_verto import TestLogin
from Pages.signInPage import signIn


class Authorize:
    def __init__(self, driver):
        self.driver = driver
        self.notifbell = ".icon.v-mid"
        self.viewall = ".btn.btn-sm.btn-custom-navy.bottomed"
        self.notiftext = ".text-navy.m-b-0.nowrap"
        self.toggeldd = ".accordion-toggle"
        self.documenttext = ".m-b-5.text-navy.small"
        self.button =".btn.btn-sm.btn-custom-navy.w-100"
        self.kyctoggel =".mat-slide-toggle-thumb"
        self.seealluser = "VIEW ALL USERS"
        self.username = ".text-gray.small.m-b-5"
        self.searchuser = "input[placeholder='Search users']"
        self.flexoutline = ".m-3.flex.outline.small.clip.pointer"
        self.entries = ".light-border.number.pointer.relative"
        self.wallets = "div.light-border.flex.padding.pointer"

    def AdminLoginfun(self, email, uname):
        sign_in = signIn()
        sign_in.sign_in("admin@vertofx.com", "vertofx123", "1133")
        util = Utilities()
        util.Click_Element(self.driver.find_element_by_css_selector(self.notifbell))
        util.Click_Element(self.driver.find_element_by_css_selector(self.viewall))
        util.DynamicWait(self.notiftext)
        nottext = self.driver.find_elements_by_css_selector(self.notiftext)
        for i in range (0, len(nottext)):
            if email in nottext[i].text:
                x = i
                break
        util.Click_Element(nottext[x])
        util.WaitForProgressSpinner()
        util.DynamicWait(self.seealluser)

        util.Click_Element(self.driver.find_element_by_link_text(self.seealluser))
        util.DynamicWait(self.username)
        users = self.driver.find_elements_by_css_selector(self.username)

        for c in range(0, len(users)):
            if uname in users[c].text:
                n = c
                break
        util.Click_Element(users[n])
        util.DynamicWait(self.toggeldd)

        util.Click_Element(self.driver.find_elements_by_css_selector(self.toggeldd)[0])
        docs = self.driver.find_elements_by_css_selector(self.documenttext)

        for j in range(0, len(docs)):
            util.Click_Element(docs[j])
            util.DynamicWait(self.button)
            util.Click_Element(self.driver.find_elements_by_css_selector(self.button)[1])

        util.Click_Element(self.driver.find_element_by_css_selector(self.kyctoggel))
        util.WaitForProgressSpinner()

        self.driver.find_element_by_css_selector(self.searchuser).send_keys(uname)
        tabs = self.driver.find_element_by_css_selector(self.flexoutline).find_elements_by_tag_name("div")
        util.Click_Element(tabs[1])
        util.DynamicWait(self.entries)
        assert len(self.driver.find_elements_by_css_selector(self)) > 0
        util.Click_Element(self.driver.find_elements_by_css_selector(self))










