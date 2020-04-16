import unittest
from scripts.handle_log import log
from configuration.config import configuration
from scripts.handle_excel import HandleExcel
from scripts.handle_request import HandleRequest
from libs.ddt import ddt, data


@ddt
class TestTokenCase(unittest.TestCase):
    """
    Create a test-case class
    """
    # 读取 Excel测试案例文件内容
    do_excel = HandleExcel(sheetname="token", filename=None)
    cases = do_excel.read_data_to_obj()

    # 在测试案例执行之前，需要执行的操作：将版本号添加到公共请求头
    @classmethod
    def setUpClass(cls):
        cls.do_request = HandleRequest()
        cls.do_request.add_headers(configuration.getConfig('api', 'version'))

    # 在测试案例执行之后，需要执行的操作：关闭请求
    @classmethod
    def tearDownClass(cls):
        cls.do_request.close()

    @data(*cases)
    def test_token(self, case):
        # 1.将测试用例中的参数参数化
        # new_data = HandleParameterize.do_param(case.data)

        # 2.拼接url
        url = configuration.getConfig('api', 'prefix') + case.url

        # 3.向服务器发起请求
        new_request = self.do_request.send(url=url,
                                           method=case.method,
                                           data=case.data,
                                           is_json=False
                                           )

        # 4.将响应报文里的数据转化为字典格式
        # actual_result = new_request.json()
        actual_result = new_request.status_code
        # 获取预期的结果,将预期结果转化为字典
        # expected = json.loads(case.expected, encoding='utf-8')
        # expected_code = expected['code']
        # expected_msg = expected['msg']
        expected_code = case.expected
        # 获取title
        title = case.title

        # 获取执行成功的提示信息
        success_msg = configuration.getConfig('msg', 'success_result')

        # 获取执行失败的提示信息
        failed_msg = configuration.getConfig('msg', 'fail_result')

        # 获取行号
        row = case.case_id + 1

        # 5.断言，预期结果与实际结果做对比
        try:
            # self.assertEqual(expected_code, actual_result['code'], msg=title)
            # self.assertEqual(expected_msg, actual_result['msg'], msg=title)
            self.assertEqual(expected_code, actual_result, msg=title)
        except AssertionError as e:
            # 将实际值写入到actual_rol列
            self.do_excel.write_to_file(row=row, column=configuration.getConfig('excel', 'actuall_col'),
                                        value=new_request.text)
            # 将实际值写入到result_col列
            self.do_excel.write_to_file(row=row, column=configuration.getConfig('excel', 'result_col'),
                                        value=failed_msg)
            log.error(f'{title}，执行的结果为：{failed_msg}\n具体异常为：{e}')
            raise e
        else:
            # 将实际值写入到actual_rol列
            self.do_excel.write_to_file(row=row, column=configuration.getConfig('excel', 'actuall_col'),
                                        value=actual_result)
            # 将实际结论写入到result_col列
            self.do_excel.write_to_file(row=row, column=configuration.getConfig('excel', 'result_col'),
                                        value=success_msg)
            log.info(f'{title}，执行的结果为：{success_msg}')
