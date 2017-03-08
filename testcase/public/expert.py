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
        self.comdict={}#save all the message
        self.baseurl=url
        self.expInfoDic={}
    
    def getcomDict(self):
        u'get the messages'
        return self.comdict

    def getexpInfoDict(self):
        u'get the messages'
        return self.expInfoDic

    def getExpAccount(self):
        u"""获取专家账户总资金 可用资金 冻结资金 本月收入"""
        dr=self.driver
        exp="/pages/exphome.do"
        expurl=self.baseurl+exp
        totalAccount=Mytool.findId(dr,"all_money").text
        availableMoney=Mytool.findId(dr,"ky_money").text
        freezeMoney=Mytool.findId(dr,"dj_money").text
        monthMoney=Mytool.findId(dr,"mouth_account").text
        self.comdict['totalAccount']=totalAccount
        self.comdict['availableMoney']=availableMoney
        self.comdict['freezeMoney']=freezeMoney
        self.comdict['monthMoney']=monthMoney

    def Info(self):
        """专家信息"""  
        #expect_url='http://192.168.11.181:8080/JSFW/problem/find_problem.do'
        dr=self.driver
        url='/JSFW/expmsg/expert_info.do?view=expert_info'
        dr.get(self.baseurl+url)
        time.sleep(3)
        userName=Mytool.findId(dr,"emp_acct")
        realName=Mytool.findId(dr,"user_realname")
        ename=Mytool.findId(dr,'user_ename')
        sex=Mytool.findCsses(dr,".radio_p")
        birthday=Mytool.findId(dr,"brithday")
        email=Mytool.findId(dr,"user_email")
        quhao=Mytool.findId(dr,"quhao")
        user_telephone=Mytool.findId(dr,"user_telephone")
        # homePh=quhao+user_telephone
        # pro=dr.execute_script("document.getElementById('province').value")
        # city=dr.execute_script("document.getElementById('city').value")
        # country=dr.execute_script("document.getElementById('county').value")
        detail_addr=Mytool.findId(dr,"detail_add")
        # complete_addr=pro+city+country+detail_addr
        Mytool.scroll(dr,800)
        graduate_sch=Mytool.findId(dr,"exp_graduate_school")
        degree=Mytool.findId(dr,"data_s8")
        company=Mytool.findId(dr,"user_comwork")
        professional=Mytool.findId(dr,"exp_js_title")
        comPhone=Mytool.findId(dr,"exp_comphone")
        duty=Mytool.findId(dr,"exp_compost")
        fax=Mytool.findId(dr,"user_fax")
        zipcode=Mytool.findId(dr,"user_zipcode")
        exp_tpyes=Mytool.findCsses(dr,"input[type='checkbox']")
        # exp_typeL=[]
        # if len(exp_tpyes)>0:
        #     for i in exp_tpyes:
        #         if exp_tpyes[i].get_attribute("checked"):
        #             exp_typeL.append(exp_tpyes[i].text)
        # else:
        #     exp_typeL.append(Mytool.findId(dr,"qt_exp"))
        remark=Mytool.findId(dr,"s19")
        self.expInfoDic={'userName':userName,
                         'realName':realName,
                         'ename':ename,
                         'sex':sex,
                         'birthday':birthday,
                         'email':email,
                         'quhao':quhao,
                         'user_telephone':user_telephone,
                         'graduate_sch':graduate_sch,
                         'degree':degree,
                         'company':company,
                         'professional':professional,
                         'comPhone':comPhone,
                         'duty':duty,
                         'fax':fax,
                         'zipcode':zipcode,
                         'exp_type':exp_tpyes,
                         'remark':remark,
        }

    def setInfo(self,infoDic):
        dr=self.driver
        self.Info()
        self.expInfoDic['realName'].send_keys(infoDic['realName'])
        self.expInfoDic['ename'].send_keys(infoDic['ename'])
        self.expInfoDic['sex'][infoDic['sex']].click()
        Mytool.selectList(dr,"years",infoDic['year'])
        Mytool.selectList(dr,"months",infoDic['month'])
        Mytool.selectList(dr,"days",infoDic['day'])
        self.expInfoDic['realName']=infoDic['realName']
        # self.expInfoDic['realName']=infoDic['realName']
        saveBtn=Mytool.findCss(dr,u"button[onclick='save()']")
        saveBtn.click()

    def getInfo(self):
        dr=self.driver
        getInfoL=[]
        url='/JSFW/expmsg/expert_info.do?view=expert_info'
        dr.get(self.baseurl+url)
        time.sleep(3)
        expInfoList=['emp_acct','user_realname','user_ename','brithday','user_email','province','city','county','quhao','user_telephone','detail_add',
                     'exp_js_title','data_s8','user_comwork','exp_compost','user_fax','user_zipcode','s19']
        for i in range(len(expInfoList)):
            val=dr.execute_script("return document.getElementById(arguments[0]).value",expInfoList[i])
            if val=='':
                val="null"
            getInfoL.append(val)
        sex=Mytool.findCss(dr,".radio_p[checked]").get_attribute('value')
        getInfoL.append(sex)
        expType=Mytool.findCsses(dr,"input[type='checkbox']")
        for j in range(len(expType)):
            if expType[j].get_attribute('checked'):
                tp=expType[j].get_attribute('id')
                getInfoL.append(tp)
        return getInfoL

    def eduHis(self):
        dr=self.driver
        hisList=Mytool.findCsses(dr,"#edu_tbody tr")
        if len(hisList):
            return hisList
        else:
            return False
    def addEdu(self,fr,to,scName,major='',remark=''):
        dr=self.driver
        Mytool.findCss(dr,"a[onclick='addEdu(false)']").click()
        Mytool.findId(dr,"edu_begin").send_keys(fr)
        Mytool.findId(dr,"edu_end").send_keys(to)
        Mytool.findId(dr,"edu_schoolname").send_keys(scName)
        Mytool.findId(dr,"edu_major").send_keys(major)
        Mytool.findId(dr,"edu_remarks").send_keys(remark)
        Mytool.findCss(dr,"span[onclick='addEduExp()']").send_keys(Keys.ENTER)

    def workHis(self):
        dr=self.driver
        hisList=Mytool.findCsses(dr,"#work_tbody tr")
        return hisList
    def addWork(self,fr,to,comName,title,remark=''):
        dr=self.driver
        Mytool.findCss(dr,"a[onclick='addWork(false)']").click()
        Mytool.findId(dr,"work_begin").send_keys(fr)
        Mytool.findId(dr,"work_end").send_keys(to)
        Mytool.findId(dr,"work_workunit").send_keys(comName)
        Mytool.findId(dr,"work_duty").send_keys(title)
        Mytool.findId(dr,"work_remarks").send_keys(remark)
        Mytool.findCss(dr,"span[onclick='addWorkExp()']").send_keys(Keys.ENTER)


    def myQuestion(self,No,opName):
        """我的问题"""  
        #expect_url='http://192.168.11.181:8080/JSFW/problem/find_problem.do'
        dr=self.driver
        exp="/pages/expert_question.do?view=expert_question"
        dr.get(self.baseurl+exp)
        # Mytool.findId(dr,"expert_question").click()
        time.sleep(2)
        ele=Mytool.findClass(dr,'my_question')
        ActionChains(dr).move_to_element(ele).perform()
        time.sleep(1)
        Mytool.findId(dr,"pro_id",No)
        self.comdict['questionNo']=No
        queryBt=Mytool.findClass(dr,"save_btn")
        resetBt=Mytool.findClass(dr,"return_btn")
        queryBt.send_keys(Keys.ENTER)

        state=Mytool.findXpath(dr,"//*[@id='expcenter_data']/tbody/tr/td[8]")
        stateV=state.get_attribute("title")
        btnList=Mytool.findClasses(dr,'look_btn')
        for btn in range(len(btnList)):
            value=btnList[btn].get_attribute("value")
            if value==opName:
                btnList[btn].send_keys(Keys.ENTER)
                time.sleep(2)
                break

    def Reply(self,text,Op,newmoney=0):
        dr=self.driver
        replayText=Mytool.findId(dr,'pro_re_det')
        replayText.send_keys(text)
        btDict={}
        btlist=Mytool.findClasses(dr,'sc_btn_to')
        for i in range(len(btlist)):
            if 'save(1)'==btlist[i].get_attribute('onclick'):
                btDict['reply']=btlist[i]
            elif 'canNotRe()'==btlist[i].get_attribute('onclick'):
                btDict['refuse']=btlist[i]
            elif 'toShow()'==btlist[i].get_attribute('onclick'):
                btDict['up']=btlist[i]
            else:
                break 
        btDict['back']=Mytool.findClass(dr,'sc_btn_bac')
        btDict[Op].click()
        time.sleep(1)
        if Op=='reply' or Op=='refuse': 
            self.comdict['replytime']=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            time.sleep(1)
            Mytool.findClass(dr,'s_ok').send_keys(Keys.ENTER)
        elif Op=='up':      #加价回复
            Mytool.findId(dr,'premium_money').send_keys(newmoney)
            Mytool.findClass(dr,'save_btn').send_keys(Keys.ENTER)
            time.sleep(2)
            Mytool.getScreen(dr,"addMoney")
    def endQuestion(self):
        u'''结束问题'''
        dr=self.driver
        reasons=Mytool.findNames(dr,'end')
        reasons[0].click()
        btns=Mytool.findClasses(dr,'sc_btn_to')
        btns[0].click()

    def returnDic(self):
        self.dict=Mytool.returnMydic()
        print"the dict has:%s"%len(self.dict)
        return self.dict

