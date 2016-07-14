# 想写一个能找到页面中文章段落的脚本
from urllib.error import HTTPError,URLError
import urllib.request
from bs4 import BeautifulSoup

def OpenWebPageSource(UrlString):
    try:
        opener = urllib.request.build_opener()
        html = opener.open(UrlString).read()
    except(HTTPError,URLError) as e:
        return None
    return html

html = OpenWebPageSource("https://cosmosmagazine.com/geoscience/scientists-warn-of-bangladesh-earthquake-time-bomb")
if html is not None:
    soup = BeautifulSoup(html, "html.parser")
    PTags = soup.find_all("p")
    for Pitem in PTags:
        print(Pitem)
        #这样找到了全部的段落，但是有些段落是我不需要的，能否将这些段落排除?
        # 我觉得短时间能排除指定段落或者说自动判断哪些段落是文章的，有些不现实
        #先获取全部段落，手动筛选文章段落，后期熟悉了Python后在处理自动判断的实现