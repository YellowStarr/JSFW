#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException 
import time,re,Mytool,datetime
import os,sys


class Expert:
    def __init__(self,driver,url):
        self.driver=driver
       # self.path='f:\\WorkSpace\\python\\excel\\new.csv'
        self.Err=[]
        dict=[]
        self.moneyDict={}
        self.baseurl=url
    
    def getmoneyDict(self):
        dict=self.moneyDict
        return dict

    def getExpAccount(self):
        """获取专家账户总资金 可用资金 冻结资金 本月收入"""
        dr=self.driver
        exp="/pages/exphome.do"
        expurl=self.baseurl+exp
        totalAccount=Mytool.findId(dr,"all_money").text
        availableMoney=Mytool.findId(dr,"ky_money").text
        freezeMoney=Mytool.findId(dr,"dj_money").text
        monthMoney=Mytool.findId(dr,"mouth_account").text
        self.moneyDict['totalAccount']=totalAccount
        self.moneyDict['availableMoney']=availableMoney
        self.moneyDict['freezeMoney']=freezeMoney
        self.moneyDict['monthMoney']=monthMoney
'''
    def Info(self):
        """专家信息"""  
        #expect_url='http://192.168.11.181:8080/JSFW/problem/find_problem.do'
        dr=self.driver
        Mytool.findLink(dr,u"我的问题").click()
        time.sleep(2)
        Mytool.findId(dr,"myInfo").click()
        Mytool.findId(dr,"user_inf").click()
        #allInput=Mytool.findCsses(dr,"input")
        userName=Mytool.findId(dr,"emp_acct")
        realName=Mytool.findId(dr,"user_realname")
        #userAccount
        sex=Mytool.findClass(dr,"s_checked02")
        email=Mytool.findId(dr,"user_email")
        tel_head=Mytool.findId(dr,"user_telephone_head")
        tel_body=Mytool.findId(dr,"user_telephone_body")
        qq=Mytool.findId(dr,"user_qq")
        work=Mytool.findId(dr,"user_comwork")
        industry=Mytool.findId(dr,"user_industry")
        product=Mytool.findId(dr,"com_product")
        addr=Mytool.findId(dr,"detail_add")
        card_no=Mytool.findId(dr,"card_no")
        limit=Mytool.findId(dr,"card_front_pg")
        saveBtn=Mytool.findCss(dr,u"input[value='保存']")
'''
    def setInfo(self):
        uname=Mytool.getDict('userName')
        uname.clear()
        uname.send_keys("qiuwenjing")
        Mytool.getDict('saveBtn').click()

    def myQuestion(self,No,btName):
        """我的问题"""  
        #expect_url='http://192.168.11.181:8080/JSFW/problem/find_problem.do'
        dr=self.driver
        exp="/pages/expert_question.do?view=expert_question"
        dr.get(self.baseurl+exp)
        # Mytool.findId(dr,"expert_question").click()
        time.sleep(2)
        ele=Mytool.findId(dr,'my_question0')
        ActionChains(dr).move_to_element(ele).click()
        time.sleep(1)
        Mytool.findId(dr,"pro_id",No)
        queryBt=Mytool.findClass(dr,"save_btn")
        resetBt=Mytool.findClass(dr,"return_btn")
        queryBt.send_keys(Keys.ENTER)

        state=Mytool.findXpath(dr,"//*[@id='expcenter_data']/tbody/tr/td[8]")
        stateV=state.get_attribute("title")
        btnList=Mytool.findClasses(dr,'look_btn')
        for btn in range(len(btnList)):
            value=btn.get_attribute("value")
            if value==btName:
                btn.send_keys(Keys.ENTER)
                time.sleep(2)

        dr.get_screenshot_as_file("F:/WorkSpace/python/JSFW/MyQuestion.png")
        djmoney=Mytool.findId(dr,"djmoney").text

    def returnDic(self):
        self.dict=Mytool.returnMydic()
        print"the dict has:%s"%len(self.dict)
        return self.dict
