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
    def __init__(self,driver,url):
        self.driver=driver
        self.base_url=url
       # self.path='f:\\WorkSpace\\python\\excel\\new.csv'
        self.Err=[]
        self.recordDic={}
        self.expIdList=[]
        self.List=[]
    def raiseQuestion(self):
        """提问题入口"""  
        expect_url='http://192.168.11.181:8080/JSFW/problem/find_problem.do'
        dr=self.driver
        Mytool.findClass(dr,"sc-matter").click()
        time.sleep(2)
        cur_url=dr.current_url
        # assert expect_url==cur_url,"url wrong"
       # Mytool.findClass(dr,"s_btn_logins").click()
        dr.implicitly_wait(10)
        self.questionDetail("2")
        self.stepOp(2)#下一步
        self.expertChoose(2)
        self.stepOp(2)
        self.payPage()

    def findExpert(self,detail,expnum,questionType=1,answer=1,date=0):
        """找专家入口流程"""  
        exp_url='/findexps/giveQuestions.do'
        dr=self.driver
        dr.get(self.base_url+exp_url)
        time.sleep(2)
        cur_url=dr.current_url
        # assert expect_url==cur_url,"url wrong"
        if questionType==2:
            quesTypes=Mytool.findClasses(dr,'sc-check-box02')
            # print quesTypes[1].get_attribute('value')
            quesTypes[1].click()

        self.expertChoose(expnum)#选专家
        self.chosedExp()
        # self.Query(u'陈明宇')

        Mytool.scroll(dr,2100)
        self.stepOp("next()")#下一步
        time.sleep(1)
        Mytool.findId(dr,'pro_detail',detail)#问题描述
        self.recordDic['detail']=detail
        if questionType==2:
            evaluationList=Mytool.findNames(dr,'checkbox')
            evaluationList[0].click()
        Mytool.scroll(dr,2000)
        time.sleep(2)

        self.stepOp("next()")#下一步
        self.payPage("E",answer,date)#支付
        time.sleep(2)
        self.getQuestionNo()

        #Mytool.saveExc('testcase.csv','questionNo',questNo)
        

#注册页面  Undone
    def Register(self):
        dr=self.driver
        Mytool.findClass(dr,'s_free').click()
        time.sleep(2)
        cur_url=dr.current_url

    def getChoseExp(self):
        expInfo=self.List
        return expInfo

    def getErr(self):
        if len(self.Err)!=0:
            return self.Err
        #获取输入文本框的值
        

    def stepOp(self,flag):
        """flag 取值为next(),last(),save(2).分别代表上一步 暂存 下一步  
        """
        dr=self.driver
        """上一步 暂存 下一步"""
        stepList=Mytool.findClasses(dr,'lastStep')
        print "stepList lenght is:"+str(len(stepList))
        for i in range(0,len(stepList)):
            if flag == stepList[i].get_attribute("onclick"):
                print flag
                stepList[i].click()
                break
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

    def Query(self,uname):
        dr=self.driver
        Mytool.findId(dr,'exp_cname').send_keys(uname)
        stepList=Mytool.findClasses(dr,'lastStep')
        for att in stepList:
            if att.get_attribute("onclick")=="search_exp()":
                att.send_keys(Keys.ENTER)
                Mytool.findLink(dr,u"选择").send_keys(Keys.ENTER)

    def expertChoose(self,num):
        u"""选择专家 num represent how many experts you want to choose"""
        dr=self.driver
        expList=Mytool.findClasses(dr,'sc-a')          #存放页面“选择”的链接列表
        print "length of expList:"+str(len(expList))
        if isinstance(num,int):
            if num>=1 and num<=len(expList):
                for i in range(0,num):
                    expid=expList[i].get_attribute("exp_id")
                    print "expid:"+str(expid)
                    self.expIdList.append(expid)
                    expList[i].send_keys(Keys.ENTER)
            else:
                raise IndexError,IndexError('num is out of range')
        elif isinstance(num,list):
            print 'list'
            self.expIdList=list
            for k in range(len(num)):
                print num[k]
                for m in range(len(expList)):
                    if num[k]==int(expList[m].get_attribute("exp_id")):
                        expList[m].send_keys(Keys.ENTER)

        
    def chosedExp(self):
        u'''选中专家Tab'''
        dr=self.driver
        Mytool.findId(dr,"selected_exp").click()
        Mytool.getScreen(dr,"selected_exp")
        nameList=Mytool.findXpathes(dr,"//*[@id='chioces_exp']/*/td[2]/p[1]/span/a")
        chargeList=Mytool.findXpathes(dr,"//input[@class='moneyValue']")
        for i in range(len(self.expIdList)):
            choseExpDic={}
            choseExpDic['name']=nameList[i].text
            choseExpDic['charge']=chargeList[i].get_attribute('value')
            choseExpDic['expid']=self.expIdList[i]
            self.List.append(choseExpDic)
        

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
        u"""
        flag:Q represent FIND_QUESTION;E represent FIND_EXPERT
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
        recordTime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ti=str(exp_time)
        reply_time.send_keys(ti)

        expFee=Mytool.findId(dr,'payment_money').text
        commission=Mytool.findId(dr,'payment_yj').text
        totalCost=Mytool.findId(dr,'xf_money').text
        self.recordDic['expFee']=float(expFee)
        self.recordDic['commission']=float(commission)
        self.recordDic['totalCost']=float(totalCost)
        self.recordDic['recordTime']=recordTime
        self.recordDic['reply_time']=ti

        if flag=="Q":
            Mytool.findCss(dr,"#payment_pwd>input").send_keys("888888")
        elif flag=="E":
            Mytool.findId(dr,"payment_pwd").send_keys("888888")
            time.sleep(3)
        self.stepOp("save(5)")
        time.sleep(2)
        if Mytool.findClass(dr,"s_ok"):
            Mytool.findClass(dr,"s_ok").click()
        else:
            raise AssertionError,AssertionError("failed paying")
    
    def getQuestionNo(self):
        dr=self.driver
        cur_url=dr.current_url
        exp_url=self.base_url+'/memquestion/question.do'
        if cur_url!=exp_url:
            dr.get(exp_url)
            time.sleep(1)
        xpath="//*[@id='all']/tbody/tr[1]/td[1]"
        no=Mytool.findXpath(dr,xpath).get_attribute('title')
        self.recordDic['questionNo']=no

    def getTotalprice(self):
        '''return the expert cost add on the fee'''
        listAmount=Mytool.getDict("listAmount")
        priceAmount=Mytool.getDict("priceAmount")
        totalPrice=float(listAmount)*float(priceAmount)
        return totalPrice
    
    def getAccount(self):
        u'''获取会员的账户情况'''
        dr=self.driver
        url='/pages/member_center.do'
        dr.get(self.base_url+url)
        time.sleep(2)
        totalAccount=float(Mytool.findId(dr,'sum').text.lstrip('￥'))
        availableAccount=float(Mytool.findId(dr,'avlb').text.lstrip('￥'))
        freezeAccount=float(Mytool.findId(dr,'frz').text.lstrip('￥'))
        accoutnDic={'total':totalAccount,
                    'avail':availableAccount,
                    'freeze':freezeAccount}
        return accoutnDic

    def detailOfInAndOut(self,filename):
        dr=self.driver
        url='/pages/user_charge.do'
        dr.get(self.base_url+url)
        time.sleep(2)
        dr.get_screenshot_as_file(filename)

    def returnDic(self):
        outputDict=self.recordDic 
        return outputDict

