# !/usr/bin/env python
# -*- coding:utf-8 -*-

'Functions to generate the relationship graph using networkx'

# Author: ericyang7816

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab


def graph_generate(star_relationships):
    '''Generate the relationship graph and show it.'''
    g = nx.Graph()  # 初始化关系图对象
    for star in star_relationships:
        for relate_figure in star_relationships[star]:
            g.add_edge(star, relate_figure[1])  # 遍历字典，建立关系
    nx.draw(g, with_labels=True, node_size=3600,
            font_size=20, node_color='#FFE4B5')
    plt.savefig('relation.png')
    plt.show(block=False)  # 保存并展示关系图
