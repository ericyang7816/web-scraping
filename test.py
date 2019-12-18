# --coding:utf-8--

from urllib import parse
from urllib.request import urlopen
from bs4 import BeautifulSoup


star_relationships = {}
pages = []
maxtry =5
#name = input("请输入你要查询的明星")
#url = 'https://baike.baidu.com/item/'+parse.quote_plus(name)
def findstar(url):
    global pages
    global star_relationships
    global maxtry
    if maxtry == 0:
        return
    else:
        maxtry = maxtry -1
        star_dict = {}
        pages.append(url)#加入到总的pages列表
        html = urlopen(url)
        bsObj = BeautifulSoup(html,'lxml')
        starname = bsObj.find('dd',{"class":"lemmaWgt-lemmaTitle-title"}).h1.get_text()    # 明星的名字(str)
        starlist = bsObj.find("div",{"class":"viewport","id":"slider_relations"}).find_all("li")
        urllist = bsObj.find("div",{"class":"viewport","id":"slider_relations"}).find_all("a")
        for star in starlist:
            name = star.find("div",{"class":"name"}).em.get_text()#名字
            lenth1 = len(name)
            relationship = star.find("div",{"class":"name"}).get_text()#关系
            lenth2 = len(relationship)
            lenth = lenth2 - lenth1
            star_dict[relationship[0:lenth]] = name
        star_relationships[starname] = star_dict        # 将明星关系字典加入总字典
        for url in urllist:
            if "herf" in url.attrs:
                new_page = "https://baike.baidu.com"+url.attrs["herf"]
                if new_page not in pages:
                    pages.append(new_page)
                    findstar(new_page)
findstar("https://baike.baidu.com/item/%E6%98%86%E5%87%8C/1545451")
print(star_relationships)

#人物字典