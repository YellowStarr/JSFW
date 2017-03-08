#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException 
import time,re,Mytool
import os,sys


class Login:
    def __init__(self,driver,url):
        self.driver=driver
       # self.path='f:\\WorkSpace\\python\\excel\\new.csv'
        self.baseurl=url
        self.name=''
    def Login(self,uname,pw):
        """登录"""
        dr=self.driver
        dr.get(self.baseurl+'/JSFW/user/login.do')
        Mytool.findId(dr,"username",uname)
        Mytool.findId(dr,"password",pw)
        time.sleep(3)
        Mytool.findClass(dr,"s_btn_logins").click()
        time.sleep(3)


#注册页面  Undone
    def userRegister(self):
        dr=self.driver
        user_account=Mytool.findId(dr,"user_member")
        user_mobile=Mytool.findId(dr,"user_mobile")
        user_pwd=Mytool.findId(dr,"user_password")
        user_pwd1=Mytool.findId(dr,"user_password1")
        user_yzm=Mytool.findId(dr,"user_yzm")
        mbtn=Mytool.findId(dr,"user_mobilecodeBtn")
        phone_yzm=Mytool.findId(dr,"user_phoneyzm")
        check_protocol=Mytool.findId(dr,"user_protocol")
        submit=Mytool.findTag(dr,"button")
        elemsDict={
            "account":user_account,
            "mobile":user_mobile,
            "pwd":user_pwd,
            "pwd1":user_pwd1,
            "yzm":user_yzm,
            "mobtn":mbtn,
            "moyzm":phone_yzm,
            "protocol":check_protocol,
            "submit":submit
        }
        return elemsDict



    def Logout(self):
        dr=self.driver
        Mytool.findCss(dr,"a[href='/JSFW/home/unlogin.do'").click()
        time.sleep(2)
