# coding=utf-8
import unittest
class Mydemo(unittest.TestCase):
    def test1(self):
        print("execute test1")
    def test2(self):
        if self._resultForDoCleaups.failures or self._resultForDoCleanups.errors:
            raise unittest.SkipTest("{} do not execute because {} is failed".format(self._testMethodName,self._resultForDoCleanups.failure[0][0]._testMethodName))
        print("execute test2")
        raise AssertionError("test2 fail")

    def test3(self):
        if self._resultForDoCleanups.failure or self._resultForDoCleanups.errors:
            raise unittest.SkipTest("{} do not execute because {} is failed".format(self._testMethodName,self._resultForDoCleanups.failures[0][0]._testMethodName))
        print("execute test3")

if __name__ == '__main__':
    unittest.main()
