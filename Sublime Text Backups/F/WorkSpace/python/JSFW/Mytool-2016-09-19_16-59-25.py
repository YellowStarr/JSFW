#coding=utf-8
import xlrd
import xlwt
import os,time
from xlutils.copy import copy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
myDict={}
def saveExc(path,title,val):
  row=0
  wb=''
  if(os.path.exists(path)):
    data=xlrd.open_workbook(path)
    ta=data.sheets()[0]
    row=ta.nrows
    wb=xlwt.Workbook()
    wb=copy(data)
    table=wb.get_sheet(0)
  else:
    wb=xlwt.Workbook()
    table=wb.add_sheet(u"data1")
  table.write(row,0,title)
  table.write(row,1,val)
  wb.save(path)
  print "rows:%s "%(row+1)
 
def readExec(path,title):
  """读取excel文件内容"""
  if(os.path.exists(path)):
    data=xlrd.open_workbook(path)
    ta=data.sheets()[0]
    rows=ta.nrows
    cols=ta.ncols
    for i in range(rows):
      #for j in range(cols):
      key=ta.cell(i,0).value
      value=ta.cell(i,1).value
      setDict(key,value)

def setDict(key,value):
  if not myDict.has_key(key):
    myDict[key]=value
  else:
    raise ValueError('the key has already in dictionary')
def getDict(key):
  if myDict.has_key(key):
    return myDict[key]

def returnMydic():
  return myDict

def printDict():
  if myDict:
    for k in myDict:
      print "key: %s"%k
      print "value is: %s"%myDict[k]

def findId(dri,id,value=""):
  ele=dri.find_element_by_id(id)
  if value:
    ele.clear()
    ele.send_keys(value)
    return
  else:
    return ele
def findClass(dri,classname):
  ele=dri.find_element_by_class_name(classname)
  return ele
def findClasses(dri,classname):
  ele=dri.find_elements_by_class_name(classname)
  return ele
def findXpath(dri,xpath):
  ele=dri.find_element_by_xpath(xpath)
  return ele
def findCss(dri,css):
  ele=dri.find_element_by_css_selector(css)
  return ele
def findCsses(dri,css):
  ele=dri.find_elements_by_css_selector(css)
  return ele
def findLink(dri,link):
  ele=dri.find_element_by_link_text(link)
  return ele
def findName(dri,name):
  ele=dri.find_element_by_name(name)
  return ele
def findTag(dri,tagname):
  ele=dri.find_element_by_tag_name(tagname)
  return ele
def findPartialLink(dri,para):
  ele=dri.find_element_by_partial_link_text(para)
  return ele

def getScreen(driver,path=u'f:\\workspace\\python',format="%y-%m-%d_%H_%M_%S"):
  now=time.strftime(format,time.localtime(time.time()))
  driver.get_screenshot_as_file(path+'\\%s.png'%now)

def verify(driver,result,expect):
  if result==expect:
    print "true"
  else:
    print"not equal"
    getScreen(driver)
    return result

def downList(driver,id,css,j):
  elem=findId(driver,id)
  ActionChains(driver).click(elem).perform()
  time.sleep(1)
  goodname_list=findCsses(driver,css)
  ActionChains(driver).click(goodname_list[j]).perform()
  trade_name=goodname_list[j].text
  return trade_name

def selectList(driver,id,xpath):
  """Traditional select list"""
  selectL=findId(driver,id)
  print id
  print selectL
  selectL.find_element_by_xpath(xpath).click()

def scroll(driver,ypoint):
  driver.execute_script("document.documentElement.scrollTop=arguments[0]",ypoint)

def chooseDate(driver,id,time):
  driver.execute_script("document.getElementById(arguments[0]).readOnly=false",id)
  findId(driver,id,time)

def getDataRules(str):
  minum=str.split(',')[1]
  maxine=str.split(',')[1]
  minVal=minum.split(':')[1]
  maxVal=maxine.split(':')[1]
  return [minVal,maxVal]
#uname=table.cell(0,0).value
#print rows
#print uname
#uname2='qiuwjcom2'#

#print rows
# 类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error


#table.put_cell(1,0,1,uname2,0)
#print table.cell(1,0)
#print table.cell(1,0).value

'''1、导入模块

      import xlrd

   2、打开Excel文件读取数据

       data = xlrd.open_workbook('excelFile.xls')

   3、使用技巧

        获取一个工作表

 

        table = data.sheets()[0]          #通过索引顺序获取
 
        table = data.sheet_by_index(0) #通过索引顺序获取
 

        table = data.sheet_by_name(u'Sheet1')#通过名称获取
 
        获取整行和整列的值（数组）
 　　
         table.row_values(i)
 
         table.col_values(i)
 
        获取行数和列数
　　
        nrows = table.nrows
 
        ncols = table.ncols
       
        循环行列表数据
        for i in range(nrows ):
      print table.row_values(i)
 
单元格
cell_A1 = table.cell(0,0).value
 
cell_C4 = table.cell(2,3).value
 
使用行列索引
cell_A1 = table.row(0)[0].value
 
cell_A2 = table.col(1)[0].value
 
简单的写入
row = 0
 
col = 0
 
# 类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
ctype = 1 value = '单元格的值'
 
xf = 0 # 扩展的格式化
 
table.put_cell(row, col, ctype, value, xf)
 
table.cell(0,0)  #单元格的值'
 
table.cell(0,0).value #单元格的值
'''