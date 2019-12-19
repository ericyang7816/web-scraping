# !/usr/bin/env python
# -*- coding:utf-8 -*-

'search function supplement'

# Author:jbqiangqiangqiang

import main

def non_star_search(name):
    for star in main.star_relationships:
        star_relationship=star_relationships[star]
        if name in star_relationship.values():
            relationship=list(a.keys())[list(a.values()).index(name)]
            print(name,"是",star,"的",relationship)


