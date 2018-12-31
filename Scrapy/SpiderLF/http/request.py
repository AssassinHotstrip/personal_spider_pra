# coding:utf-8

class Request(object):
    """框架提供的 请求类, 用户导入此类构建请求对象"""

    def __init__(self, url, method="GET", headers=None, params=None, formdata=None, proxy=None):
        # 请求url地址
        self.url = url
        # 请求方法(默认GET)
        self.method = method
        # 请求报头
        self.headers = headers
        # 请求 查询字符
        self.params = params
        # 请求表单
        self.formdata = formdata
        # 请求的代理
        self.proxy = proxy
