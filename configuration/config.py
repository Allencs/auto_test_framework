import yaml
from configuration.path import CONFIG_API_FILE_PATH

"""
The class to handle configuration files.
"""


class Configuration(object):

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, filename):
        with open(filename, encoding='utf-8') as one_file:
            self.data = yaml.full_load(one_file)
    pass

    def getConfig(self, section, option):
        return self.data[section][option]

    @staticmethod
    def setConfig(filename, data):
        with open(filename, 'w', encoding='utf-8') as file:
            yaml.dump(data, file, allow_unicode=True)


configuration = Configuration(CONFIG_API_FILE_PATH)





