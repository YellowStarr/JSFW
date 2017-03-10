#codidng=utf-8
import unittest
import sys,datetime,time
sys.path.append("testcase")
from testcase import *
import HTMLTestRunner

import login_test,subject_test

caseNames=[
    # login_test.Login_Test,
    subject_test.Subject_Test
]

testunit=unittest.TestSuite()
for i in range(0,len(caseNames)):
    testunit.addTest(unittest.makeSuite(caseNames[i]))

nowtime=time.strftime("%Y-%m-%M-%H_%M_%S",time.localtime(time.time()))
filename='reporter\\'+nowtime+"reporter.html"
fp=file(filename,'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='testcase-logintest',description='desc')

runner.run(testunit)
