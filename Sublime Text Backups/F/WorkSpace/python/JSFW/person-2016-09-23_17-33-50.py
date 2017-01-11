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
        Mytool.findLink(dr,u"我的问题").click()
        time.sleep(2)
    def Info(self):
        """个人信息"""  
        #expect_url='http://192.168.11.181:8080/JSFW/problem/find_problem.do'
        dr=self.driver
        
        Mytool.findId(dr,"myInfo").click()
        
        #self.payPage()

    def findExpert(self):
        """找专家入口"""  
        expect_url='http://192.168.11.181:8080/JSFW/findexps/findexp.do'
        dr=self.driver
        Mytool.findCss(dr,"div.sc_login_after>a").click()
        time.sleep(2)
        cur_url=dr.current_url
        assert expect_url==cur_url,"url wrong"
       # Mytool.findClass(dr,"s_btn_logins").click()
        dr.implicitly_wait(10)
        self.expertChoose(1)
        Mytool.scroll(dr,2000)
        self.stepOp(2)
        time.sleep(1)
        Mytool.findId(dr,'pro_title',u'test1')
        Mytool.findId(dr,'pro_detail',u'计算')
        Mytool.scroll(dr,2000)
        time.sleep(2)
        self.stepOp(4)
        self.payPage("E")

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
        print len(stepList)
        print stepList[flag].get_attribute("class")
        stepList[flag].click()
        del stepList
       
 
    def questionDetail(self,i="1",k=1):
        """问题描述"""
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

        Mytool.findId(dr,'pro_title',u'test1')
        Mytool.findId(dr,'pro_detail',u'计算')

    def expertChoose(self,num=1):
        """选择专家"""
        dr=self.driver
        expList=Mytool.findLinks(dr,u"选择")
        if num>=1 and num<=len(expList):
            for i in range(0,num):
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
        """
        """
        dr=self.driver
        if flag=="Q":
            n_exp=Mytool.findId(dr,"n_exp")
        elif flag=="E":
            n_exp=Mytool.findId(dr,"expect_re_num")
        n_exp.clear()
        n_exp.send_keys(n)
        reply_time=Mytool.findCss(dr,"#re_date>input")
        exp_time=datetime.date.today()+datetime.timedelta(t)
        ti=str(exp_time)
        print ti
        reply_time.send_keys(ti)
        if flag=="Q":
            Mytool.findCss(dr,"#payment_pwd>input").send_keys("888888")
            Mytool.findId(dr,"payment_checknum").send_keys("1")
        elif flag=="E":
            Mytool.findId(dr,"payment_pwd").send_keys("888888")
            Mytool.findId(dr,"payment_checknum").send_keys("1")
        self.stepOp(2)
        time.sleep(2)
        if Mytool.findClass(dr,"s_ok"):
            Mytool.findClass(dr,"s_ok").click()
        else:
            raise AssertionError,AssertionError("failed paying")
      
    def getTotalprice(self):
        listAmount=Mytool.getDict("listAmount")
        priceAmount=Mytool.getDict("priceAmount")
        totalPrice=float(listAmount)*float(priceAmount)
        return totalPrice
    

    
    def getContract(self,depValue=1,buyerP=0,sellerP=0,firstN=80,day1=0,day2=1,day3=1,day4=1,day5=1):
        """depValue 1 means deposit percent ,default value;2 means choose deposit quato 
           buyerP means buyer's rule and sellerP means seller's rule. if input less than system setting, we will use system setting`
           values, else we will use the args. if no input values we use system setting
        """
        driver=self.driver
        try:
            self.driver.find_element_by_id("append_more").click()
            time.sleep(1)
        except:
            print 'no button'
        depL=self.driver.find_elements_by_name("deposit_id")
        if depValue==1:
            Mytool.setDict('garanteeWay','percentage')
            percentageB=self.driver.find_element_by_id("deposit_value_1")
            datarules1=percentageB.get_attribute('data-rules')
            perB=Mytool.getDataRules(datarules1)[0]
            percentageS=self.driver.find_element_by_id("deposit_value_1_2")
            datarules2=percentageS.get_attribute('data-rules')
            perS=Mytool.getDataRules(datarules2)[0] 
            if buyerP>=float(perB) and buyerP<= 100:
                percentageB.clear()
                percentageB.send_keys(buyerP)
            else:
                print 'wrong number'
            if self.flag==0:
                if sellerP>=float(perS) and sellerP<= 100:
                    percentageS.clear()
                    percentageS.send_keys(sellerP)
            else:
                sellerP=""
        elif depValue==2:
            depL[1].click()
            Mytool.setDict('garanteeWay','quato')
            quatoB=self.driver.find_element_by_id("deposit_value_2")
            datarules1=quatoB.get_attribute('data-rules')
            numB=Mytool.getDataRules(datarules1)[0]
            quatoS=self.driver.find_element_by_id("deposit_value_2_2")
            datarules2=quatoS.get_attribute('data-rules')
            numS=Mytool.getDataRules(datarules2)[0]
            if buyerP>=float(numB):
                quatoB.clear()
                quatoB.send_keys(buyerP)
                print 'the number must be higher than pre-setting number'
            if self.flag==0:
                if sellerP>=float(numS):
                    quatoS.clear()
                    quatoS.send_keys(sellerP)
            else:
                sellerP=""
        Mytool.setDict("buyerP",buyerP)
        Mytool.setDict("sellerP",sellerP)

        inspect=Mytool.findId(driver,"att45")
        
        if not inspect.get_attribute("disabled"):
            print inspect.get_attribute("disabled")
            print 'disable'
            rule1=inspect.get_attribute('data-rules')
            minVal=Mytool.getDataRules(rule1)[0]
            inspect.send_keys(firstN)


        ganranteeDeadline=Mytool.findId(driver,'att41')
        
        if not ganranteeDeadline.get_attribute("disabled"):
            rule2=ganranteeDeadline.get_attribute('data-rules')
            minVal2=Mytool.getDataRules(rule2)[0]
            ganranteeDeadline.send_keys(day1)

        payDeadline=Mytool.findId(driver,'att42')
        if not payDeadline.get_attribute("disabled"):
            rule3=payDeadline.get_attribute('data-rules')
            minVal3=Mytool.getDataRules(rule3)[0]
            payDeadline.send_keys(day2)

        delivDeadline=Mytool.findId(driver,'att47')
        if not delivDeadline.get_attribute("disabled"):
            rule4=delivDeadline.get_attribute('data-rules')
            minVal4=Mytool.getDataRules(rule4)[0]
            delivDeadline.send_keys(day3)

        inspectDeadline=Mytool.findId(driver,'att43')
        if not inspectDeadline.get_attribute("disabled"):
            rule5=inspectDeadline.get_attribute('data-rules')
            minVal5=Mytool.getDataRules(rule5)[0]
            inspectDeadline.send_keys(day4)

        ticketDeadline=Mytool.findId(driver,'att44')
        if not ticketDeadline.get_attribute("disabled"):
            rule6=ticketDeadline.get_attribute('data-rules')
            minVal6=Mytool.getDataRules(rule6)[0]
            ticketDeadline.send_keys(day5)
#合同约定资金
    def payDeposite(self):
        """no input accept. just get values that system has calculated
        """
        driver=self.driver
        totalPrice=driver.execute_script('return document.getElementById("totalprice_id").value')
        
        deposit=driver.execute_script('return document.getElementById("deposit_value").value')
        #print driver.find_element_by_id("other_value").get_attribute("data-rules")
        freezeM=driver.execute_script('return document.getElementById("totalpay").value')
        commission=driver.execute_script('return document.getElementById("charge_money").value')
        availableM=driver.execute_script('return document.getElementById("money_all").value')

        driver.find_element_by_id("passw").send_keys("888888")
        Mytool.setDict("totalPrice",totalPrice)
        Mytool.setDict("deposit",deposit)
        Mytool.setDict("availableM",availableM)
        Mytool.setDict("commission",commission)
        Mytool.setDict("freezeM",freezeM)
    
    def getFreezeM(self):
        commission=Mytool.getDict("commission")
        deposit=Mytool.getDict("deposit")
        freezeMc=float(commission)+float(deposit)
        return freezeMc
        
#submit
    def submit(self):
        print"submit"
        self.driver.find_element_by_id("commitBtnId").click()
        time.sleep(1)
        self.driver.get_screenshot_as_file("f:\\workspace\\python\\2.png")
        if self.flag==0:
            if self.driver.find_element_by_css_selector("button[datas='cancel']").is_displayed():
                print "continue"
                self.driver.find_element_by_css_selector("button[datas='cancel']").click()
        else:
            if self.driver.find_element_by_css_selector("button[datas='ok']").is_displayed():
                print "go on"
                self.driver.find_element_by_css_selector("button[datas='ok']").click()
                time.sleep(2)
                self.driver.find_element_by_css_selector("button[datas='cancel']").click()
                
    def getListNo(self):
        if self.driver.title==u'挂牌管理':
            listL=self.driver.find_elements_by_class_name('ullist')
            print len(listL)
            noList=self.driver.find_elements_by_class_name('ullist>li')
            no=noList[0].get_attribute("title")
            No=no.split(u"：")[1]
            Mytool.setDict("listNo",No)
        else:
            print "list failed"

    def returnDic(self):
        self.dict=Mytool.returnMydic()
        print"the dict has:%s"%len(self.dict)
        return self.dict

