import re
from configuration.path import CONFIG_USER_ACCOUNT_FILE_PATH
from configuration.config import Configuration


class HandleParameterize:
    """
    参数化类
    """
    invested_user_pwd_pattern = r'{invest_user_pwd}'
    invested_user_id_pattern = r'{invest_user_id}'

    configuration = Configuration(CONFIG_USER_ACCOUNT_FILE_PATH)

    @classmethod
    def do_param(cls, data):

        # 替换密码
        if re.search(cls.invested_user_pwd_pattern, data):
            data = re.sub(cls.invested_user_pwd_pattern, cls.configuration.getConfig('Invest', 'pwd'), data)

        # 替换id
        if re.search(cls.invested_user_id_pattern, data):
            data = re.sub(cls.invested_user_id_pattern, str(cls.configuration.getConfig('Invest', 'id')), data)

        return data


if __name__ == '__main__':
    '''
    EXAMPLE
    one_str = '{"mobile_phone":"13345588812","pwd":"{invest_user_pwd}","type":1,"reg_name":"sunny"}'
    print(HandleParameterize.do_param(one_str))
    '''
    pass

