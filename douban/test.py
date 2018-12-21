
try:
    from queue import Queue
except:
    from Queue import Queue
import time
#from threading import Thread
# 多进程模块里的多线程子模块里的线程池
#from multiprocessing.dummy import Pool


import requests
from lxml import etree

# 导入协程gevent模块
import gevent
# 执行猴子补丁，让网络库可以异步执行网络IO任务

# 创建协程池
from gevent.pool import Pool

from gevent.monkey import patch_all
patch_all()


class DoubanSpider(object):
    def __init__(self):
        self.url_list = ["https://movie.douban.com/top250?start=" + str(page) for page in range(0, 226, 25)]
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

        self.queue = Queue()


    def send_request(self, url):
        print("[INFO] send request : {}".format(url))
        response = requests.get(url, headers=self.headers)
        time.sleep(1)
        return response



    def parse_response(self, response):
    #def parse_response(self, response_list):
        #for response in response_list:
        html = response.content
        html_obj = etree.HTML(html)

        node_list = html_obj.xpath("//div[@class='info']")

        for node in node_list:
            title = node.xpath(".//span[@class='title'][1]/text()")[0]

            self.queue.put(title)

    # def save_data(self):
    #     pass

    def main(self):
        # for url in self.url_list:
        #     response = self.send_request(url)
        #     self.parse_response(response)


        #### 1. gevent 协程模块的常规用法
        # job_list = []
        # for url in self.url_list:
        #     # 构建协程任务
        #     job = gevent.spawn(self.send_request, url)
        #     job_list.append(job)

        # g_list = gevent.joinall(job_list)

        # for g in g_list:
        #     self.parse_response(g.get())

        #### 2. gevent.pool的协程池用法
        #_ = [self.parse_response(g.get()) for g in gevent.joinall([gevent.spawn(self.send_request, url) for url in self.url_list])]


        pool = Pool(10)

        # pool.map()
        # pool.map_async()
        # pool.apply()
        for url in self.url_list:
            pool.apply_async(self.send_request, [url], callback=self.parse_response)

        #pool.close()
        pool.join()



        while not self.queue.empty():
            print(self.queue.get())

        print("[INFO]: over.")




if __name__ == '__main__':
    spider = DoubanSpider()
    start = time.time()
    spider.main()
    end = time.time()

    # 12.900727987289429
    print("[INFO] : using time {}".format(end - start))
