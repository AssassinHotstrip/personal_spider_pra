# coding:utf-8

# 导入队列
from six.moves.queue import Queue  # six 用于python2/3兼容

class Scheduler(object):

    def __init__(self):
        self.request_queue = Queue()
        self.fingerprint_set = set()  # 请求指纹,用于标记请求是否在队列中


    def add_request(self, request):
        """添加请求到队列"""
        # 判断请求是否已经在队列中:
        if self._filter_request(request):
            self.request_queue.put(request)
        self.fingerprint_set.add(request.url)


    def _filter_request(self, request):
        """过滤重复请求"""
        # 判断请求指纹是否已存在于指纹集合中,若在,返回False,进一步让请求不能加入队列
        if request.url in self.fingerprint_set:
            return False
        # 若不在,返回True,允许请求加入队列
        else:
            return True


    def get_request(self):
        """获取过滤后的请求"""
        # 返回一个不重复的请求给引擎,引擎交给下载器处理
        return self.request_queue.get()