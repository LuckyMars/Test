#在数据库中找到对应的译文来源网页
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