import time
import re
import os
import stat
import base64
from selenium import webdriver
from bs4 import BeautifulSoup
from PIL import Image

#输入账号及密码
def put_message():
    driver.find_element_by_xpath("//div[@class='login-account']/div/input").send_keys('18815119265')
    driver.find_element_by_xpath("//div[@class='login-account']/div[2]/input").send_keys('********')
    
#进行图片验证,并且登陆
def login():
    solution = input('请输入验证码位置，以","分割[例如2,5]:')
    soList = solution.split(',')
    yanSol = [35,50,105,50,175,50,245,50,35,120,105,120,175,120,245,120]#'35,35','105,35','175,35','245,35','35,105','105,105','175,105','245,105'
    img=driver.find_element_by_xpath("//div[@id='J-loginImgArea']/img")
    imglocation=img.location
    #然后通过item*2，item*2+1分别获取x和y，再与获得的那个location相加，再通过鼠标点击。
    for item in soList:
        x=yanSol[int(item)*2]+imglocation.get('x')
        y=yanSol[int(item)*2+1]+imglocation.get('y')
        webdriver.ActionChains(driver).move_by_offset(x,y).click().perform()
        #将鼠标的坐标初始化
        webdriver.ActionChains(driver).move_by_offset(-x,-y).click().perform()
        print(x,y)
    time.sleep(10)
    driver.find_element_by_xpath("//a[@id='J-login']").click()


if __name__ == '__main__':
    driver=webdriver.Firefox()
    #进入12306并且切换至账号密码登陆
    url='https://kyfw.12306.cn/otn/resources/login.html'
    driver.get(url)
    time.sleep(3)
    driver.find_element_by_xpath("//ul[@class='login-hd']/li[2]/a").click()
    put_message()
    time.sleep(3)
    login()
     


