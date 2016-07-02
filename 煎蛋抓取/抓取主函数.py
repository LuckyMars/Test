import 写入数据库
import 抓取文章页面
import 静态字符串

from 煎蛋抓取 import 首页文章标题链接图片抓取

MainData = 首页文章标题链接图片抓取.GetUrlPicTitle()
if MainData is not None:
    for divTag in MainData:
        exist = 写入数据库.QueryMySql\
            ('SELECT * from Article  WHERE Article.LinkUrl=\'' + divTag[1] +'\' LIMIT 1',
             静态字符串.Seting._ConnString)
        if(len(exist) is 0):
            PaTag = 抓取文章页面.GetArticleParagraph(divTag[1])
            写入数据库.InsertMainDetail(静态字符串.Seting.InserMainQS, divTag,
                                   静态字符串.Seting.InserDetailQS,
                                   PaTag, 静态字符串.Seting._ConnString)
        else:
            break



