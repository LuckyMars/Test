class Seting():
    header1 = ('User-Agent',
               'Mozilla/5.0 (Windows NT 7) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    header2 = ('User-Agent',
               'Mozilla/5.0 (Windows NT 8) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    header3 = ('User-Agent',
               'Mozilla/5.0 (Windows NT 10) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    jandanurl = "http://www.jandan.net/"

    _ConnString = {
        'host': '116.251.219.27',
        'port': '3306',
        'user': 'python',
        'password': 'lipasswd',
        'database': 'jandan'}


    InserMainQS = 'INSERT into Article(title,linkurl,picurl) values(%s,%s,%s)'

    InserDetailQS = 'INSERT INTO Paragraph(Title,Content,Source) VALUES(%s,%s,%s)'