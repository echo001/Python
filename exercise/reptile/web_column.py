#统计各个省份的IP，做分布图
#将数据库中的数据输出到web页面上
import os
import dash
import pandas as pd
import peewee
#import cdata.mysql as mod
#import plotly.graph_objs as go
from dash import dcc
from dash import html
from dash import dash_table
from peewee import *
#mysql_connect = mod.connect("User=root; Password=helloworld; Database=person; Server=localhost; Port=3306;")
#数据库设定，reptile数据库名，如果没有，需要进入mysql自建一个
db = MySQLDatabase('reptile', host='127.0.0.1', user='root', passwd='helloworld', port=3306)
db.connect()    #数据库连接
print(db.is_closed())   #判断数据库是不是链接好
df = pd.read_sql("SELECT Address FROM person", db)

str_df = ''.join(df)
print(str_df)
