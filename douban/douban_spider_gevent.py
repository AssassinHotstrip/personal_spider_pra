# coding:utf-8
try:
    from queue import Queue  # python3
except:
    from Queue import Queue  # python2
import time


import requests
from lxml import etree

# 协程
from gevent.pool import Pool
import gevent
from gevent.monkey import patch_all
patch_all()


class DoubanSpider(object):
    def __init__(self):
        self.full_url_list = ["https://movie.douban.com/top250?start=" + str(page) for page in range(0, 226, 25)]
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.queue = Queue()


    def send_request(self, url):
        print("[INFO] Requesting...:{}".format(url))
        response = requests.get(url, headers=self.headers)
        time.sleep(1)  # 模拟网络阻塞
        return response


    def parse_response(self, response):
        html = response.content
        html_obj = etree.HTML(html)
        movie_list = html_obj.xpath("//div[@class='info']")
        print(movie_list)
        for movie in movie_list:
            movie_name = movie.xpath(".//span[@class='title'][1]/text()")[0]
            self.queue.put(movie_name)


    def save_data(self):
        pass

    def main(self):


        ### 1. gevent 协程模块的常规用法
        # job_list = []
        # for url in self.full_url_list:
        #     # 构建协程任务
        #     job = gevent.spawn(self.send_request, url)
        #     job_list.append(job)
        #
        # g_list = gevent.joinall(job_list)
        #
        # for g in g_list:
        #     self.parse_response(g.get())

        #### 2. gevent.pool的协程池用法
        # dis = [self.parse_response(g.get()) for g in gevent.joinall([gevent.spawn(self.send_request, url) for url in self.full_url_list])]

        pool = Pool(10)
        # pool.map()
        # pool.map_async()
        # pool.apply()
        for url in self.full_url_list:
            pool.apply_async(self.send_request, [url], callback=self.parse_response)

        # pool.close()  # 协程池不用close
        pool.join()


        while not self.queue.empty():
            print(self.queue.get())


if __name__ == '__main__':
    spider = DoubanSpider()
    start = time.time()
    spider.main()
    end = time.time()

    print("[INFO] : using time {}".format(end - start))