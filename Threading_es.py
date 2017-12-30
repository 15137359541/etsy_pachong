#coding=utf-8
import threading
from Etsy import getPage
threads = []
url1='https://www.etsy.com/c/bath-and-beauty/skin-care?explicit=1&page='
url2='https://www.etsy.com/c/accessories/hair-accessories?explicit=1&page='


t1 = threading.Thread(target=getPage,args=(1,2,url1))
threads.append(t1)
t2 = threading.Thread(target=getPage,args=(1,2,url2))
threads.append(t2)

# t2 = threading.Thread(target=startbangong)
# threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        if t.isAlive() == False:
            t.start()