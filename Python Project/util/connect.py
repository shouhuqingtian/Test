# -*- coding:utf-8 -*-
import json

import MySQLdb.cursors


class OperationMysql:
    def __init__(self):
        self.conn = MySQLdb.Connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='le_study',
            charset='gbk',
            cursorclass=MySQLdb.cursors.DictCursor
        )
        self.cur = self.conn.cursor()

    # 查询一条数据
    def search_one(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        result = json.dumps(result)
        return result


if __name__ == '__main__':
    op_mysql = OperationMysql()
    print(op_mysql.search_one("SELECT * FROM web_user WHERE NAME = '刘大爷'"))

# cur.execute("SELECT * FROM web_user WHERE NAME = 'test'")
# print(cur.fetchone())
