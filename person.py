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


class Person:
    def __init__(self,driver):
        self.driver=driver
       # self.path='f:\\WorkSpace\\python\\excel\\new.csv'
        self.Err=[]
        dict=[]
        
    def Info(self):
        """个人信息"""  
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
       
        Mytool.setDict("userName",userName)
        Mytool.setDict("realName",realName)
        Mytool.setDict("sex",sex)
        Mytool.setDict("email",email)
        Mytool.setDict("tel_head",tel_head)
        Mytool.setDict("tel_body",tel_body)
        Mytool.setDict("qq",qq)
        Mytool.setDict("work",work)
        Mytool.setDict("industry",industry)
        Mytool.setDict("product",product)
        Mytool.setDict("addr",addr)
        Mytool.setDict("card_no",card_no)
        Mytool.setDict("limit",limit)
        Mytool.setDict("saveBtn",saveBtn)
    
    def setInfo(self):
        uname=Mytool.getDict('userName')
        uname.clear()
        uname.send_keys("qiuwenjing")
        Mytool.getDict('saveBtn').click()

    def MyQuestion(self,No):
        """我的问题"""  
        #expect_url='http://192.168.11.181:8080/JSFW/problem/find_problem.do'
        dr=self.driver
        Mytool.findLink(dr,u"我的问题").click()
        time.sleep(2)
        Mytool.findId(dr,"question_code",No)
        queryBt=Mytool.findClass(dr,"save_btn")
        resetBt=Mytool.findClass(dr,"return_btn")
        queryBt.click()
        state=Mytool.findClass(dr," stall")
        Mytool.setDict("state",state.text)
        Mytool.findClass(dr,"look_btn").send_keys(Keys.ENTER)
        dr.get_screenshot_as_file("F:/WorkSpace/python/JSFW/MyQuestion.png")
        djmoney=Mytool.findId(dr,"djmoney").text
        Mytool.setDict("dj",djmoney)

    def AnswerQuestion(self,No):
        u"""专家回复问题"""
        dr=self.driver
        Mytool.findLink(dr,u"我的问题").click()
        time.sleep(2)
        Mytool.findId(dr,"exp_re_question").click()
        Mytool.findId(dr,"pro_code",No)
        queryBt=Mytool.findClass(dr,"save_btn")
        resetBt=Mytool.findClass(dr,"return_btn")
        queryBt.send_keys(Keys.ENTER)
        time.sleep(2)
        Mytool.getScreen(dr)
        deadTime=Mytool.findXpath(dr,"//*[@id='re_question']/tbody/tr[1]/td[4]").text
        expName=Mytool.findXpath(dr,"//*[@id='re_question']/tbody/tr[1]/td[5]").text
        cost=Mytool.findXpath(dr,"//*[@id='re_question']/tbody/tr[1]/td[6]").text
        state=Mytool.findXpath(dr,"//*[@id='re_question']/tbody/tr[1]/td[8]").text

        Mytool.setDict("deadTime",deadTime)
        Mytool.setDict("expName",expName)
        Mytool.setDict("cost",cost)
        # Mytool.setDict("expName",expName)
        Mytool.setDict("state",state)

        btnList=Mytool.findClass(dr,"btn")
        for i in range(len(btnList)):
            if  Op==btnList[i].get_attribute('value'):
                btnList[i].send_keys(Keys.ENTER)
                break
        if Mytool.findClass(dr,'s_ok'):
            Mytool.findClass(dr,'s_ok').click()


    def add_Question(self,text):
        dr=self.driver
        Mytool.findId(dr,'pro_re_det').send_keys(text)
        btL=Mytool.findClasses(dr,'btn')
        for i in range(len(btl)):
            if Op==btL[i].get_attribute('value'):
                btL[i].send_keys(Keys.ENTER)
                break
#上传图片
    def upload_Pic(self,url):
        self.driver.find_element_by_id("uppicpath").click()
        time.sleep(2)
        js="document.getElementsByClassName('ks-editor-input')[0].readOnly=false"
        self.driver.execute_script(js)
        self.driver.find_element_by_name("test").send_keys(url)
        self.driver.find_element_by_css_selector("button[datas='up']").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("div.ks-overlay-footer>div>button[datas='ok']").click()
        time.sleep(1)

    def returnDic(self):
        self.dict=Mytool.returnMydic()
        print"the dict has:%s"%len(self.dict)
        return self.dict

