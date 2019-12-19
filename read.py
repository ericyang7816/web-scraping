# !/usr/bin/env python
# -*- coding:utf-8 -*-

'read program'

# Author:lwx1015


def read_one_star(name,star_relationships):
    if name not in star_relationships.keys():
        return 0
    print(name+"的关系情况：")
    print('----------------')
    relationships=star_relationships[name]
    new_dic={}
    for relationship_and_name in relationships:
        relationship=relationship_and_name[0]
        name_list=[relationship_and_name[1]]   #名字默认用列表存储
        if relationship in new_dic.keys():    #当关系已存在时，将已存在的人
            exist_name_list=new_dic[relationship]
            name_list=exist_name_list+name_list
        new_dic[relationship]=name_list
    for relationship in new_dic:
        print(relationship+": ",end="")
        for s_name in new_dic[relationship]:
            print(s_name+" ",end="")
        print()
    print('----------------')


