import os
import sys
import unittest
from datetime import datetime
from auto_test.auto_test import AutoTest, CreateTest
from configuration.config import configuration
from configuration.path import REPORTS_FILE_PATH, API_CASES_DIR
from libs.HTMLTestRunnerNew import HTMLTestRunner


class APITest(AutoTest):
    """
    Concrete API test class
    """
    def __init__(self, cases_dir=None, cases=None, report_name=None):
        super().__init__()
        if cases_dir is not None:
            self.cases_dir = cases_dir
        else:
            self.cases_dir = API_CASES_DIR
        if report_name is not None:
            r_name = report_name + '.html'
            self.report_name = os.path.join(REPORTS_FILE_PATH, r_name)
        else:
            r_name = configuration.getConfig('report', 'name') + '_' + \
                             datetime.strftime(datetime.now(), '%Y%m%d%H%M%S') + '.html'
            self.report_name = os.path.join(REPORTS_FILE_PATH, r_name)
        if cases is not None:
            self.cases = cases

    def run(self):
        if self.cases is None:
            suite = unittest.defaultTestLoader.discover(self.cases_dir)
        else:
            sys.path.append(self.cases_dir)
            suite = unittest.TestLoader().loadTestsFromNames(self.cases)
        runner = HTMLTestRunner(stream=open(self.report_name, 'wb'),
                                verbosity=2,
                                title=configuration.getConfig('report', 'title'),
                                description=configuration.getConfig('report', 'description'),
                                tester=configuration.getConfig('report', 'tester'))
        runner.run(suite)


class CreateAPITest(CreateTest):
    """
    Concrete factory for creating concrete api test
    """
    def create(self, *args, **kwargs):
        concrete_test = APITest(*args, **kwargs)
        return concrete_test
