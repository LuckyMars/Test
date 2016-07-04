from bs4 import BeautifulSoup
import urllib查看网页源代码
import 静态字符串

def GetUrlPicTitle():
    data = urllib查看网页源代码.OpenArticleWebSource(静态字符串.Seting.jandanurl)
    if(data is not None):
        soup = BeautifulSoup(data, "html.parser")
        DivTags = soup.find_all("div", attrs={"class": "post f list-post"})
        divLen = len(DivTags)
        list = []
        for link in range(0,divLen):
            aTags = DivTags[link].find_all("a", limit=2)
            hrefTemp = aTags[0]['href']
            textTemp = aTags[1].text
            im = DivTags[link].find("img")
            imTemp = ''
            if (im.has_attr('data-original')):
                imTemp = im['data-original']
            if (im.has_attr('src')):
                imTemp = im['src']
            # s = "({'Title': %s),('SourceUrl':%s),('Pic':%s)})" % (textTemp, hrefTemp, imTemp)
            s = (textTemp, hrefTemp, imTemp)
            list.append(s)
        return list
