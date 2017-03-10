#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,sys,os
sys.path.append("public")
from public import *
from public import Mytool
import os,datetime
import HTMLTestRunner

class Subject_Test(unittest.TestCase):
    def setUp(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        self.driver.implicitly_wait(30)
        # self.base_url = "http://218.249.15.107" #准生产
        self.base_url = "http://192.168.11.181:8080" #测试机
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.maximize_window()
        self.path=os.getcwd()

    def  test_case1(self):
        u"""按学科找专家流程"""
        dr=self.driver
        lg=login.Login(dr,self.base_url)
        lg.Login("qiuwjcom1",888888)
        sub=raiseQuestion.raiseQuestion(dr,self.base_url)
        sub.subjectExpert(u"计算机感知",u"计算机",1,1,1)
        time.sleep(3)
        sub.getQuestionNo()
        dict=sub.returnDic()
        Mytool.saveExc(self.path+"\\data\\subject.xls",dict)

    def  test_case2(self):
        u"""按技术领域找专家流程"""
        dr=self.driver
        lg=login.Login(dr,self.base_url)
        lg.Login("qiuwj3",888888)
        sub=raiseQuestion.raiseQuestion(dr,self.base_url)
        sub.industryExpert(u"基础软件",u"基础",2,1,2)
        time.sleep(3)
        sub.getQuestionNo()
        dict=sub.returnDic()
        Mytool.saveExc(self.path+"/data/industry.xls",dict,true)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
