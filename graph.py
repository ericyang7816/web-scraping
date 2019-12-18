# !/usr/bin/env python
# -*- coding:utf-8 -*-

'graph generation'

# Author:EricYang

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab
import main

g=nx.Graph()
for star in main.star_relationships:
    for relate_figure in main.star_relationships[star].values():
        g.add_edge(star,relate_figure)
nx.draw(g,with_labels=True,node_size=3600,font_size=20,node_color='#FFE4B5')
#nx.draw(g,pos=nx.spring_layout(g))
plt.show()