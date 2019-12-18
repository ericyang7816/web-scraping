# !/usr/bin/env python
# -*- coding:utf-8 -*-

'graph generation'

# Author:EricYang

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab

g=nx.Graph()
g.add_edge('张三','李四')
g.add_edge('李四','王五')
g.add_edge('张三','王五')
nx.draw(g,with_labels=True,node_size=1000,font_size=20,node_color='#FFFFFF')
plt.show()