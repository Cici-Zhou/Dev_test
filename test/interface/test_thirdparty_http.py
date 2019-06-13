import unittest
from utils.config import Config, REPORT_PATH
from utils.client import HTTPClient
from utils.log import logger
from utils.HTMLTestRunner_PY3 import HTMLTestRunner
from utils.assertion import assertHTTPCode


class TestThirdPartyHTTP(unittest.TestCase):
    URL = Config().get('URL')

    def setUp(self):
        self.client = HTTPClient(url=self.URL, method='GET')

    def test_thirdparty_http(self):
        res = self.client.send()
        logger.debug(res.text)
        assertHTTPCode(res, [400])
        self.assertIn(u'ThirdParty', res.text)

if __name__ == '__main__':

    """
    testunit = unittest.TestSuite()
    testunit.addTest(TestThirdPartyHTTP('test_thirdparty_http'))
    report = REPORT_PATH + '\\portreport.html'
    fp = open(report, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u'从0搭建测试框架 灰蓝', description='接口报告')
    runner.run(testunit)
    fp.close()
"""

    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner  = HTMLTestRunner(f, verbosity=2, title='从零搭建测试框架', description='接口html报告')
        runner.run(TestThirdPartyHTTP(test_thirdparty_http))
