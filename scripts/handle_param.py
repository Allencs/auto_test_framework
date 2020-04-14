import re
from configuration.path import CONFIG_USER_ACCOUNT_FILE_PATH
from scripts.handle_mysql import HandleMysql
from configuration.config import Configuration


class HandleParameterize:
    """
    参数化类
    """
    not_existed_mobile_pattern = r'{not_existed_tel}'
    invested_user_mobile_pattern = r'{invest_user_tel}'
    invested_user_pwd_pattern = r'{invest_user_pwd}'
    invested_user_id_pattern = r'{invest_user_id}'
    no_exsited_user_id_pattern = r'{no_exsited_invest_user_id}'

    configuration = Configuration(CONFIG_USER_ACCOUNT_FILE_PATH)

    @classmethod
    def do_param(cls, data):
        # 替换未注册的手机号
        if re.search(cls.not_existed_mobile_pattern, data):
            do_mysql = HandleMysql()
            data = re.sub(cls.not_existed_mobile_pattern, do_mysql.creat_no_existed_mobile(), data)
            do_mysql.close()

        # 替换投资人手机号
        if re.search(cls.invested_user_mobile_pattern, data):
            data=re.sub(cls.invested_user_mobile_pattern, cls.configuration.getConfig('Invest', 'mobile_phone'), data)

        # 替换投资人密码
        if re.search(cls.invested_user_pwd_pattern, data):
            data = re.sub(cls.invested_user_pwd_pattern, cls.configuration.getConfig('Invest', 'pwd'), data)

        # 替换投资人id
        if re.search(cls.invested_user_id_pattern, data):
            data = re.sub(cls.invested_user_id_pattern, str(cls.configuration.getConfig('Invest','id')), data)

        # 替换未存在的用户id
        if re.search(cls.no_exsited_user_id_pattern, data):
            domysql = HandleMysql()
            data = re.sub(cls.no_exsited_user_id_pattern, domysql.creat_no_existed_user_id(), data)
            domysql.close()

        return data


if __name__ == '__main__':
    one_str = '{"mobile_phone":"{not_existed_mobile}","pwd":"12345678","type":1,"reg_name":"sunny"}'
    two_str = '{"mobile_phone":{invest_user_tel},"pwd":{invest_user_pwd}}'
    print(HandleParameterize.do_param(one_str))
    print(HandleParameterize.do_param(two_str))


