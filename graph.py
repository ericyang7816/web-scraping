# !/usr/bin/env python
# -*- coding:utf-8 -*-

'relationship graph generation using networkx'

# Author:ericyang

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab


def graph_generate(star_relationships):
    g=nx.Graph()
    for star in star_relationships:
        for relate_figure in star_relationships[star]:
            g.add_edge(star,relate_figure[1])
    nx.draw(g,with_labels=True,node_size=3600,font_size=20,node_color='#FFE4B5')
    plt.show()