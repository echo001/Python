def export_excel(doc):
    pf = pd.DataFrame(doc)
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
