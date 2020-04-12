import pymysql
import random
from configuration.config import configuration


class HandleMysql:
    def __init__(self):
        self.conn = pymysql.connect(host=configuration.getConfig('mysql', 'host'),  # mysql服务器IP或者域名
                                    user=configuration.getConfig('mysql', 'user'),  # 用户名
                                    password=configuration.getConfig('mysql', 'password'),  # 密码
                                    db=configuration.getConfig('mysql', 'db'),  # 连接的数据库名称
                                    port=configuration.getConfig('mysql', 'port'),  # 数据库的端口号，默认为3306
                                    charset='utf8',  # 数据库编码为utf8，不能写为utf-8
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
    @staticmethod
    def creat_mobile():
        # 随机生成11位手机号码
        return '133' + ''.join(random.sample('0123456789', 8))

    def is_exist_mobile(self, mobile):
        # 判断数据库是否存在已注册手机号
        sql = do_yaml.read_yaml('mysql','select_user_sql')
        if self.run(sql, args=[mobile]):
            return True
        else:
            return False

    def creat_no_existed_mobile(self):
        # 创建一个在数据库中未注册的手机号
        while True:
            one_mobile=self.creat_mobile()
            if not self.is_exist_mobile(one_mobile):
                break
        return one_mobile

    def creat_no_existed_user_id(self):
        # 创建一个不存在的id
        max_id_sql=do_yaml.read_yaml('mysql','select_maxuserid_sql')
        res_data=self.run(max_id_sql)
        no_existed_user_id=int(res_data[0]['MAX(id)'])+1
        return str(no_existed_user_id)
"""

if __name__ == '__main__':

    pass
