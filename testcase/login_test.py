#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import pdb
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,sys
sys.path.append("public")
from public import login
from public import Mytool
import os,datetime
import HTMLTestRunner

class Login_Test(unittest.TestCase):
    def setUp(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        self.driver.implicitly_wait(30)
        #self.base_url = "http://218.249.25.106:15301/JSFW"
        # self.base_url = "http://218.249.15.107"
        self.base_url = "http://192.168.11.181:8080"
        self.verificationErrors = []
        self.accept_next_alert = True
        #self.f=open("f:/workspace/python/data.txt","w")
        self.driver.maximize_window()

    def  test_case1(self):
        u"""用户登录"""
        dr=self.driver
        lg=login.Login(dr,self.base_url)
        lg.Login("qiuwj3",888888)
        username=Mytool.findId(dr,"u_emp_name").get_attribute("value")
        self.assertEqual(username,u"邱文静2")

    def  test_case2(self):
        u"""会员注册链接"""
        dr=self.driver
        expurl=self.base_url+"/JSFW/webpages/user_register.jsp"
        dr.get(self.base_url+'/JSFW/user/login.do')
        Mytool.findPartialLink(dr,u"会员").click()
        time.sleep(1)
        currurl=dr.current_url
        try:
            self.assertEqual(expurl,currurl)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_case3(self):
        u"""个人注册账号文本框"""
        dr=self.driver
        expurl=self.base_url+"/JSFW/webpages/user_register.jsp"
        dr.get(self.base_url+'/JSFW/user/login.do')
        Mytool.findPartialLink(dr,u"会员").click()
        time.sleep(1)
        currurl=dr.current_url
        try:
            self.assertEqual(expurl,currurl)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        user=login.Login(dr,self.base_url)
        udict=user.userRegister()
        udict["account"].send_keys("111")
        udict["mobile"].send_keys(18782943855)
        try:
            err=Mytool.findCss(dr,"#user_member_error span").text
            self.assertIn(u"正确",err)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_case4(self):
        u"""个人注册手机文本框"""
        dr=self.driver
        expurl=self.base_url+"/JSFW/webpages/user_register.jsp"
        dr.get(self.base_url+'/JSFW/user/login.do')
        Mytool.findPartialLink(dr,u"会员").click()
        time.sleep(1)
        currurl=dr.current_url
        try:
            self.assertEqual(expurl,currurl)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        user=login.Login(dr,self.base_url)
        udict=user.userRegister()
        udict["account"].send_keys("a18782943855")
        udict["mobile"].send_keys('ad1249873~!')
        udict["pwd"].send_keys('888888')
        try:
            err=Mytool.findCss(dr,"#user_mobile_error span").text
            self.assertIn(u"正确",err)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_case5(self):
        u"""个人注册密码文本框"""
        dr=self.driver
        expurl=self.base_url+"/JSFW/webpages/user_register.jsp"
        dr.get(self.base_url+'/JSFW/user/login.do')
        Mytool.findPartialLink(dr,u"会员").click()
        time.sleep(1)
        currurl=dr.current_url
        try:
            self.assertEqual(expurl,currurl)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        user=login.Login(dr,self.base_url)
        udict=user.userRegister()
        udict["account"].send_keys("a18782943855")
        udict["mobile"].send_keys('18782943855')
        udict["pwd"].send_keys('111s2')
        udict["pwd1"].send_keys('111s2')
        try:
            err=Mytool.findCss(dr,"#user_pwd_error span").text
            self.assertIn(u"正确",err,u"长度未验证")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        finally:
            udict["pwd"].send_keys('111s3@#1111111111')
            udict["pwd1"].send_keys('111s2')
        try:
            err=Mytool.findCss(dr,"#user_pwd_error span").text
            Mytool.getScreen(dr,"userpwderror")
            self.assertIn(u"正确",err,u"length more than 16")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        finally:
            udict["pwd"].send_keys('111s3@#')
            udict["pwd1"].send_keys('111s2')
        try:
            err=Mytool.findCss(dr,"#user_pwd_error span").text
            self.assertIn(u"正确",err,u"format wrong")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_case6(self):
        u"""个人注册确认密码文本框"""
        dr=self.driver
        expurl=self.base_url+"/JSFW/webpages/user_register.jsp"
        dr.get(self.base_url+'/JSFW/user/login.do')
        Mytool.findPartialLink(dr,u"会员").click()
        time.sleep(1)
        currurl=dr.current_url
        try:
            self.assertEqual(expurl,currurl)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        user=login.Login(dr,self.base_url)
        udict=user.userRegister()
        udict["account"].send_keys("a18782943855")
        udict["mobile"].send_keys('18782943855')
        udict["pwd"].send_keys('888888')
        udict["pwd1"].send_keys('111s2')
        udict["yzm"].send_keys("1111")
        try:
            err=Mytool.findCss(dr,"#user_pwd_error_12 span").text
            self.assertIn(u"不匹配",err,u"undone compare")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
    def test_case7(self):
        u"""个人注册验证码文本框"""
        dr=self.driver
        expurl=self.base_url+"/JSFW/webpages/user_register.jsp"
        dr.get(self.base_url+'/JSFW/user/login.do')
        Mytool.findPartialLink(dr,u"会员").click()
        time.sleep(1)
        currurl=dr.current_url
        try:
            self.assertEqual(expurl,currurl)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        user=login.Login(dr,self.base_url)
        udict=user.userRegister()
        udict["account"].send_keys("a18782943855")
        udict["mobile"].send_keys('18782943855')
        udict["pwd"].send_keys('888888')
        udict["pwd1"].send_keys('888888')
        udict["yzm"].send_keys("")
        udict["mobtn"].click()
        try:
            err=dr.switch_to_alert().text
            print err
            self.assertIn(u"错误",err)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        finally:
            time.sleep(3)
            
    def test_case8(self):
        u"""个人注册手机验证码文本框"""
        dr=self.driver
        expurl=self.base_url+"/JSFW/webpages/user_register.jsp"
        dr.get(self.base_url+'/JSFW/user/login.do')
        Mytool.findPartialLink(dr,u"会员").click()
        time.sleep(1)
        currurl=dr.current_url
        try:
            self.assertEqual(expurl,currurl)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        user=login.Login(dr,self.base_url)
        udict=user.userRegister()
        udict["account"].send_keys("a18782943855")
        udict["mobile"].send_keys('QWEEEEE')
        udict["pwd"].send_keys('888888')
        udict["pwd1"].send_keys('888888')
        udict["yzm"].send_keys("")
        time.sleep(3)
        udict["mobtn"].click()
        try:
            err=Mytool.findCss(dr,"#user_phoneyzm_error_12 span").text
            print err
            self.assertIn(u"错误",err)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    """def Question_Passby(self):

        path='F:\\WorkSpace\\python\\JSFW\\testcase\\testcase.xls'
        Mytool.readExec(path)
        initDict=Mytool.returnMydic()
        driver = self.driver
        driver.delete_all_cookies()
        driver.get(self.base_url + "/home/unlogin.do")
        li=Login(driver,self.base_url)
        li.Login(initDict['uname'],initDict['pwd'])  
        time.sleep(3) 
        RQ=raiseQuestion(driver,self.base_url)
        initAccount=RQ.getAccount()
        Mytool.getScreen(driver,"initAccount")
        RQ.raiseQuestion(u'基础软件',initDict['detail'])
        # RQ.findExpert(initDict['detail'],initDict['choseExp'],initDict['questionType'],initDict['answerNum'],initDict['lastDay'])
        dic=RQ.returnDic()
        secAccount=RQ.getAccount()
        Mytool.getScreen(driver,"secAccount")
        try:self.assertEqual(initAccount['total'],secAccount['total'],'check the money')
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        cost=initAccount['avail']-secAccount['avail']
        try:self.assertAlmostEqual(cost,dic['totalCost'],1)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print cost
            print dic['totalCost']
        no=dic["questionNo"].replace(' ','')
        Mytool.getScreen(driver, no)
        HY=Person(driver,self.base_url)
        HY.user_Charge(no)
        time.sleep(2)
        Mytool.getScreen(driver,"userCharge")
        Mytool.saveExc('F:\\WorkSpace\\python\\JSFW\\testcase\\output.xls',initAccount,True)
        # Mytool.saveExc('F:\\WorkSpace\\python\\JSFW\\testcase\\output.xls',initDict['uname'])
        Mytool.saveExc('F:\\WorkSpace\\python\\JSFW\\testcase\\output.xls',dic)
        # RQ.printExp()

    def ExpertReply(self):
        initDict={
            'uname':'qiuwjcom4',
            'pwd':888888,
            'detail':u'资金验证-追问 推送-资金测试',
            'choseExp':2,
            'questionType':1,
            'answerNum':1,
            'lastDay':0,
        }
        driver = self.driver
        driver.delete_all_cookies()
        driver.get(self.base_url + "/home/unlogin.do")
        li=Login(driver)
        li.Login(initDict['uname'],initDict['pwd'])
        time.sleep(3)
        RQ=raiseQuestion(driver,self.base_url)
        initAccount=RQ.getAccount()
        Mytool.getScreen(driver,"initAccount")
        RQ.findExpert(initDict['detail'],initDict['choseExp'],initDict['questionType'],initDict['answerNum'],initDict['lastDay'])
        explist=RQ.getChoseExp()
        # print len(explist)
        dic=RQ.returnDic()
        secAccount=RQ.getAccount()
        Mytool.getScreen(driver,"secAccount")
        try:self.assertEqual(initAccount['total'],secAccount['total'],'check the money')
        except AssertionError as e: self.verificationErrors.append(str(e))
        cost=initAccount['avail']-secAccount['avail']
        try:self.assertAlmostEqual(cost,dic['totalCost'],1)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print cost
            print dic['totalCost']
        no=dic["questionNo"].replace(' ','')
        dic["uname"]=li.getName()
        expid=explist
        Mytool.getScreen(driver, no)
        HY=Person(driver,self.base_url)
        HY.user_Charge(no)
        time.sleep(2)
        Mytool.getScreen(driver,"userCharge")
        li.Logout()
        Mytool.saveExc('F:\\WorkSpace\\python\\JSFW\\testcase\\output.xls',initAccount,True)
        Mytool.saveExc('F:\\WorkSpace\\python\\JSFW\\testcase\\output.xls',dic)
        expList=[]
        for i in range(len(expid)):
             expList.append(expid[i]["expid"])
        for i in range(len(expList)):
            li.Login(expList[i],888888)
            time.sleep(3)
            Exp=Expert(driver,self.base_url)
            Exp.getExpAccount()
            account=Exp.getDict()
            account['uname']=li.getName()
            Mytool.getScreen(driver)
            Exp.myQuestion(no,u'回复')
            time.sleep(1)
            Exp.Reply('reply','reply')
            if expList[i]=="15":
                Exp.myQuestion(no,u'结束问题')
                Exp.endQuestion()
            Mytool.saveExc('F:\\WorkSpace\\python\\JSFW\\testcase\\money.xls',account,True)


        li.Login(initDict['uname'],initDict['pwd'])
        time.sleep(3)
        Qs=Person(driver,self.base_url)
        Qs.AnswerQuestion(no)
        Qs.add_Question()
    def addQuestion(self):
         initDict={
            'uname':'qiuwjcom4',
            'pwd':888888,
            'detail':u'资金验证-追问回复截止时间-资金测试',
             'no':'jszx20170120142657'
         }
         # no='jszx20170118144844'
         driver = self.driver
         driver.delete_all_cookies()
         driver.get(self.base_url + "/home/unlogin.do")
         li=Login(driver)
         li.Login(initDict['uname'],initDict['pwd'])
         time.sleep(3)
         Qs=Person(driver,self.base_url)
         Qs.AnswerQuestion(initDict['no'])
         Qs.add_Question()

    def checkQuestion(self):
        u'''截止日期测试'''
        dataInit={
            'username':'qiuwjn2',
            'pwd':888888,
        }
        questionExpectData={
            'Qstate':u'完成',
            'deadtime':'2017-01-15',
            'cost':600,
            'questionNo':'',
        }
        driver = self.driver
        driver.delete_all_cookies()
        driver.get(self.base_url + "/home/unlogin.do")
        li=Login(driver)
        li.Login(dataInit['username'],dataInit['pwd'])
        time.sleep(3) 
        p=Person(driver,self.base_url)
        p.MyQuestion(questionExpectData['questionNo'])
        try:self.assertEqual(u"完成",Mytool.getDict("state"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try:self.assertEqual("2016-12-15",Mytool.getDict("deadTime"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try:self.assertEqual("600",Mytool.getDict("cost"),"cost wrong")
        except AssertionError as e: 
            self.verificationErrors.append(str(e))
        
    def checkExpInfo(self):
        dataInit={
            'username':'chenglong',
            'pwd':888888,
        }
        driver = self.driver
        expInfoDic={
            'userName':'chenglong',
            'realName':u'程龙',
            'ename':u'LongCheng',
            'sex':0,
            'year':'1990',
            'month':'9',
            'day':'11'
            # 'email':email,
            # 'quhao':quhao,
            # 'user_telephone':user_telephone,
            # 'graduate_sch':graduate_sch,
            # 'degree':degree,
            # 'company':company,
            # 'professional':professional,
            # 'comPhone':comPhone,
            # 'duty':duty,
            # 'fax':fax,
            # 'zipcode':zipcode,
            # 'exp_type':exp_tpyes,
            # 'remark':remark,
        }
        driver.delete_all_cookies()
        driver.get(self.base_url + "/home/unlogin.do")
        li=Login(driver,self.base_url )
        li.Login(dataInit['username'],dataInit['pwd'])
        time.sleep(3)
        expInfo=Expert(driver,self.base_url)
        expInfo.getInfo()

        # try:self.assertIn(u"中文格式错误",Mytool.findId(driver,"user_realname_error").text)
        # except AssertionError as e: self.verificationErrors.append(str(e))
        #
        # try:self.assertIn(u"英文格式错误",Mytool.findId(driver,"user_ename_error").text)
        # except AssertionError as e: self.verificationErrors.append(str(e))

    def readExcel(self):
        path='F:\\WorkSpace\\python\\JSFW\\testcase\\testcase.xls'
        Mytool.clearMydic()
        Mytool.readExec(path)
        initDict=Mytool.returnMydic()
        Mytool.printDict(initDict)
        lg=Login(self.driver,self.base_url)
        lg.Login("anxuejun",888888)
"""

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
    # testunit=unittest.TestSuite()
    # testunit.addTest(test("test_login"))
    #testunit.addTest(test("test_PersonCenter"))
    # testunit.addTest(test("Exp"))
    # testunit.addTest(test("ExpertReply"))
    # testunit.addTest(test("checkExpInfo"))
    # testunit.addTest(test("readExcel"))
    # testunit.addTest(test("ExpertReply"))
    # testunit.addTest(test("ExpertReply"))
    #  filename="f:\\WorkSpace\\python\\JSFW\\repoter.html"
    # fp=file(filename,'wb')
    # runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='testreport',description='caseRun')
    # runner.run(testunit)
    # runner=unittest.TextTestRunner()
    # runner.run(testunit)