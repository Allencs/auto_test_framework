from api_test.api_test import CreateAPITest
from ui_test.ui_test import CreateUITest


class CreateClient(object):
    """
    This is a test creator client for you to create concrete test according to the type of test.
    """

    def __init__(self):
        pass

    @staticmethod
    def createTest(test_type):
        if test_type == "api":
            client = CreateAPITest()
            concrete_test = client.create(cases_dir=None, report_name="MyReport")
            return concrete_test
        elif test_type == "ui":
            client = CreateUITest()
            concrete_test = client.create(cases_dir=None, report_name=None)
            return concrete_test


if __name__ == '__main__':
    test_client = CreateClient()
    test = test_client.createTest("api")
    test.run()
    pass






