import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import cdata.mysql as mod
import plotly.graph_objs as go

mysql_connect = mod.connect("User=root; Password=helloworld; Database=NorthWind;")