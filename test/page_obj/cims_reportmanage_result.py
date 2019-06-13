# coding:utf-8
from test.page_obj.cims_reportmanage_model import ReportManagementModule
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ReportManagementResult(ReportManagementModule):

    def send_report_result_links(self):
        ReportManagementModule.send_report(self)
        send_report_message = self.find_element(By.ID, "btnRemove").get_attribute("value")
        return send_report_message

    def email_template_result(self):
        ReportManagementModule.email_template(self)
        self.implicitly_wait(20)
        email_template_message = self.find_element(By.ID, "btCancel").get_attribute("value")
        return email_template_message

    def report_result(self):
        ReportManagementModule.report(self)
        self.implicitly_wait(10)
        time.sleep(20)
        report_message = self.find_element(By.ID, "gvReport_ctl02_lblReportName").get_attribute("value")
        return report_message

    def ddas_result(self):
        ReportManagementModule.ddasreportnotification(self)
        self.implicitly_wait(10)
        ddas_message = self.find_element(By.CSS_SELECTOR, "#apUpdate>table>tbody>tr>td>span").get_attribute("value")
        return ddas_message

    def reportparament_result(self):
        ReportManagementModule.reportparameter(self)
        self.implicitly_wait(10)
        reportparameter_message = self.find_element(By.CSS_SELECTOR, '.list_1>th:nth-child(3)>a').get_attribute("value")
        return reportparameter_message

    def reporthistory_result(self):
        ReportManagementModule.reporthistory(self)
        self.implicitly_wait(10)
        # time.sleep(10)
        reporthistory_message = self.find_element(By.CSS_SELECTOR,
                                                  '.search>table>tbody>tr:nth-child(2)>td').get_attribute("value")
        return reporthistory_message

    def etoolgroup_result(self):
        ReportManagementModule.eToolgroup(self)
        self.implicitly_wait(10)
        etoolgroup_message = self.find_element(By.CSS_SELECTOR, '#lstAvailable>option').get_attribute("value")
        return etoolgroup_message

    def etoolsextype_result(self):
        ReportManagementModule.etoolsextype(self)
        self.implicitly_wait(10)
        etoolsextype_message = self.find_element(By.CSS_SELECTOR,
                                                 "#adgrdDetail>tbody>tr:nth-child(3)>td:nth-child(1)").get_attribute("value")
        return etoolsextype_message

    def etoolsecurity_result(self):
        ReportManagementModule.etoolsecurity(self)
        self.implicitly_wait(10)
        etoolsecurity_message = self.find_element(By.CSS_SELECTOR,
                                                  "#gvEToolSecurity_ctl13_lblEToolType").get_attribute("value")
        return etoolsecurity_message

    def etoolwebaccess_result(self):
        ReportManagementModule.etoolsecurity(self)
        self.implicitly_wait(10)
        etoolwebaccess_message = self.find_element(By.ID, "gvPermissionList_ctl02_lblModule").get_attribute("value")
        return etoolwebaccess_message

    def sentemail_result(self):
        ReportManagementModule.send_report(self)
        self.implicitly_wait(10)
        sentemail_message = self.find_element(By.CSS_SELECTOR, ".list_1>th>a").get_attribute("value")
        return sentemail_message

    def lotmatching_result(self):
        ReportManagementModule.lotmatching(self)
        self.implicitly_wait(10)
        lotmatching_message = self.find_element(By.CSS_SELECTOR,
                                                "#dgrdLotMatching>tbody>tr>td:nth-child(2)>a").get_attribute("value")
        return lotmatching_message

    def lotmatchinghistory_result(self):
        ReportManagementModule.lotmatchinghistory(self)
        self.implicitly_wait(10)
        lotmatchinghistory_message = self.find_element(By.CSS_SELECTOR,
                                                       "#dgrdLotMatching>tbody>tr:nth-child(3)>td:nth-child(2)").get_attribute("value")
        return lotmatchinghistory_message

    def codemanager_result(self):
        ReportManagementModule.codemanager(self)
        self.implicitly_wait(10)
        codemanager_message = self.find_element(By.CSS_SELECTOR,
                                                "#dgrdCode>tbody>tr:nth-child(11)>td:nth-child(3)").get_attribute("value")
        return codemanager_message

    def systemfield_result(self):
        ReportManagementModule.systemfield(self)
        self.implicitly_wait(10)
        systemfield_message = self.find_element(By.CSS_SELECTOR,"#gv>tbody>tr>th:nth-child(5)>a").get_attribute("value")
        return systemfield_message

    def fieldmapping_result(self):
        ReportManagementModule.fieldmapping(self)
        self.implicitly_wait(10)
        fieldmapping_message = self.find_element(By.CSS_SELECTOR, ".bodylgb>th:nth-child(1)").get_attribute("value")
        return fieldmapping_message

    def myreport_result(self):
        ReportManagementModule.myreport(self)
        self.implicitly_wait(10)
        myreport_message = self.find_element(By.CSS_SELECTOR, ".list_1>th:nth-child(6)").get_attribute("value")
        return myreport_message

    def htsidataqualityreport_result(self):
        ReportManagementModule.htsidataqualityreport(self)
        self.implicitly_wait(10)
        htsidataqualityreport_message = self.find_element(By.CSS_SELECTOR, ".list_1>th:nth-child(4)").get_attribute("value")
        return htsidataqualityreport_message

    def poultryexcelreport_result(self):
        ReportManagementModule.poultryexcelreport(self)
        self.implicitly_wait(10)
        poultryexcelreport_message = self.find_element(By.CSS_SELECTOR, "#AjaxPanelShowData>span>input").get_attribute("value")
        return poultryexcelreport_message

    def htsidataextract_result(self):
        ReportManagementModule.htsidataextract(self)
        self.implicitly_wait(10)
        htsidataextract_message = self.find_element(By.CSS_SELECTOR,
                                                    "#UpdatePanel1>table>tbody>tr:nth-child(2)>td>table>tbody>tr:nth-child(8)>td:nth-child(2)>span>b").get_attribute("value")
        return htsidataextract_message

    def reportsecurity_result(self):
        ReportManagementModule.reporthistory(self)
        self.implicitly_wait(10)
        reportsecurity_message = self.find_element(By.CSS_SELECTOR, ".list_1>th:nth-child(3)").get_attribute("value")
        return reportsecurity_message

    def ftp_management_result(self):
        ReportManagementModule.ftp_management(self)
        self.implicitly_wait(10)
        ftp_management_message = self.find_element(By.CSS_SELECTOR,
                                                   ".list_1>th:nth-child(6)>a").get_attribute("value")
        return ftp_management_message

    def reports_result(self):
        ReportManagementModule.reports(self)
        self.implicitly_wait(10)
        reports_message = self.find_element(By.CSS_SELECTOR, ".a9").get_attribute("value")
        return reports_message
