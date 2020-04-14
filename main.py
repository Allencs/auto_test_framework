from api_test.api_test import CreateAPITest
from ui_test.ui_test import CreateUITest


class CreateClient(object):
    """
    This is a test creator client for you to create concrete test according to the type of test.
    """

    def __init__(self):
        pass

    @staticmethod
    def createTest(test_type, cases_dir=None, cases=None, report_name=None):
        """
        Create concrete test instance
        :param test_type: test type such as api_test or ui_test
        :param cases_dir: if None, default dir which defined in yaml will be used and all cases will be executed
        :param cases: specific cases list
        :param report_name: define your own report name
        :return: None
        """
        if test_type == "api":
            client = CreateAPITest()
            concrete_test = client.create(cases_dir, cases, report_name="report_demo")
            return concrete_test
        elif test_type == "ui":
            client = CreateUITest()
            concrete_test = client.create(cases_dir, report_name)
            return concrete_test


"""""""""""""""""""""""""""""""""""""""""""""""
Use the specific cases [cases -> list]
--------------------------------------
Illustration:
test_sub   ->   Module
SubCase    ->   unittest.TestCase
test_add_1 ->   case from unittest.TestCase
--------------------------------------
# example 1
# cases = ['test_sub','test_add']

# example 2
cases = ['test_sub.SubCase', 'test_add.AddCase.test_add_1']

# example 3
# cases = ['test_sub.SubCase.test_sub_1','test_add.AddCase.test_add_1']
"""""""""""""""""""""""""""""""""""""""""""""""


if __name__ == '__main__':
    test_client = CreateClient()
    test = test_client.createTest("api", cases=["test_01_token"])
    test.run()
    pass






