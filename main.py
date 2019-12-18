# !/usr/bin/env python
# -*- coding:utf-8 -*-

'main scrap program'

# Author: ericyang pigxx500kg jbqiangqiangqiang

from urllib import parse
from urllib.request import urlopen
from bs4 import BeautifulSoup


star_relationships = {}
pages = []
MAX_TRY = 5

name = input("请输入你要查询的明星：")
url = 'https://baike.baidu.com/item/'+parse.quote_plus(name)


def find_star(url):
    global pages
    global star_relationships
    global MAX_TRY
    if MAX_TRY == 0:
        return
    else:
        star_dict = {}
        pages.append(url)  # 加入到总的pages列表
        html = urlopen(url)
        bsObj = BeautifulSoup(html, 'lxml')
        star_name = bsObj.find(
            'dd', {"class": "lemmaWgt-lemmaTitle-title"}).h1.get_text()    # 明星的名字(str)
        try:
            star_list = bsObj.find(
                "div", {"class": "viewport", "id": "slider_relations"}).find_all("li")
        except Exception:
            return
        else:
            MAX_TRY = MAX_TRY - 1
        star_list = bsObj.find(
            "div", {"class": "viewport", "id": "slider_relations"}).find_all("li")
        url_list = bsObj.find(
            "div", {"class": "viewport", "id": "slider_relations"}).find_all("a")
        for star in star_list:
            name = star.find("div", {"class": "name"}).em.get_text()  # 名字
            lenth1 = len(name)
            relationship = star.find("div", {"class": "name"}).get_text()  # 关系
            lenth2 = len(relationship)
            lenth = lenth2 - lenth1
            star_dict[relationship[0:lenth]] = name
        star_relationships[star_name] = star_dict        # 将明星关系字典加入总字典
        for url in url_list:
            if "href" in url.attrs:
                new_page = "https://baike.baidu.com"+url.attrs["href"]
                if new_page not in pages:
                    pages.append(new_page)
                    find_star(new_page)


find_star(url)
print(star_relationships)
