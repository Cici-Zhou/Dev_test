# coding: utf-8

from selenium.webdriver.common.by import By
from test.common.Page import Page
import time


class AccountManagementModule(Page):

    # login
    username_input = (By.CSS_SELECTOR, '#txtUserName')
    pwd_input = (By.CSS_SELECTOR, "#txtPWD")
    login_button = (By.CSS_SELECTOR, "#btnLogin")

    def login(self,usr, pwd):
        self.find_element(*self.username_input).send_keys(usr)
        self.find_element(*self.pwd_input).send_keys(pwd)
        self.find_element(*self.login_button).click()

    # AccountList
    AccountManagement_button = (By.CSS_SELECTOR, "#menu0")
    QuickAccountManagement_button = (By.CSS_SELECTOR, "div#tvModuleTreen0Nodes>table:nth-child(2)>tbody>tr>td:nth-child(4)>a:nth-child(2)")
    AccountList_button = (By.CSS_SELECTOR, "div#tvModuleTreen0Nodes>table:nth-child(1)>tbody>tr>td:nth-child(4)>a:nth-child(2)")
    AccountName_input = (By.CSS_SELECTOR, "#txtAccountName")
    Search_button = (By.CSS_SELECTOR, "#btnSearch")

    def AccountList(self):
        # Account Management
        self.find_element(*self.AccountManagement_button).click()
        self.switch_to_frame("indexFrame")
        self.implicitly_wait(10)
        self.switch_to_frame("leftFrame")
        self.implicitly_wait(10)
        # 点击AccountList,需要先点击其它按钮再点击AccountList,页面才会有响应
        self.find_element(*self.QuickAccountManagement_button).click()
        time.sleep(3)
        self.find_element(*self.AccountList_button).click()
        time.sleep(3)
        self.switch_to_parent_frame()
        self.switch_to_frame("contentFrame")
        self.find_element(*self.AccountName_input).send_keys('0614Test Account')
        self.find_element(*self.Search_button).click()

