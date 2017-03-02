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
    def __init__(self,driver,url):
        self.driver=driver
       # self.path='f:\\WorkSpace\\python\\excel\\new.csv'
        self.baseurl=url
        self.Err=[]
        self.myQueDict={}
        self.ansQList=[]
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
       

    def setInfo(self):
        uname=Mytool.getDict('userName')
        uname.clear()
        uname.send_keys("qiuwenjing")
        Mytool.getDict('saveBtn').click()

    def MyQuestion(self,No):
        """我的问题"""  
        #expect_url='http://192.168.11.181:8080/JSFW/problem/find_problem.do'
        url='/memquestion/question.do'
        dr=self.driver
        dr.get(self.baseurl+url)
        time.sleep(2)
        Mytool.findId(dr,"question_code",No)
        queryBt=Mytool.findClass(dr,"save_btn")
        resetBt=Mytool.findClass(dr,"return_btn")
        queryBt.click()
        state=Mytool.findClass(dr," stall")
        self.myQueDict["Qstate"]=state.text
        Mytool.findClass(dr,"look_btn").send_keys(Keys.ENTER)
        Mytool.getScreen(dr,"MyQuestion",No)
        djmoney=Mytool.findId(dr,"djmoney").text
        self.myQueDict["dj"]=float(djmoney)

    def AnswerQuestion(self,No):
        u"""专家回复问题"""
        dr=self.driver
        url='/exprequestion/exp_re_question.do'
        dr.get(self.baseurl+url)
        time.sleep(2)
        Mytool.findId(dr,"pro_code",No)
        queryBt=Mytool.findClass(dr,"save_btn")
        resetBt=Mytool.findClass(dr,"return_btn")
        queryBt.send_keys(Keys.ENTER)
        time.sleep(2)
        Mytool.getScreen(dr,"expertAnswerQuestion",No)
        rows=Mytool.findXpathes(dr,"//*[@id='re_question']/tbody/tr")
        for i in range(1,len(rows)+1):
            ansQ={}
            deadTime=Mytool.findXpath(dr,"//*[@id='re_question']/tbody/tr["+str(i)+"]/td[4]").text
            expName=Mytool.findXpath(dr,"//*[@id='re_question']/tbody/tr["+str(i)+"]/td[5]").text
            cost=Mytool.findXpath(dr,"//*[@id='re_question']/tbody/tr["+str(i)+"]/td[6]").text
            state=Mytool.findXpath(dr,"//*[@id='re_question']/tbody/tr["+str(i)+"]/td[8]").text
            btnList=Mytool.findClasses(dr,"btn")
            ansQ['deadTime']=deadTime
            ansQ['expName']=expName
            ansQ['cost']=float(cost)
            ansQ['state']=state
            ansQ['Op']=btnList
            self.ansQList.append(ansQ)

    def add_Question(self,rows=0,text='add question'):
         u'''追问操作'''
         dr=self.driver
         addDict=self.ansQList[rows]
         btnList=addDict['Op']
         for i in range(len(btnList)):
             if  u'追问'==btnList[i].get_attribute('value'):
                 btnList[i].send_keys(Keys.ENTER)
                 time.sleep(2)
                 break
         Mytool.findId(dr,'pro_re_det').send_keys(text)
         Mytool.findClass(dr,'save_btn').send_keys(Keys.ENTER)
         time.sleep(1)
         if Mytool.findClass(dr,'s_ok'):
             Mytool.findClass(dr,'s_ok').send_keys(Keys.ENTER)

    def make_Evalue(self,rows=0,level=4):
         u'''评价'''
         dr=self.driver
         addDict=self.ansQList[rows]
         btnList=addDict['op']
         for i in range(len(btnList)):
             if  u'评价'==btnList[i].get_attribute('value'):
                 btnList[i].send_keys(Keys.ENTER)
                 time.sleep(2)
                 break
         allStars=Mytool.findClasses(dr,'star')
         allStars[level].click()
         Mytool.findId(dr,'judge').send_keys(u'evaluation')
         Mytool.findClass(dr,'save_btn').send_keys(Keys.ENTER)
         if Mytool.findClass(dr,'s_ok'):
             Mytool.findClass(dr,'s_ok').send_keys(Keys.ENTER)

    def user_Charge(self,no):
        u'''收支明细'''
        dr=self.driver
        url="/JSFW/pages/user_charge.do"
        dr.get(self.baseurl+url)
        Mytool.findId(dr,"questionNo").send_keys(no)
        Mytool.findClass(dr,"save_btn").send_keys(Keys.ENTER)
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

    def getAnswerQList(self):
        return self.ansQList
    def getMyQuestionDict(self):
        return self.myQueDict

