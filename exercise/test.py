import pandas as pd
data1 = {'IP': '49.86.9.86', 'Port': '9999', '地址': ['中国  江苏  扬州'], '运营商': ['电信']}
data2 = {'IP': '49.86.9.86', 'Port': '9999', '地址': ['中国  江苏  扬州'], '运营商': ['电信']}
data3 = list(data1)
pf = pd.DataFrame({'IP': '49.86.9.86', 'Port': '9999', '地址': ['中国  江苏  扬州'], '运营商': ['电信']})
order = ['IP', 'Port', '地址', '运营商'] #指定输出字段顺序
pf = pf[order]
columns = {
'IP':'IP',
'Port':'端口',
'地址':'地址',
'运营商':'运营商'
}
pf.rename(columns=columns)
file_path = pd.ExcelWriter('D:/test/Code/exercise/reptile/data/reptile_verify.xlsx')
pf.fillna(' ', inplace=True)    #替换空单元格
pf.to_excel(file_path, encoding='utf-8', index=False)
file_path.save()


print(data3)
