# coding: utf-8

from selenium.webdriver.common.by import By
from test.common.Page import Page
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class ReportManagementModule(Page):
    log_username_input = (By.ID, 'txtUserName')
    log_password_input = (By.ID, 'txtPWD')
    log_login_button = (By.ID, 'btnLogin')

    def login(self, usr, pws):
        """ 搜索功能 """
        self.find_element(*self.log_username_input).send_keys(usr)
        self.find_element(*self.log_password_input).send_keys(pws)
        self.find_element(*self.log_login_button).click()

    def send_report(self):
        # Report Management
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR, "#menu5>a>span").click()
        self.switch_to_frame("indexFrame")
        self.implicitly_wait(10)
        self.switch_to_frame("leftFrame")
        self.implicitly_wait(10)
        # Send Report
        self.find_element(By.CSS_SELECTOR, "#tvModuleTreen0Nodes>table>tbody>tr>td:nth-child(4)>a:nth-child(1)").click()
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR, "#tvModuleTreen0Nodes>table>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
        self.switch_to_parent_frame()
        self.switch_to_frame("contentFrame")
        time.sleep(2)

    def email_template(self):

        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR, "#menu5>a>span").click()
        self.switch_to_frame("indexFrame")
        self.implicitly_wait(10)
        self.switch_to_frame("leftFrame")
        self.implicitly_wait(10)
        # Email Template
        # self.switch_to_parent_frame()
        # self.switch_to_frame("leftFrame")
        # self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR,
                          "#tvModuleTreen0Nodes>table>tbody>tr>td:nth-child(4)>a:nth-child(1)").click()
        self.find_element(By.CSS_SELECTOR,
                          "#tvModuleTreen0Nodes>table:nth-child(2)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
        self.implicitly_wait(10)
        self.switch_to_parent_frame()
        self.switch_to_frame("contentFrame")
        time.sleep(10)
        self.find_element(By.ID, "ibtnSearch")
        add_new = WebDriverWait(self, 20, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#ibtnChange")))
        add_new.click()

    # Report
    def report(self):
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR, "#menu5>a>span").click()
        self.switch_to_frame("indexFrame")
        self.switch_to_frame("leftFrame")
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR, "#tvModuleTreen0Nodes>table>tbody>tr>td:nth-child(4)>a:nth-child(1)").click()
        self.implicitly_wait(20)
        self.find_element(By.CSS_SELECTOR,
                          "#tvModuleTreen0Nodes>table:nth-child(3)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
        self.implicitly_wait(30)
        self.switch_to_parent_frame()
        self.switch_to_frame("contentFrame")
        self.implicitly_wait(30)
        time.sleep(5)
        self.find_element(By.ID, "ibtnSearch").click()

        self.implicitly_wait(20)
        self.find_element(By.CSS_SELECTOR,"#gvReport_ctl02_ibtnEdit").click()
        self.implicitly_wait(20)
        time.sleep(5)
        self.find_element(By.CSS_SELECTOR,"#gvReport_ctl02_ibtnCancel").click()

    # DDAS Report Notification
    def ddasreportnotification(self):
        self.find_element(By.CSS_SELECTOR, "#menu5>a>span").click()
        self.switch_to_frame("indexFrame")
        self.switch_to_frame("leftFrame")
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR, "#tvModuleTreen0Nodes>table>tbody>tr>td:nth-child(4)>a:nth-child(1)").click()
        self.implicitly_wait(20)
        self.find_element(By.CSS_SELECTOR,
                          "#tvModuleTreen0Nodes>table:nth-child(4)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
        self.implicitly_wait(10)
        self.switch_to_parent_frame()
        self.switch_to_frame("contentFrame")

    # Report Parameter
    def reportparameter(self):
        self.find_element(By.CSS_SELECTOR, "#menu5>a>span").click()
        self.switch_to_frame("indexFrame")
        self.switch_to_frame("leftFrame")
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR, "#tvModuleTreen0Nodes>table>tbody>tr>td:nth-child(4)>a:nth-child(1)").click()
        self.implicitly_wait(20)
        self.find_element(By.CSS_SELECTOR,
                          "#tvModuleTreen0Nodes>table:nth-child(5)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
        self.switch_to_parent_frame()
        self.switch_to_frame("contentFrame")
        self.implicitly_wait(10)
        time.sleep(2)
        reportname = self.find_element(By.ID, "dropReport")
        Select(reportname).select_by_value("6")
        self.implicitly_wait(10)
        time.sleep(2)
        self.find_element(By.ID, "btnSearch").click()

    # Report History
    def reporthistory(self):
        self.find_element(By.CSS_SELECTOR, "#menu5>a>span").click()
        self.switch_to_frame("indexFrame")
        self.switch_to_frame("leftFrame")
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR, "#tvModuleTreen0Nodes>table>tbody>tr>td:nth-child(4)>a:nth-child(1)").click()
        self.implicitly_wait(20)
        self.find_element(By.CSS_SELECTOR,
                          "#tvModuleTreen0Nodes>table:nth-child(6)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
        self.switch_to_parent_frame()
        self.switch_to_frame("contentFrame")
        self.implicitly_wait(10)
        Contact = self.find_element(By.CSS_SELECTOR,"#dropContact")
        Select(Contact).select_by_value("15876")
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR,"#ibtnSearch").click()
        self.implicitly_wait(10)

        # ETool Group
    def eToolgroup(self):
        self.find_element(By.CSS_SELECTOR, "#menu5>a>span").click()
        self.switch_to_frame("indexFrame")
        self.switch_to_frame("leftFrame")
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR, "#tvModuleTreen0Nodes>table>tbody>tr>td:nth-child(4)>a:nth-child(1)").click()
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR,
                          "#tvModuleTreen0Nodes>table:nth-child(7)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
        self.implicitly_wait(10)
        self.switch_to_parent_frame()
        self.switch_to_frame("contentFrame")
        user = self.find_element(By.ID, "dropUser")
        Select(user).select_by_value("15876")
        self.implicitly_wait(20)
        time.sleep(2)
        etool = self.find_element(By.ID, "dropETool")
        Select(etool).select_by_value("WebTool|760")
        self.implicitly_wait(20)
        time.sleep(2)
        account = self.find_element(By.ID, "dropAccount")
        Select(account).select_by_value("AccountID|10233")

        # ETook SexType
    def etoolsextype(self):
        self.find_element(By.CSS_SELECTOR, "#menu5>a>span").click()
        self.switch_to_frame("indexFrame")
        self.switch_to_frame("leftFrame")
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR, "#tvModuleTreen0Nodes>table>tbody>tr>td:nth-child(4)>a:nth-child(1)").click()
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR,
                          "#tvModuleTreen0Nodes>table:nth-child(8)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
        self.switch_to_parent_frame()
        self.switch_to_frame("contentFrame")
        etooltype = self.find_element(By.CSS_SELECTOR,"#dropEToolType")
        # Days on Feed Calculator
        Select(etooltype).select_by_value("367")
        self.implicitly_wait(10)
        time.sleep(2)

        # ETool Security
    def etoolsecurity(self):
        self.find_element(By.CSS_SELECTOR, "#menu5>a>span").click()
        self.switch_to_frame("indexFrame")
        self.switch_to_frame("leftFrame")
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR, "#tvModuleTreen0Nodes>table>tbody>tr>td:nth-child(4)>a:nth-child(1)").click()
        self.implicitly_wait(20)
        self.switch_to_parent_frame()
        self.switch_to_frame("leftFrame")
        self.find_element(By.CSS_SELECTOR,
                          "#tvModuleTreen0Nodes>table:nth-child(9)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
        self.switch_to_parent_frame()
        self.switch_to_frame("contentFrame")
        contact = self.find_element(By.CSS_SELECTOR,"#dropContact")
        Select(contact).select_by_value("15876")
        self.implicitly_wait(20)
        time.sleep(5)
        self.find_element(By.CSS_SELECTOR,"#ibtnSearch").click()
        self.implicitly_wait(10)
        time.sleep(5)

        # ETool Web Access
    def etoolwebaccess(self):
        self.find_element(By.CSS_SELECTOR, "#menu5>a>span").click()
        self.switch_to_frame("indexFrame")
        self.switch_to_frame("leftFrame")
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR, "#tvModuleTreen0Nodes>table>tbody>tr>td:nth-child(4)>a:nth-child(1)").click()
        self.implicitly_wait(20)
        self.switch_to_parent_frame()
        self.switch_to_frame("leftFrame")
        self.find_element(By.CSS_SELECTOR,
                          "#tvModuleTreen0Nodes>table:nth-child(10)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
        self.switch_to_parent_frame()
        self.switch_to_frame("contentFrame")
        self.implicitly_wait(10)
        time.sleep(2)
        etool = self.find_element(By.CSS_SELECTOR,"#dropETool")
        Select(etool).select_by_value("760")
        self.implicitly_wait(10)
        time.sleep(2)
        contact = self.find_element(By.CSS_SELECTOR,"#dropContact")
        Select(contact).select_by_value("15876")
        self.implicitly_wait(10)
        time.sleep(2)
        account = self.find_element(By.CSS_SELECTOR,"#dropAccount")
        Select(account).select_by_value("10233")
        self.implicitly_wait(10)
        time.sleep(2)

        # Sent Emails
    def sentemail(self):
        self.find_element(By.CSS_SELECTOR, "#menu5>a>span").click()
        self.switch_to_frame("indexFrame")
        self.switch_to_frame("leftFrame")
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR, "#tvModuleTreen0Nodes>table>tbody>tr>td:nth-child(4)>a:nth-child(1)").click()
        self.implicitly_wait(20)
        self.switch_to_parent_frame()
        self.switch_to_frame("leftFrame")
        self.find_element(By.CSS_SELECTOR,
                          "#tvModuleTreen0Nodes>table:nth-child(11)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
        self.switch_to_parent_frame()
        self.switch_to_frame("contentFrame")
        se_contact = self.find_element(By.CSS_SELECTOR,"#dropContactEmail")
        Select(se_contact).select_by_value("15876")
        self.find_element(By.CSS_SELECTOR,"#btnSearch").click()
        self.implicitly_wait(10)
        time.sleep(2)

        # LotMatching
    def lotmatching(self):
        self.find_element(By.CSS_SELECTOR, "#menu5>a>span").click()
        self.switch_to_frame("indexFrame")
        self.switch_to_frame("leftFrame")
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR, "#tvModuleTreen0Nodes>table>tbody>tr>td:nth-child(4)>a:nth-child(1)").click()
        self.implicitly_wait(20)
        self.switch_to_parent_frame()
        self.switch_to_frame("leftFrame")
        self.find_element(By.CSS_SELECTOR,
                          "#tvModuleTreen0Nodes>table:nth-child(12)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
        self.switch_to_parent_frame()
        self.switch_to_frame("contentFrame")
        lm_ba = self.find_element(By.CSS_SELECTOR,"#Table1>tbody>tr:nth-child(3)>td>select")
        Select(lm_ba).select_by_value("15876")
        self.implicitly_wait(10)
        time.sleep(2)

        # LotMatching History
    def lotmatchinghistory(self):
        self.find_element(By.CSS_SELECTOR, "#menu5>a>span").click()
        self.switch_to_frame("indexFrame")
        self.switch_to_frame("leftFrame")
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR, "#tvModuleTreen0Nodes>table>tbody>tr>td:nth-child(4)>a:nth-child(1)").click()
        self.implicitly_wait(20)
        self.switch_to_parent_frame()
        self.switch_to_frame("leftFrame")
        self.find_element(By.CSS_SELECTOR,
                          "#tvModuleTreen0Nodes>table:nth-child(13)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
        self.switch_to_parent_frame()
        self.switch_to_frame("contentFrame")
        company = self.find_element(By.ID, "dropCompany")
        # Oppliger Feeders
        Select(company).select_by_value("1000064")
        time.sleep(2)
        self.find_element(By.CSS_SELECTOR,"#btnSearch").click()
        self.implicitly_wait(10)
        time.sleep(2)

        # Code Manager
    def codemanager(self):
        self.find_element(By.CSS_SELECTOR, "#menu5>a>span").click()
        self.switch_to_frame("indexFrame")
        self.switch_to_frame("leftFrame")
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR, "#tvModuleTreen0Nodes>table>tbody>tr>td:nth-child(4)>a:nth-child(1)").click()
        self.implicitly_wait(20)
        self.switch_to_parent_frame()
        self.switch_to_frame("leftFrame")
        self.find_element(By.CSS_SELECTOR,
                          "#tvModuleTreen0Nodes>table:nth-child(14)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
        self.implicitly_wait(10)
        self.switch_to_parent_frame()
        self.switch_to_frame("contentFrame")
        time.sleep(3)

        self.find_element(By.CSS_SELECTOR, ".bodylgb>td>a").click()
        time.sleep(2)

        # SystemField
    def systemfield(self):
        self.find_element(By.CSS_SELECTOR, "#menu5>a>span").click()
        self.switch_to_frame("indexFrame")
        self.switch_to_frame("leftFrame")
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR, "#tvModuleTreen0Nodes>table>tbody>tr>td:nth-child(4)>a:nth-child(1)").click()
        self.implicitly_wait(20)
        self.find_element(By.CSS_SELECTOR,
                          "#tvModuleTreen0Nodes>table:nth-child(15)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
        self.implicitly_wait(10)
        self.switch_to_parent_frame()
        self.switch_to_frame("contentFrame")
        self.find_element(By.ID, "txtSearchFieldName").send_keys("3")
        self.find_element(By.ID, "btnSearch").click()
        time.sleep(2)

        # Field Mapping
    def fieldmapping(self):
        self.find_element(By.CSS_SELECTOR, "#menu5>a>span").click()
        self.switch_to_frame("indexFrame")
        self.switch_to_frame("leftFrame")
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR, "#tvModuleTreen0Nodes>table>tbody>tr>td:nth-child(4)>a:nth-child(1)").click()
        self.implicitly_wait(20)
        self.find_element(By.CSS_SELECTOR,
                          "#tvModuleTreen0Nodes>table:nth-child(16)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
        self.switch_to_parent_frame()
        self.switch_to_frame("contentFrame")

        fm_dt = self.find_element(By.CSS_SELECTOR,"#dropFileType")
        Select(fm_dt).select_by_value("CloseoutCore")

        FM_Account = self.find_element(By.CSS_SELECTOR,"#dropAccount")
        Select(FM_Account).select_by_value("89008")
        self.implicitly_wait(10)
        # radio button
        self.find_element(By.CSS_SELECTOR,"#radlType_1").send_keys(Keys.SPACE)
        time.sleep(2)

        # My Report
    def myreport(self):
        self.find_element(By.CSS_SELECTOR, "#menu5>a>span").click()
        self.switch_to_frame("indexFrame")
        self.switch_to_frame("leftFrame")
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR, "#tvModuleTreen0Nodes>table>tbody>tr>td:nth-child(4)>a:nth-child(1)").click()
        self.implicitly_wait(20)
        self.find_element(By.CSS_SELECTOR,
                          "#tvModuleTreen0Nodes>table:nth-child(17)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
        self.switch_to_parent_frame()
        self.switch_to_frame("contentFrame")
        MR_Report = self.find_element(By.CSS_SELECTOR,"#dropReport")
        Select(MR_Report).select_by_value("4")
        time.sleep(2)

        # HTSiDataQualityReport
    def htsidataqualityreport(self):
        self.find_element(By.CSS_SELECTOR, "#menu5>a>span").click()
        self.switch_to_frame("indexFrame")
        self.switch_to_frame("leftFrame")
        self.find_element(By.CSS_SELECTOR, "#tvModuleTreen0Nodes>table>tbody>tr>td:nth-child(4)>a:nth-child(1)").click()
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR,
                          "#tvModuleTreen0Nodes>table:nth-child(18)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
        self.switch_to_parent_frame()
        self.switch_to_frame("contentFrame")
        HT_RN = self.find_element(By.CSS_SELECTOR,"#dropReportName")
        # HTS+ Dashboard
        Select(HT_RN).select_by_value("699")
        time.sleep(2)

        # PoultryExcelReport
    def poultryexcelreport(self):
        self.find_element(By.CSS_SELECTOR, "#menu5>a>span").click()
        self.switch_to_frame("indexFrame")
        self.switch_to_frame("leftFrame")
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR, "#tvModuleTreen0Nodes>table>tbody>tr>td:nth-child(4)>a:nth-child(1)").click()
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR,
                          "#tvModuleTreen0Nodes>table:nth-child(19)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
        self.switch_to_parent_frame()
        self.switch_to_frame("contentFrame")
        self.implicitly_wait(10)
        reportname = self.find_element(By.ID,"dropReportName")
        # AllProductionData Published
        Select(reportname).select_by_value("R2")
        self.implicitly_wait(10)
        time.sleep(2)

        # HTSi Data Extract
    def htsidataextract(self):
        self.find_element(By.CSS_SELECTOR, "#menu5>a>span").click()
        self.switch_to_frame("indexFrame")
        self.switch_to_frame("leftFrame")
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR, "#tvModuleTreen0Nodes>table>tbody>tr>td:nth-child(4)>a:nth-child(1)").click()
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR,
                          "#tvModuleTreen0Nodes>table:nth-child(20)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
        self.switch_to_parent_frame()
        self.switch_to_frame("contentFrame")
        self.implicitly_wait(20)
        time.sleep(2)
        HDE_TO = self.find_element(By.CSS_SELECTOR,"#dropTemplateOwner")
        Select(HDE_TO).select_by_value("10777")
        self.find_element(By.CSS_SELECTOR,"#ibtnAddNew").click()
        time.sleep(2)

        # ReportSecurity
    def reportsecurity(self):
        self.find_element(By.CSS_SELECTOR, "#menu5>a>span").click()
        self.switch_to_frame("indexFrame")
        self.switch_to_frame("leftFrame")
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR, "#tvModuleTreen0Nodes>table>tbody>tr>td:nth-child(4)>a:nth-child(1)").click()
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR,
                          "#tvModuleTreen0Nodes>table:nth-child(21)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
        self.switch_to_parent_frame()
        self.switch_to_frame("contentFrame")
        self.implicitly_wait(10)
        time.sleep(2)
        rs_contact = self.find_element(By.CSS_SELECTOR,"#dropContact")
        Select(rs_contact).select_by_value("15876")
        self.implicitly_wait(20)
        self.find_element(By.CSS_SELECTOR,"#btnSearch").click()
        time.sleep(2)

        # FTP Management
    def ftp_management(self):
        self.find_element(By.CSS_SELECTOR, "#menu5>a>span").click()
        self.switch_to_frame("indexFrame")
        self.switch_to_frame("leftFrame")
        self.implicitly_wait(30)
        self.find_element(By.CSS_SELECTOR, "#tvModuleTreen0Nodes>table>tbody>tr>td:nth-child(4)>a:nth-child(1)").click()
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR,
                          "#tvModuleTreen0Nodes>table:nth-child(22)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
        self.switch_to_parent_frame()
        self.switch_to_frame("contentFrame")
        self.implicitly_wait("10")
        time.sleep(2)
        FTPM_Contact = self.find_element(By.CSS_SELECTOR,"#dropContactEmail")
        Select(FTPM_Contact).select_by_value("15876")
        self.find_element(By.CSS_SELECTOR,"#btnSearch").click()
        time.sleep(2)

        # Reports
    def reports(self):
        self.find_element(By.CSS_SELECTOR, "#menu5>a>span").click()
        self.switch_to_frame("indexFrame")
        self.switch_to_frame("leftFrame")
        self.implicitly_wait(30)
        self.find_element(By.CSS_SELECTOR, "#tvModuleTreet23").click()
        self.implicitly_wait(10)
        time.sleep(15)
        # Benchmark
        self.find_element(By.CSS_SELECTOR, "#tvModuleTreet24").click()
        self.implicitly_wait(10)
        time.sleep(15)
        # Benchmark Monthly Consultant Report
        self.find_element(By.CSS_SELECTOR,
                          "#tvModuleTreen23Nodes>div>table>tbody>tr>td:nth-child(6)>a:nth-child(2)").click()
        self.switch_to_parent_frame()
        self.switch_to_frame("contentFrame")
        self.implicitly_wait(30)
        # AccountGroup
        RBB_AG = self.find_element(By.CSS_SELECTOR, "#rpwDisplay_ctl00_ctl03_ddValue")
        Select(RBB_AG).select_by_value("1")
        # View Report
        self.find_element(By.CSS_SELECTOR, "#rpwDisplay_ctl00_ctl00").click()
        self.implicitly_wait(15)
        time.sleep(20)
        # 下一页
        self.find_element(By.CSS_SELECTOR, "#rpwDisplay_ctl01_ctl01_ctl05_ctl00>tbody>tr>td>input").click()
        self.implicitly_wait(10)
        # PDF
        format_select = self.find_element(By.CSS_SELECTOR, "#rpwDisplay_ctl01_ctl05_ctl00")
        Select(format_select).select_by_value("PDF")
        # Export
        self.find_element(By.CSS_SELECTOR, "#rpwDisplay_ctl01_ctl05_ctl01").click()
        self.implicitly_wait(10)
        """
        self.switch_to_parent_frame()
        self.switch_to_frame("leftFrame")
        self.implicitly_wait(10)
        self.find_element(By.CSS_SELECTOR,
                          "#tvModuleTreen24Nodes>table:nth-child(2)>tbody>tr>td:nth-child(6)>a:nth-child(2)").click()
        self.switch_to_parent_frame()
        self.switch_to_frame("contentFrame")
        self.implicitly_wait(10)
        # GroupName
        GroupName = self.find_element(By.CSS_SELECTOR, "#rpwDisplay_ctl00_ctl03_ddValue")
        Select(GroupName).select_by_value("2")
        self.find_element(By.CSS_SELECTOR, "#rpwDisplay_ctl00_ctl00").click()
        self.implicitly_wait(15)
        time.sleep(15)
        # 下一页
        self.find_element(By.CSS_SELECTOR, "#rpwDisplay_ctl01_ctl01_ctl05_ctl00>tbody>tr>td>input").click()
        self.implicitly_wait(10)
        # PDF
        format_select = self.find_element(By.CSS_SELECTOR, "#rpwDisplay_ctl01_ctl05_ctl00")
        Select(format_select).select_by_value("PDF")
        # Export
        self.find_element(By.CSS_SELECTOR, "#rpwDisplay_ctl01_ctl05_ctl01").click()
        self.implicitly_wait(15)
        """
        time.sleep(5)
