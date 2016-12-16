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


class raiseQuestion:
    def __init__(self,driver):
        self.driver=driver
       # self.path='f:\\WorkSpace\\python\\excel\\new.csv'
        self.Err=[]
    def raiseQuestion(self):
        """提问题入口"""  
        expect_url='http://192.168.11.181:8080/JSFW/problem/find_problem.do'
        dr=self.driver
        Mytool.findClass(dr,"sc-matter").click()
        time.sleep(2)
        cur_url=dr.current_url
        assert expect_url==cur_url,"url wrong"
       # Mytool.findClass(dr,"s_btn_logins").click()
        dr.implicitly_wait(10)
        self.questionDetail("2")
        self.stepOp(2)#下一步
        self.expertChoose(2)
        self.stepOp(2)
        self.payPage()

    def findExpert(self,expnum=1):
        """找专家入口流程"""  
        expect_url='http://192.168.11.181:8080/JSFW/findexps/findexp.do'
        dr=self.driver
        Mytool.findCss(dr,"div.sc_login_after>a").click()
        time.sleep(2)
        cur_url=dr.current_url
        assert expect_url==cur_url,"url wrong"
        time.sleep(4)
        self.expertChoose(expnum)#选专家
        Mytool.scroll(dr,2000)
        self.stepOp(2)#下一步
        time.sleep(1)
        Mytool.findId(dr,'pro_detail',u'截止日期测试')#问题描述
        Mytool.scroll(dr,2000)
        time.sleep(2)
        self.stepOp(4)#下一步
        self.payPage("E",1,3)#支付


#注册页面  Undone
    def Register(self):
        dr=self.driver
        Mytool.findClass(dr,'s_free').click()
        time.sleep(2)
        cur_url=dr.current_url

    def getErr(self):
        if len(self.Err)!=0:
            return self.Err
        #获取输入文本框的值
        

    def stepOp(self,flag):
        """flag 取值为0,1,2.分别代表上一步 暂存 下一步  
        """
        dr=self.driver
        """上一步 暂存 下一步"""
        stepList=Mytool.findClasses(dr,'lastStep')
        print "stepList lenght is:"+str(len(stepList))
        print stepList[flag].get_attribute("class")
        for i in range(0,len(stepList)):
            print stepList[i].get_attribute("class")
        stepList[flag].click()
        del stepList
       
 
    def questionDetail(self,i="1",k=1):
        """问题描述 when i==1, means the question type is 技术咨询,i==2 means the question type is 项目评价.And
        when i==2,k means how many types of evaluation needs to be done"""
        dr=self.driver
        Mytool.findLink(dr,u"电子信息").click()
        Mytool.findLink(dr,u"云计算").click()
        Mytool.findClass(dr,"lastStep").click()
        if u"电子信息-软件-云计算" !=Mytool.findId(dr,"you_choice").text:
            str="you_choice_not_equal"
            self.Err.append(str)
        if i=="2":
            pro_typeid="//option[@value="+i+"]"
            Mytool.selectList(dr,"pro_typeid",pro_typeid)
            reqList=Mytool.findCsses(dr,"input[type='checkbox']")
            for j in range(0,k):
                reqList[j].click()
        Mytool.findId(dr,'pro_detail',u'计算')

    def expertChoose(self,num=1):
        u"""选择专家 num represent how many experts you want to choose"""
        dr=self.driver
        expList=Mytool.findLinks(dr,u"选择")
        print "length of expList:"+str(len(expList))
        if num>=1 and num<=len(expList):
            for i in range(0,num):
                expid=expList[i].get_attribute("exp_id")
                print "expid:"+str(expid)
                expList[i].click()
        else:
            raise IndexError,IndexError('num is out of range')

        


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

#Trade information

    def payPage(self,flag="Q",n=1,t=0):
        u"""flag:Q represent FIND_QUESTION;E represent FIND_EXPERT
        n:expect N experts to answer
        t:expectation of the final answer day
        """
        dr=self.driver
        if flag=="Q":
            n_exp=Mytool.findId(dr,"n_exp")
        elif flag=="E":
            n_exp=Mytool.findId(dr,"expect_re_num")
        n_exp.clear()
        n_exp.send_keys(n)
        reply_time=Mytool.findCss(dr,"#re_date>input")
        exp_time=datetime.date.today()+datetime.timedelta(t)#期望回复日期
        ti=str(exp_time)
        print ti
        reply_time.send_keys(ti)
        if flag=="Q":
            Mytool.findCss(dr,"#payment_pwd>input").send_keys("888888")
            Mytool.findId(dr,"payment_checknum").send_keys("1")
        elif flag=="E":
            Mytool.findId(dr,"payment_pwd").send_keys("888888")
            #Mytool.findId(dr,"payment_checknum").send_keys("1")
            time.sleep(3)
        self.stepOp(4)
        time.sleep(2)
        if Mytool.findClass(dr,"s_ok"):
            Mytool.findClass(dr,"s_ok").click()
        else:
            raise AssertionError,AssertionError("failed paying")
      
    def getTotalprice(self):
        '''return the expert cost add on the fee'''
        listAmount=Mytool.getDict("listAmount")
        priceAmount=Mytool.getDict("priceAmount")
        totalPrice=float(listAmount)*float(priceAmount)
        return totalPrice

    def returnDic(self):
        self.dict=Mytool.returnMydic()
        print"the dict has:%s"%len(self.dict)
        return self.dict

