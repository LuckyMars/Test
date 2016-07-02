import urllib.request
from urllib.error import HTTPError,URLError
import urllib查看网页源代码

from 煎蛋抓取 import 静态字符串


def OpenWebPageSource(UrlString,header):
    try:
        opener = urllib.request.build_opener()
        opener.addheaders = [header]
        html = opener.open(UrlString).read()
    except(HTTPError,URLError) as e:
        return None
    return html

def OpenArticleWebSource(ArticleUrl):
    htmlOne = urllib查看网页源代码.OpenWebPageSource(ArticleUrl, 静态字符串.Seting.header1)
    if htmlOne is None:
        htmlTwo = urllib查看网页源代码.OpenWebPageSource(ArticleUrl, 静态字符串.Seting.header2)
        if htmlTwo is None:
            return urllib查看网页源代码.OpenWebPageSource(ArticleUrl, 静态字符串.Seting.header3)
        else:
            return htmlTwo
    else:
        return htmlOne


