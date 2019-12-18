# !/usr/bin/env python
# -*- coding:utf-8 -*-

'read program'

# Author:

star_relationships = {'李小龙': {'妻子': '琳达·埃莫瑞', '女儿': '李香凝', '儿子': '李国豪', '父亲': '李海泉', '母亲': '何爱瑜', '哥哥': '李忠琛', '弟弟': '李振辉', '爷爷': '李震彪', '搭档': '仓田保昭'}}

def read_one_star(s_r,name):
    if name not in s_r.keys():
        return 0
    print(name+"的关系表：")
    relationships=star_relationships[name]
    for relationship in relationships:
        print(relationship,":",relationships[relationship])


read_one_star(star_relationships,"李小龙")  
    


