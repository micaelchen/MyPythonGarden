#! python3
# -*- coding: utf-8 -*

import os,bs4,requests,time
from selenium import webdriver
from selenium.webdriver. common.keys import Keys
#Create xkcd folder
i=0
urlid = 13868039
if not os.path.exists('xkcd'):
    os.makedirs('xkcd')
# The URL for wangyi Pic
url = 'http://pp.163.com/group/5001/slide/0/' + str(urlid)
while i<3:
    print('Downloading the page %s...' % url)
    browser = webdriver.Firefox()  # Open the firefox
    browser.get(url)
    browser.implicitly_wait(10)
    link=browser.find_element_by_xpath("//*[@id='p_slide_img']")   # get the iamge,it must use the xpath
    picUrl=link.get_attribute('src')   # get the element's src
    print(picUrl)

    res=requests.get(picUrl)    #Start to download the pic
    res.raise_for_status()
    #create a image file to load the image
    imageFile=open(os.path.join('xkcd',os.path.basename(picUrl)),'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()           #end to download the pic
    nextButton=browser.find_element_by_xpath("//*[@id='p_slide_next']") #get the next button,it must use the xpath
    url=nextButton.get_attribute('href') # get the href
    browser.quit()
    i=i+1
print('Done...')


