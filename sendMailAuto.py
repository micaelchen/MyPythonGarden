#! python3
# -*- coding: utf-8 -*
import os,sys,time
from selenium import webdriver
from selenium.webdriver. common.keys import Keys

browser=webdriver.Firefox()    #Open the firefox
browser.get('https://mail.126.com/')
#try:
browser.implicitly_wait(10)
browser.switch_to.frame('x-URS-iframe')
accountTxt=browser.find_element_by_name('email')
accountTxt.clear()
accountTxt.send_keys('XXXXXXXX')   #Set your mail account
passwordTxt=browser.find_element_by_name('password')
passwordTxt.send_keys('**********',Keys.ENTER)  #Set your mail's password and click Enter
browser.implicitly_wait(10)
browser.switch_to.default_content()
logMailBtn=browser.find_element_by_xpath("//div[@id='dvNavTop']/ul/li[2]/span[2]")
logMailBtn.click()
time.sleep(2)
browser.switch_to.default_content()
browser.find_element_by_class_name('nui-editableAddr-ipt').send_keys('280395474@qq.com')
#browser.find_element_by_class_name('nui-ipt-input').send_keys('Auto send Python mail')
browser.find_element_by_xpath("//input[@class='nui-ipt-input' and @maxlength='256' and @type='text']").send_keys('Auto send Python mail')
xpath=browser.find_element_by_xpath("//div[@class='APP-editor-edtr']/iframe")
browser.switch_to.frame(xpath)
browser.find_element_by_class_name('nui-scroll').send_keys('''
Dear,
  This is my first mail sent by bot!
thanks
Michael''')
browser.switch_to.default_content()
sendMailBtn=browser.find_element_by_xpath("//footer[@class='jp0']/div/span[2]")
print(type(sendMailBtn))
sendMailBtn.click()
time.sleep(5)
browser.quit()
# except:
#     print('some issue need handle')

