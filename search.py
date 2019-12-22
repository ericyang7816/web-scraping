# !/usr/bin/env python
# -*- coding:utf-8 -*-

'Functions to find the relationship between figures.'

# Author: jbqiangqiangqiang liuwx1015 ericyang7816


def non_center_search(name, star_relationships):
    '''Show the relationships of a person who is not the center of a relationship.'''
    tag = 0
    print(name+"的关系情况：")
    print('----------------')
    for star in star_relationships:
        star_relationship = star_relationships[star]
        for relationship in star_relationship:
            if name == relationship[1]:  # 使用format格式化字符串方便输出
                print("{}是{}的{}".format(name, star, relationship[0])) 
                tag = 1
    if not tag:
        print("Error: 查无此人")
    print('----------------')
    print('\n')
    


def center_search(name, star_relationships):
    '''Show the relationships of a person who is the center of a relationship.'''
    if name not in star_relationships.keys():
        return 0
    print(name+"的关系情况：")
    print('----------------')
    relationships = star_relationships[name]
    new_dic = {}
    for relationship_and_name in relationships:
        relationship = relationship_and_name[0]
        name_list = [relationship_and_name[1]]  # 将姓名存储到列表中
        if relationship in new_dic.keys():  # 当关系已存在时，将已存在的人加入到列表中
            exist_name_list = new_dic[relationship]
            name_list = exist_name_list+name_list
        new_dic[relationship] = name_list

    for one_name in star_relationships.keys():               #将对与其相关的所有关系进行查找，对new_dic进行关系的补充
        one_relationships=star_relationships[one_name]
        for one_relationship in one_relationships.keys():
            if one_relationships[one_relationship]==name:    #确认与查找的人是否相关
                if one_relationship not in new_dic.keys():   #如果关系不存在，则添加
                    new_dic[one_relationship]=[one_name]
                if one_name not in new_dic[one_relationship]:#如果仁为添加进关系，则添加
                    new_dic[one_relationship]+=[one_name] 


    for relationship in new_dic:
        print(relationship+": ", end="")
        for s_name in new_dic[relationship]:
            print(s_name+" ", end="")
        print()
    print('----------------')
    print('\n')
