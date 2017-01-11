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
    def __init__(self,driver):
        self.driver=driver
       # self.path='f:\\WorkSpace\\python\\excel\\new.csv'
        self.righturl="http://192.168.11.181:8080/JSFW/pages/exphome.do"
    def Login(self,uname,pw):
        """登录"""
        dr=self.driver
        Mytool.findId(dr,"username",uname)
        Mytool.findId(dr,"password",pw)
        time.sleep(3)
        Mytool.findClass(dr,"s_btn_logins").click()
        time.sleep(3)
        if dr.current_url==self.righturl:
            name=Mytool.findId(dr,"u_emp_name").value
            no=Mytool.findId(dr,"u_cust_co").value
#注册页面  Undone
    def Register(self):
        dr=self.driver
        Mytool.findClass(dr,'s_free').click()
        time.sleep(2)
        cur_url=dr.current_url
