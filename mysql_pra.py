from templates_mysql import SqlHelper
num=0
good_num=5
def pollMysql(title,price_ago,price_now,feedback,favorited,img):
    global good_num
    good_sql=SqlHelper(host='localhost',port=3306,db='etsy',user='root',password='123456')
    good_one='insert into platformes_goods value(%s,%s,%s,%s,%s,%s,%s)'
    print [good_num,title,price_ago,price_now,feedback,favorited,img]
    good_one_name=(good_num,title,price_ago,price_now,feedback,favorited,img)
    print good_num
    good_num +=1
    count=good_sql.update(good_one,good_one_name)
    return count
if __name__=="__main__":
    pollMysql('The Office &quot;Meredith Rabies Awareness Fun Run&quot; Shirt S-4XL and Long Sleeve Available', '$15.99+', '$15.99+', '489', '1451', 'static/es_platform/img/4d64e8c0-e6d9-11e7-98f0-f0def183b657.jpg')