#coding=utf-8
import  pymysql
import re
from GetPost import gets,posts
num=1
def get_cloth(url):
    global num
    res=gets(url=url)

    if res['issuccess'] !=1:
        return None
    else:
        print res["message"]

        # 简单处理页面
        html =res['message'].replace('\n', '').replace('\r', '').replace('\t', '')
        list_urls=re.findall('<a        class=" display-inline-block listing-link"(.*?)href="(.*?)"',html)

        if len(list_urls) > 0 :
            for ever_url in list_urls:
                num +=1
                #
                # if num >=2:
                #     break
                # else:
                print("目前访问第%s个网页：%s,"% (num,ever_url[1],))
                # 商品的更多评论，有的selenium爬取
                # goodUrl = feedBack(ever_url[1])
                #对得到的地址做进一步的处理


        else:
            print '没有这个网页'

if __name__=="__main__":
    url='https://www.etsy.com/c/bath-and-beauty/skin-care?explicit=1&page=1'
    get_cloth(url)