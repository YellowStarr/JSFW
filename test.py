#!/usr/bin/env python
# -*- coding: utf-8 -*-
#库存挂牌
import pdb
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from login import Login
from raiseQuestion import raiseQuestion
from person import Person
import os,sys
import Mytool
import HTMLTestRunner

class test(unittest.TestCase):
    def setUp(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://218.249.25.106:15301/JSFW"
        self.verificationErrors = []
        self.accept_next_alert = True
        #self.f=open("f:/workspace/python/data.txt","w")
        self.driver.maximize_window()
        global dict

    def test_LG(self):
        u"""技术服务提问题测试"""
        driver = self.driver
        driver.delete_all_cookies()
        driver.get(self.base_url + 
        "/home/unlogin.do")
        li=Login(driver)
        '''for i in range(1,100):
            li.Login(i,888888)
        Mytool.printDict()  '''
        time.sleep(3) 
        RQ=raiseQuestion(driver)
        RQ.raiseQuestion()

    def test_Exp(self):
        u"""技术服务找专家测试"""
        driver = self.driver
        driver.delete_all_cookies()
        # Mytool.readExec("F:\\WorkSpace\\python\\JSFW\\testcase.csv")
        driver.get(self.base_url + "/home/unlogin.do")
        li=Login(driver)
        li.Login("qiuwjcom1",888888)  
        time.sleep(3) 
        RQ=raiseQuestion(driver)
        RQ.findExpert(u'数值佣金测试case01',1,2,1,3)

    def test_Money(self):
        u'''资金测试'''
        driver = self.driver
        driver.delete_all_cookies()
        driver.get(self.base_url + "/home/unlogin.do")
        li=Login(driver)
        li.Login("qiuwjn2",888888)  
        time.sleep(3) 

        RQ=raiseQuestion(driver)
        RQ.findExpert()
        

        # try:self.assertEqual(u"完成",Mytool.getDict("state"))
        # except AssertionError as e: self.verificationErrors.append(str(e))
        # try:self.assertEqual("2016-12-15",Mytool.getDict("deadTime"))
        # except AssertionError as e: self.verificationErrors.append(str(e))
        # try:self.assertEqual("600",Mytool.getDict("cost"),"cost wrong")
        # except AssertionError as e: 
        #     self.verificationErrors.append(str(e))



    def test_DeadTime(self):
        u'''截止日期测试'''
        driver = self.driver
        driver.delete_all_cookies()
        driver.get(self.base_url + "/home/unlogin.do")
        li=Login(driver)
        li.Login("qiuwjn2",888888)  
        time.sleep(3) 
        p=Person(driver)
        p.AnswerQuestion("jszx20161221172109")
        try:self.assertEqual(u"完成",Mytool.getDict("state"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try:self.assertEqual("2016-12-15",Mytool.getDict("deadTime"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try:self.assertEqual("600",Mytool.getDict("cost"),"cost wrong")
        except AssertionError as e: 
            self.verificationErrors.append(str(e))
        

    def test_PersonCenter(self):
        u"""个人中心测试"""
        driver = self.driver
        driver.delete_all_cookies()
        driver.get(self.base_url + 
            "/home/unlogin.do")
        li=Login(driver)
        li.Login("siva002",888888)  
        time.sleep(3)   
        info=Person(driver)
        info.Info()
        info.setInfo()

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
        # self.driver.quit()
        self.assertEqual([], self.verificationErrors)
            
if __name__ == "__main__":
    testunit=unittest.TestSuite()
    # testunit.addTest(test("test_DeadTime"))
    #testunit.addTest(test("test_PersonCenter"))
    testunit.addTest(test("test_Exp"))

    #  filename="f:\\WorkSpace\\python\\JSFW\\repoter.html"
    # fp=file(filename,'wb')
    # runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='testreport',description='caseRun')
    # runner.run(testunit)
    runner=unittest.TextTestRunner()
    runner.run(testunit)