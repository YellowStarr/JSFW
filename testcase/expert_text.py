#!/usr/bin/env python
# -*- coding: utf-8 -*-
#专家问题中心测试
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,sys,os
sys.path.append("public")
from public import *
from public import Mytool
import os,datetime
import HTMLTestRunner

class Expert_Test(unittest.TestCase):
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
        u"""回复问题后，结束问题"""
        question_NO='jszx20170329162951'
        expert_name='chenjian'
        expert_password=123456
        expect_url=self.base_url+'/JSFW/reply/jszx_reply.do?view=expert_question&state_typeid=2'

        dr=self.driver
        lg=login.Login(dr,self.base_url)
        lg.Login(expert_name,expert_password)
        Expert=expert.Expert(dr,self.base_url)
        Expert.myQuestion(question_NO,u"回复")
        time.sleep(3)
        self.assertEqual(dr.current_url,expect_url,"WRONG URL,CHECK THE BUTTON TO SEE IF IT'S NOT WORK!")
        Expert.Reply("replyed the question and end the question","reply")
        time.sleep(2)
        # dr.get(self.base_url+'/JSFW/pages/expert_question.do?view=expert_question')
        # time.sleep(2)
        state=Expert.queryQuestion(question_NO)
        time.sleep(1)
        try:
            self.assertEqual(state,u"已回复","WRONG STATE")
        except AssertionError as e:
            Mytool.getScreen('replyed')
            self.verificationErrors.append(str(e))
        Expert.myQuestion(question_NO,u"结束问题")
        Expert.endQuestion()
        time.sleep(4)
        state=Expert.queryQuestion(question_NO)
        time.sleep(2)
        try:
            self.assertEqual(state,u"完成-未评价","WRONG STATE")
        except AssertionError as e:
            Mytool.getScreen('complete')
            self.verificationErrors.append(str(e))


    def  test_case2(self):
        u"""无法回答操作"""
        question_NO='jszx20170329162951'
        expert_name='chenjian'
        expert_password=123456
        expect_url=self.base_url+'/JSFW/reply/jszx_reply.do?view=expert_question&state_typeid=2'

        dr=self.driver
        lg=login.Login(dr,self.base_url)
        lg.Login(expert_name,expert_password)
        Expert=expert.Expert(dr,self.base_url)
        Expert.myQuestion(question_NO,u"无法回答")
        time.sleep(3)
        self.assertEqual(dr.current_url,expect_url,"WRONG URL,CHECK THE BUTTON TO SEE IF IT'S NOT WORK!")
        Expert.Reply("can't reply your question sorry","refuse")
        time.sleep(2)
        state=Expert.queryQuestion(question_NO)
        time.sleep(1)
        try:
            self.assertEqual(state,u"未解决","WRONG STATE")
        except AssertionError as e:
            Mytool.getScreen('unsolve')
            self.verificationErrors.append(str(e))



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
