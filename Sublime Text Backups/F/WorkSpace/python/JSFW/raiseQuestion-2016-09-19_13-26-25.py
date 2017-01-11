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


class raiseQuestion:
    def __init__(self,driver):
        self.driver=driver
       # self.path='f:\\WorkSpace\\python\\excel\\new.csv'
    def raiseQuestion(self):
        
        expect_url='http://192.168.11.181:8080/JSFW/problem/find_problem.do'
        dr=self.driver
        Mytool.findClass(dr,"sc-matter").click()
        time.sleep(2)
        cur_url=dr.current_url
        assert expect_url==cur_url,"url wrong"
        Mytool.findClass(dr,"s_btn_logins").click()
        dr.implicitly_wait(10)
        

#注册页面  Undone
    def Register(self):
        dr=self.driver
        Mytool.findClass(dr,'s_free').click()
        time.sleep(2)
        cur_url=dr.current_url

    def Question(self):
        driver=self.driver
        Mytool.findId(driver,"address_btn").click()
        self.driver.find_element_by_id("wh_addr_id").click()
        self.driver.find_element_by_link_text(u"甘肃").click()
        self.driver.find_element_by_link_text(u"临夏回族自治州").click()
        self.driver.find_element_by_link_text(u"临夏县").click()
        self.driver.find_element_by_id("addr_id").clear()
        self.driver.find_element_by_id("addr_id").send_keys(u"撒地方")
        Mytool.findClass(driver,"ok1").click()
        #获取输入文本框的值
        

#选择保证金货信用金挂牌时，选择品种等
#xpath路经应该是这种类型
    def goods_pick(self,i=0,j=0):
        """i 代表品种选择第i个
            j代表品名选择第j个  
        """
        driver=self.driver
        Mytool.findId(driver,"btn_add").click()

        elem=self.driver.find_element_by_xpath('//*[@id="addgoodsForm"]/div[1]/div[2]/div[1]/div[1]/div/div/div/div/div')
        ActionChains(self.driver).click(elem).perform()
        listid=elem.get_attribute("aria-haspopup")

        listid="ks-content-"+str(listid)
        print listid
        lists=self.driver.find_elements_by_css_selector("div#"+listid+">div")
        print len(lists)
        ActionChains(self.driver).move_to_element(lists[i]).send_keys(Keys.ENTER).perform()
        variety=self.driver.find_element_by_name("cat_id_txt").get_attribute("value")
        self.driver.implicitly_wait(10)
#品名
        trade_name=Mytool.downList(driver,"goods_name_input","a.list-group-item",j)
        time.sleep(1)
        Mytool.setDict("variety",variety)
        Mytool.setDict("trade_name",trade_name)
        
 #商品属性  
    def Goods_attr(self):
        """商品属性 都选择下拉列表中第一个属性"""
        self.driver.find_element_by_id('att14_tg').click()
        time.sleep(1)
        standardList=self.driver.find_elements_by_css_selector('a[role="link-#att14_ip"]')
        #print type(standardList)
        if not standardList:
            print "no standard value"
            specification=""
        else:
            specification=standardList[0].text
            standardList[0].click()

        self.driver.find_element_by_id('att3_tg').click()
        time.sleep(1)
        typeList=self.driver.find_elements_by_css_selector('a[role="link-#att3_ip"]')
        if not typeList:
            print "no type value"
            model=""
        else:
            print "list length:%d"%len(typeList)
            model=typeList[0].text
            ActionChains(self.driver).move_to_element(typeList[0]).click().perform()
            #typeList[0].click
            time.sleep(5)
        self.driver.find_element_by_id('att7_tg').click()
        time.sleep(1)
        originList=self.driver.find_elements_by_css_selector('a[role="link-#att7_ip"]')
        if not originList:
            print "no origin value"
            origin=""
        else:
            origin=originList[0].text
            ActionChains(self.driver).move_to_element(originList[0]).click().perform()
            

        self.driver.find_element_by_id('att13_tg').click()
        time.sleep(1)
        descripList=self.driver.find_elements_by_css_selector('a[role="link-#att13_ip"]')
        if not descripList:
            print "no description value"
            instruction=""
        else:
            instruction=descripList[0].text
            ActionChains(self.driver).move_to_element(descripList[0]).click().perform()
            
        self.driver.find_element_by_id('att6_tg').click()
        time.sleep(1)
        codeList=self.driver.find_elements_by_css_selector('a[role="link-#att6_ip"]')
        if not codeList:
            print "no code value"
            coding=""
        else:
            coding=codeList[0].text
            ActionChains(self.driver).move_to_element(codeList[0]).click().perform()

        Mytool.setDict("specification",specification)
        Mytool.setDict("model",model)
        Mytool.setDict("origin",origin)
        Mytool.setDict("instruction",instruction)
        Mytool.setDict("coding",coding)

    def intro(self,path,ids="bx_intro"):
        """商品描述"""
        word=open(path,'r')
        intro=word.read()
        s=intro.decode("gbk")
        print "intro"
        self.driver.find_element_by_id(ids).send_keys(s)

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

    def trade_info(self,nego,num,minum,pricenum):
        """nego:1 一口价 2 洽谈
            num 挂牌量
            minum 起购量
            pricenum 单价
        """
        negoList=self.driver.find_elements_by_name("trade_class")
        if nego==1:
            Mytool.setDict("bidway",u"一口价")
        elif nego==2:
            negoList[1].click()
            Mytool.setDict("bidway",u"可洽谈")
        if self.driver.find_element_by_id("weight_avb").is_displayed():
            Total_amount=self.driver.find_element_by_id("weight_avb")
            totalnum=self.driver.execute_script('return document.getElementById("weight_avb").value')
            Mytool.setDict("totalnum",totalnum)
        
        amount=self.driver.find_element_by_id("provided_qtt_id")
        amount.clear()
        amount.send_keys(num)
        listAmount=self.driver.execute_script('return document.getElementById("provided_qtt_id").value')
        Mytool.setDict("listAmount",listAmount)

        min_amount=self.driver.find_element_by_id("min_batch_qtt_id")
        min_amount.clear()
        min_amount.send_keys(minum)
        minAmount=self.driver.execute_script('return document.getElementById("min_batch_qtt_id").value')
        Mytool.setDict("minAmount",minAmount)

        price=self.driver.find_element_by_id("order_price_id")
        price.clear()
        price.send_keys(pricenum)
        priceAmount=self.driver.execute_script('return document.getElementById("order_price_id").value')
        Mytool.setDict("priceAmount",priceAmount)
        unit=self.driver.execute_script('return document.getElementById("weight_unit_name").value')
        weight=self.driver.find_element_by_css_selector("input[name='att5_id_txt']").get_attribute("value")
        Mytool.setDict("unit",unit)
        Mytool.setDict("weight",weight)
    

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

