import json
import requests


class HandleRequest(object):

    def __init__(self):
        self.one_session = requests.Session()

    def add_headers(self, headers):
        """添加公共请求头"""
        self.one_session.headers.update(headers)

    def send(self, url, method='post', data=None, is_json=True, **kwargs):
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except Exception as e:
                print('使用日志器来记录日志')
                data = eval(data)

        method = method.lower()
        if method == 'get':
            res = self.one_session.request(method, url, params=data, **kwargs)
        elif method in ('post', 'delete', 'put', 'patch'):
            if is_json:
                res = self.one_session.request(method, url, json=data, **kwargs)
            else:
                res = self.one_session.request(method, url, data=data, **kwargs)
        else:
            res = None
            print('不支持{}请求方法'.format(method))

        return res

    def close(self):
        self.one_session.close()


if __name__ == '__main__':
    pass

