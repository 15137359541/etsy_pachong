# coding=utf-8
from selenium import webdriver
import requests
# 线程等待着2秒钟，直接操作浏览器的方式，那么我自己在操作浏览器的时候，也会有所停留
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# 启动谷歌浏览器
# PhantomJS同谷歌火狐一样，是个没有图形界面的浏览器
driver = webdriver.Chrome()
driver.get('https://www.etsy.com/listing/469233405/')
try:
#显示等待,面的代码最多等待 10 秒，超时后就抛出 TimeoutException，假设在第3秒就找到了这个元素，那么也就不会多等剩下的7秒使时间，而是继续执行后续代码。

    element = WebDriverWait(driver,10,0.5).until(ec.presence_of_all_elements_located((By.ID,"reviews")))
finally:
    #找到评论中more按钮，彰显出更多评论
    elem = driver.find_element_by_xpath('//*[@id="reviews"]/div/button')
    # 敲回车了
    elem.click()
    time.sleep(0.5)

# 浏览器刷新
    # driver.refresh()
    #获取更过评论链接
    elem = driver.find_element_by_xpath('//*[@id="reviews"]/div/div[3]/a')
    #获取到对象，再用一下两种方法可以获取地址
    #  elem.get_property("href")
    feedbackUrl= elem.get_attribute("href")
    print feedbackUrl


# print driver.page_source
