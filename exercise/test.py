#url:https://proxy.ip3366.net/free/?action=china&page=1
import requests
import re
import time
import peewee
from peewee import *
from io import BytesIO
#content > section > div.container > table > tbody > tr:nth-child(5) > td:nth-child(1)
#数据库设定，reptile数据库名，如果没有，需要进入mysql自建一个
db = MySQLDatabase('reptile', host='127.0.0.1', user='root', passwd='Zpepc001@', port=3306)
db.connect()    #数据库连接
print(db.is_closed())   #判断数据库是不是链接好

class BaseModel(Model):
    class Meta:
        database = db
class Person(BaseModel):
    IP = CharField(verbose_name='IP', max_length=20, null=False, index=True)
    Port = CharField(verbose_name='Port', max_length=10, null=False)
    Address = CharField(verbose_name='地址', max_length=20)
    Business = CharField(verbose_name='运营商', max_length=20)
    class Meta:
        primary_key = CompositeKey('IP', 'Port')
#db.create_tables([Person]) 只需运行一次，已经创建好名为person的表
def store_data(data):
    try:    #联合主键设置，IP,Port数据一样时，插入数据产生报错
        Person.insert_many(data).execute()  #插入数据
    except:
        print('[Error]------data repetition------')

if __name__ == '__main__':
    data = [{'IP': '60.179.177.64', 'Port': '3000', 'Address': ['中国  浙江  宁波'], 'Business': ['电信']}]
    data1 = [{'IP': '59.55.162.106', 'Port': '3256', 'Address': ['中国  江西  吉安'], 'Business': ['电信']}]
    store_data(data)
    store_data(data1)
