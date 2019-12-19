# !/usr/bin/env python
# -*- coding:utf-8 -*-

'read program'

# Author:


def read_one_star(name,star_relationships):
    if name not in star_relationships.keys():
        return 0
    print(name+"的关系表：")
    relationships=star_relationships[name]
    for relationship in relationships:
        print(relationship,":",relationships[relationship])


    


