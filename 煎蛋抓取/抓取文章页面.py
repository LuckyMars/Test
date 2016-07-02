#获取链接中文章的全部段落列表
from bs4 import BeautifulSoup

from 煎蛋抓取 import urllib查看网页源代码


def GetArticleParagraph(ArticleUrl):
    htmldata = urllib查看网页源代码.OpenArticleWebSource(ArticleUrl)
    if htmldata is not None:
        list = []
        soup = BeautifulSoup(htmldata, "html.parser")
        divTags = soup.find("div", attrs={"class": "post f"})
        h1Tag = divTags.find('h1').get_text()
        pTags = divTags.find_all('p')
        ContentTemp = ''
        for pItem in pTags:
            img = pItem.find('img')
            if img is not None:
                if (img.has_attr('data-original')):
                    ContentTemp = img['data-original']
            else:
                ContentTemp = pItem.get_text()
            # s = "({'Title': %s),('Content':%s),('Source':%s)})" % (h1Tag, ContentTemp, pItem)
            s = (str(h1Tag), str(ContentTemp), str(pItem))
            list.append(s)
        return list
