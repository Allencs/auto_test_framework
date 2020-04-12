import os
import unittest
from datetime import datetime
from auto_test.auto_test import AutoTest, CreateTest
from configuration.config import configuration
from configuration.path import REPORTS_FILE_PATH, CASES_DIR
from libs.HTMLTestRunnerNew import HTMLTestRunner


class UITest(AutoTest):
    def __init__(self, cases_dir=None, report_name=None):
        super().__init__()
        if cases_dir is not None:
            self.cases_dir = cases_dir
        else:
            self.cases_dir = CASES_DIR
        if report_name is not None:
            r_name = report_name + '.html'
            self.report_name = os.path.join(REPORTS_FILE_PATH, r_name)
        else:
            r_name = configuration.getConfig('report', 'name') + '_' + \
                     datetime.strftime(datetime.now(), '%Y%m%d%H%M%S') + '.html'
            self.report_name = os.path.join(REPORTS_FILE_PATH, r_name)

    def run(self):
        suite = unittest.defaultTestLoader.discover(self.cases_dir)
        runner = HTMLTestRunner(stream=open(self.report_name, 'wb'),
                                verbosity=2,
                                title=configuration.getConfig('report', 'title'),
                                description=configuration.getConfig('report', 'description'),
                                tester=configuration.getConfig('report', 'tester'))
        runner.run(suite)


class CreateUITest(CreateTest):
    def create(self, *args, **kwargs):
        concrete_test = UITest(*args, **kwargs)
        return concrete_test


