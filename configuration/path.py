import os


# 项目的根路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取配置文件所在目录的路径
CONFIG_DIR = os.path.join(BASE_DIR, 'conf')

# 获取配置文件的路径
CONFIG_API_FILE_PATH = os.path.join(CONFIG_DIR, 'case.yaml')

# 获取日志文件所在目录的路径
LOGS_FILE_PATH = os.path.join(BASE_DIR, 'logs')

# 获取报告文件所在目录的路径
REPORTS_FILE_PATH = os.path.join(BASE_DIR, 'reports')

# 获取excel文件所在目录的路径
EXCEL_FILE_PATH = os.path.join(BASE_DIR, 'resources')

# 获取用户信息配置文件的路径
CONFIG_USER_ACCOUNT_FILE_PATH = os.path.join(CONFIG_DIR, 'users.yaml')

# 获取测试用例类所在的路径
CASES_DIR = os.path.join(BASE_DIR, 'test_set')

#
API_CASES_DIR = os.path.join(CASES_DIR, 'api_test')
