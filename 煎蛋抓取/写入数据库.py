import mysql.connector

def QueryMySql(QueryString,ConnString):
    try:
        conn = mysql.connector.connect(**ConnString)
        cursor = conn.cursor()
        cursor.execute(QueryString)
        # 取回的是列表，列表中包含元组
        print('查询成功+1...')
        return cursor.fetchall()
    except mysql.connector.Error as e:
        print('查询错误:{}'.format(e))
    finally:
        cursor.close;
        conn.close;

def InserOneMySql(QueryString,ConnString,Data):
    try:
        conn = mysql.connector.connect(**ConnString)
        cursor = conn.cursor()
        cursor.execute(QueryString,Data)
        conn.commit()
        print('单个插入成功+1...')
    except mysql.connector.Error as e:
        print('单个插入错误:{}'.format(e))
    finally:
        cursor.close
        conn.close

def InserManyMySql(QueryString,ConnString,Data):
    try:
        conn = mysql.connector.connect(**ConnString)
        cursor = conn.cursor()
        cursor.executemany(QueryString, Data)
        conn.commit()
        print('连续插入成功+1...')
    except mysql.connector.Error as e:
        print('连续插入出错:{}'.format(e))
    finally:
        cursor.close
        conn.close


def InsertMainDetail(MainQS,MainData,DetailQS,DetailData,ConnString):
    try:
        conn = mysql.connector.connect(**ConnString)
        cursor = conn.cursor()
        cursor.execute(MainQS, MainData)
        cursor.executemany(DetailQS, DetailData)
        conn.commit()
        print('文章数据插入成功+1...')
    except mysql.connector.Error as e:
        print('文章数据存储出错:{}'.format(e))
    finally:
        cursor.close
        conn.close





