# !/usr/bin/env python
# -*- coding:utf-8 -*-

'search function supplement'

# Author:jbqiangqiangqiang

def non_star_search(name,star_relationships):
    for star in star_relationships:
        star_relationship=star_relationships[star]
        for relationship in star_relationship:
            if name==relationship[1]:
                print("{}是{}的{}".format(name,star,relationship[0]))


