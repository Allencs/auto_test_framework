import logging
import os
from configuration.config import configuration
from configuration.path import LOGS_FILE_PATH


class HandleLog(object):

    @staticmethod
    def creat_logger():
        # 创建一个日志收集器
        my_log = logging.getLogger(configuration.getConfig('log', 'logger_name'))

        # 设置日志收集器的等级
        my_log.setLevel(configuration.getConfig('log', 'log_level'))

        # 设置日志输出格式
        formatter = logging.Formatter(configuration.getConfig('log', 'formatter'))

        # 日志的输出
        # 创建一个输出到控制台的数据流
        sh = logging.StreamHandler()
        sh.setLevel(configuration.getConfig('log', 'output_level'))
        # 设置输出到控制台的日志格式
        sh.setFormatter(formatter)
        # 将输出渠道加入到日志收集器中
        my_log.addHandler(sh)

        # 创建一个输出到文件的日志数据流
        fh = logging.FileHandler(os.path.join(LOGS_FILE_PATH, configuration.getConfig('log', 'filelog_name')),
                                 encoding='utf-8')
        fh.setLevel(configuration.getConfig('log', 'file_level'))
        # 设置输出到文件的日志格式
        fh.setFormatter(formatter)
        my_log.addHandler(fh)

        return my_log


log = HandleLog.creat_logger()

# if __name__ == '__main__':
#     log = MyLogger.creat_logger()
#     log.info('这是我封装的日志模块')
