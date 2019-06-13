# author: Cici Zhou
# -*- coding:utf-8 -*-

import unittest
from selenium.webdriver.common.by import By
from test.models.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH
from test.models.log import logger
from test.models.filereader import ExcelReader
from test.models.HTMLTestRunner_PY3 import HTMLTestRunner
from test.page_obj.cims_accountmanage_model import AccountManagementModule
from test.page_obj.cims_reportmanage_model import ReportManagementModule
from test.page_obj.cims_reportmanage_result import ReportManagementResult
from test.common.Page import Page


class TestCIMS(unittest.TestCase):
    CIMSURL = Config().yaml_get('CIMSURL')
    excel = DATA_PATH + '/Thirdpartyuser.xlsx'

    def sub_setUp(self):
        #self.Account_Management_page = AccountManagementModule(browser_type='chrome').get(self.URL, maximize_window=False)
        self.page = Page(browser_type= 'Chrome').get(self.CIMSURL, maximize_window=False)
        self.Report_Management_page = ReportManagementModule(browser_type='Chrome').get(self.CIMSURL, maximize_window=False)

    def sub_tearDown(self):
        # self.Account_Management_page.quit()
        self.Report_Management_page.quit()

    def login_success(self):
        # self.Account_Management_page.login('Cici.zhou@itlogica.com', 'Qwe0416!@#')
        self.Report_Management_page.login('Cici.zhou@itlogica.com', 'Qwe0516!@#')

    def test_login(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            self.sub_setUp()
            self.page.login(d['User'], d['Password'])
            self.sub_tearDown()
    
    def test_01report_list(self):
        self.sub_setUp()
        self.login_success()
        self.Report_Management_page = ReportManagementResult(self.Report_Management_page)
        send_report_message = self.Report_Management_page.send_report_result_links()
        self.assertEqual(send_report_message, 'Remove')
        logger.info(send_report_message)
        self.tearDown()
    
    def test_02email_template(self):
        self.sub_setUp()
        self.login_success()
        self.Report_Management_page = ReportManagementResult(self.Report_Management_page)
        email_template_message = self.Report_Management_page.email_template_result()
        self.assertEqual(email_template_message, 'Cancel')
        logger.info(email_template_message)
        self.tearDown()
    
    def test_03report(self):
        self.sub_setUp()
        self.login_success()
        self.Report_Management_page = ReportManagementResult(self.Report_Management_page)
        report_message = self.Report_Management_page.report_result()
        print(report_message)
        #self.assertEqual(report_message, 'Search')
        logger.info(report_message)
        self.tearDown()

    def test_04ddas(self):
        self.sub_setUp()
        self.login_success()
        self.Report_Management_page = ReportManagementResult(self.Report_Management_page)
        ddas_message = self.Report_Management_page.ddas_result()
        logger.info(ddas_message)
        self.tearDown()

    def test_05reportparameter(self):
        self.sub_setUp()
        self.login_success()
        self.Report_Management_page = ReportManagementResult(self.Report_Management_page)
        reportparameter_message = self.Report_Management_page.reportparament_result()
        logger.info(reportparameter_message)
        self.tearDown()
    
    def test_06reporthistory(self):
        self.sub_setUp()
        self.login_success()
        self.Report_Management_page = ReportManagementResult(self.Report_Management_page)
        reporthistory_message = self.Report_Management_page.reporthistory_result()
        logger.info(reporthistory_message)
        self.tearDown()
    
    def test_07etoolgroup(self):
        self.sub_setUp()
        self.login_success()
        self.Report_Management_page = ReportManagementResult(self.Report_Management_page)
        etoolgroup_message = self.Report_Management_page.etoolgroup_result()
        self.assertEqual(etoolgroup_message, 'Sgroup')
        logger.info(etoolgroup_message)
        self.tearDown()
    
    def test_08etoolsextype(self):
        self.sub_setUp()
        self.login_success()
        self.Report_Management_page = ReportManagementResult(self.Report_Management_page)
        etoolsextype_message = self.Report_Management_page.etoolsextype_result()
        logger.info(etoolsextype_message)
        self.tearDown()
    
    def test_09etoolsecurity(self):
        self.sub_setUp()
        self.login_success()
        self.Report_Management_page = ReportManagementResult(self.Report_Management_page)
        etoolsecurity_message = self.Report_Management_page.etoolsecurity_result()
        logger.info(etoolsecurity_message)
        self.tearDown()
    
    def test_10etoolwebaccess(self):
        self.sub_setUp()
        self.login_success()
        self.Report_Management_page = ReportManagementResult(self.Report_Management_page)
        etoolwebaccess_message = self.Report_Management_page.etoolwebaccess()
        logger.info(etoolwebaccess_message)
        self.tearDown()
    
    def test_11sendemail(self):
        self.sub_setUp()
        self.login_success()
        self.Report_Management_page = ReportManagementResult(self.Report_Management_page)
        sendemail_message = self.Report_Management_page.send_report()
        logger.info(sendemail_message)
        self.tearDown()
    
    def test_12lotmatching(self):
        self.sub_setUp()
        self.login_success()
        self.Report_Management_page = ReportManagementResult(self.Report_Management_page)
        lotmatching_message = self.Report_Management_page.lotmatching()
        logger.info(lotmatching_message)
        self.tearDown()
    
    def test_13lotmatchinghistory(self):
        self.sub_setUp()
        self.login_success()
        self.Report_Management_page = ReportManagementResult(self.Report_Management_page)
        lotmatchinghistory_message = self.Report_Management_page.lotmatchinghistory_result()
        logger.info(lotmatchinghistory_message)
        self.tearDown()

    def test_14codemanager(self):
        self.sub_setUp()
        self.login_success()
        self.Report_Management_page = ReportManagementResult(self.Report_Management_page)
        codemanger_message = self.Report_Management_page.codemanager_result()
        logger.info(codemanger_message)
        self.tearDown()
    
    def test_15systemfield(self):
        self.sub_setUp()
        self.login_success()
        self.Report_Management_page = ReportManagementResult(self.Report_Management_page)
        systemfield_message = self.Report_Management_page.systemfield_result()
        logger.info(systemfield_message)
        self.tearDown()
    
    def test_16fieldmapping(self):
        self.sub_setUp()
        self.login_success()
        self.Report_Management_page = ReportManagementResult(self.Report_Management_page)
        fieldmapping_message = self.Report_Management_page.fieldmapping_result()
        logger.info(fieldmapping_message)
        self.tearDown()
    
    def test_17myreport(self):
        self.sub_setUp()
        self.login_success()
        self.Report_Management_page = ReportManagementResult(self.Report_Management_page)
        myreport_message = self.Report_Management_page.myreport_result()
        logger.info(myreport_message)
        self.tearDown()
    
    def test_18htsidataqualityreport(self):
        self.sub_setUp()
        self.login_success()
        self.Report_Management_page = ReportManagementResult(self.Report_Management_page)
        htsidataqualityreport_message = self.Report_Management_page.htsidataqualityreport_result()
        logger.info(htsidataqualityreport_message)
        self.tearDown()
    
    def test_19poultryexcelreport(self):
        self.sub_setUp()
        self.login_success()
        self.Report_Management_page = ReportManagementResult(self.Report_Management_page)
        poultryexcelreport_message = self.Report_Management_page.poultryexcelreport_result()
        self.assertEqual(poultryexcelreport_message, 'View Report')
        logger.info(poultryexcelreport_message)
        self.tearDown()
    
    def test_20htsidataextract(self):
        self.sub_setUp()
        self.login_success()
        self.Report_Management_page = ReportManagementResult(self.Report_Management_page)
        htsidataextract_message = self.Report_Management_page.htsidataextract_result()
        logger.info(htsidataextract_message)
        self.tearDown()
    
    def test_21reportsecurity(self):
        self.sub_setUp()
        self.login_success()
        self.Report_Management_page = ReportManagementResult(self.Report_Management_page)
        reportsecurity_message = self.Report_Management_page.reportsecurity_result()
        logger.info(reportsecurity_message)
        self.tearDown()

    def test_22ftpmanagement(self):
        self.sub_setUp()
        self.login_success()
        self.Report_Management_page = ReportManagementResult(self.Report_Management_page)
        ftpmanagement_message = self.Report_Management_page.ftp_management_result()
        logger.info(ftpmanagement_message)
        self.tearDown()
    
    def test_23reports(self):
        self.sub_setUp()
        self.login_success()
        self.Report_Management_page = ReportManagementResult(self.Report_Management_page)
        reports_message = self.Report_Management_page.reports_result()
        logger.info(reports_message)
        self.tearDown()

if __name__ == '__main__':
    unittest.main()
    """
    report = REPORT_PATH + '\\report.html'
    testsuite = unittest.TestSuite()
    testsuite.addTest(TestThirdparty('test_login'))
    testsuite.addTest(TestThirdparty('test_addnew'))
    testsuite.addTest(TestThirdparty('test_templatelist'))
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f,title=u'从0搭建测试框架 灰蓝', description='修改HTML报告')
        runner.run(testsuite)

    """
