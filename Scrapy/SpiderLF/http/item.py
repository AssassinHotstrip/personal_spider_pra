# coding:utf-8

class Item(object):
    """框架提供的item数据类, 用户解析响应体后获得的数据放在响应体中"""
    def __init__(self, data):
        # 解析的目标数据
        self._immutabledata = data

    @property
    def data(self):
        """通过接口提供外部访问,但不允许修改"""
        return self._immutabledata
