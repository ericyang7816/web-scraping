# !/usr/bin/env python
# -*- coding:utf-8 -*-

'main scrap program'

# Author: ericyang7816 pigxx500kg jbqiangqiangqiang

from urllib import parse
from urllib.request import urlopen
from bs4 import BeautifulSoup

import graph
import search

star_relationships = {}  # 人物的关系
pages = []  # 查询的页面
MAX_TRY = 8  # 查询深度，会遍历 MAX_TRY-1 个人物


name = input("请输入你要查询的明星：")
url = 'https://baike.baidu.com/item/'+parse.quote_plus(name)  # 将中文名进行转义


def find_star(url):
    global pages
    global star_relationships
    global MAX_TRY
    if MAX_TRY == 0:
        return
    else:
        star_relation_list = []  # 明星关系总列表
        pages.append(url)  # 加入到总的pages列表
        try:
            html = urlopen(url)
        except Exception:
            return
        bsObj = BeautifulSoup(html, 'html.parser')
        try:
            star_name = bsObj.find(
                'dd', {"class": "lemmaWgt-lemmaTitle-title"}).h1.get_text()    # 查找明星的名字
            star_location = bsObj.find(
                "div", {"class": "viewport", "id": "slider_relations"})
        except Exception:
            return
        if star_location is not None:
            star_list = star_location.find_all("li")
        else:
            return  # 如果当前人物不存在关系，就返回继续查找
        MAX_TRY = MAX_TRY - 1
        star_list = bsObj.find(
            "div", {"class": "viewport", "id": "slider_relations"}).find_all("li")
        url_list = bsObj.find(
            "div", {"class": "viewport", "id": "slider_relations"}).find_all("a")
        for star in star_list:
            name = star.find("div", {"class": "name"}).em.get_text()  # 获取姓名
            lenth1 = len(name)
            relationship = star.find(
                "div", {"class": "name"}).get_text()  # 返回关系和姓名的组合
            lenth2 = len(relationship)
            lenth = lenth2 - lenth1
            one_relation = [relationship[0:lenth], name]  # 利用切片将关系提取
            star_relation_list.append(one_relation)
        star_relationships[star_name] = star_relation_list  # 将明星关系列表加入总字典
        for url in url_list:
            if "href" in url.attrs:
                # 如果是内链，则添加前缀后添加
                if "baike.baidu.com" not in url.attrs["href"]:
                    new_page = "https://baike.baidu.com"+url.attrs["href"]
                else:  # 如果是外链，则直接添加
                    new_page = url.attrs["href"]
                if new_page not in pages:
                    pages.append(new_page)
                    find_star(new_page)


find_star(url)
if star_relationships:  # 当查找到人物关系时，向下执行
    graph.graph_generate(star_relationships)  # 生成关系图
    while True:
        name = input('请输入要查询的人物: ')
        print()
        # 如果遍历过要查询的人物的关系，就返回TA的关系，并且以其他人为中心查找与TA的关系
        # 否则只返回以其他人为中心与TA的关系
        if name in star_relationships.keys():
            search.center_search(name, star_relationships)
        else:
            search.non_center_search(name, star_relationships)
else:
    print('未找到人物关系...')
