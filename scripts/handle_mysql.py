import pymysql
from configuration.config import configuration


'''
if need data from database
'''


class HandleMysql:
    def __init__(self):
        self.conn = pymysql.connect(host=configuration.getConfig('mysql', 'host'),
                                    user=configuration.getConfig('mysql', 'user'),
                                    password=configuration.getConfig('mysql', 'password'),
                                    db=configuration.getConfig('mysql', 'db'),
                                    port=configuration.getConfig('mysql', 'port'),
                                    charset='utf8',
                                    cursorclass=pymysql.cursors.DictCursor  # 让返回结果为字典类型
                                    )
        self.cursor = self.conn.cursor()

    def run(self, sql, args=None, is_more=True):
        self.cursor.execute(sql, args)
        self.conn.commit()
        if is_more:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()


"""
    do something in database
"""

if __name__ == '__main__':

    pass
