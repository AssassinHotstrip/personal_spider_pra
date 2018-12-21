try:
    from queue import Queue  # python3
except:
    from Queue import Queue  # python2
import time
from threading import Thread

import requests
from lxml import etree


class DoubanSpider(object):
    def __init__(self):
        self.full_url_list = ["https://movie.douban.com/top250?start=" + str(page) for page in range(0, 226, 25)]
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.queue = Queue()


    def send_request(self, url):
        print("[INFO] Requesting...:{}".format(url))
        response = requests.get(url, headers=self.headers)
        time.sleep(1)  # 模拟网络阻塞
        # return response
        self.parse_response(response)  # 直接在此处将response传给parse_response

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
        # for url in self.full_url_list:
        #     response = self.send_request(url)
        #     self.parse_response(response)

        # 多线程方式
        thread_list = []
        for url in self.full_url_list:
            # 构建一个线程对象来发送请求
            thread = Thread(target=self.send_request, args=[url])
            thread.start()
            thread_list.append(thread)

        # 让主线程阻塞,等待所有子线程结束后才结束
        for thread in thread_list:
            thread.join()

        while not self.queue.empty():

            print(self.queue.get())


if __name__ == '__main__':
    spider = DoubanSpider()
    start = time.time()
    spider.main()
    end = time.time()

    print("[INFO] : using time {}".format(end - start))






# 重写Thread方法 来实现多线程(还存在问题)
# try:
#     from queue import Queue  # python3
# except:
#     from Queue import Queue  # python2
# import time
# from threading import Thread
#
# import requests
# from lxml import etree
#
#
#
# class SendThread(Thread):
#     """ 自定义线程类实现 """
#     def __init__(self, target, args=[]):
#         #Thread.__init__()
#         super(SendThread, self).__init__()
#
#         self.target = target
#         self.args = args
#         self.response = None
#
#     def run(self):
#         self.response = self.target(self.args[0])
#         #print(len(self.response.content))
#         #self.get_response(response)
#         #self.send_request(url)
#
#     def get_response(self):
#         return self.response
#
#
# class DoubanSpider(object):
#     def __init__(self):
#         self.full_url_list = ["https://movie.douban.com/top250?start=" + str(page) for page in range(0, 226, 25)]
#         self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
#         self.queue = Queue()
#
#
#     def send_request(self, url):
#         print("[INFO] Requesting...:{}".format(url))
#         response = requests.get(url, headers=self.headers)
#         time.sleep(1)  # 模拟网络阻塞
#         return response
#
#
#     def parse_response(self, response):
#         html = response.content
#         html_obj = etree.HTML(html)
#         movie_list = html_obj.xpath("//div[@class='info']")
#         print(movie_list)
#         for movie in movie_list:
#             movie_name = movie.xpath(".//span[@class='title'][1]/text()")[0]
#             self.queue.put(movie_name)
#
#
#     def save_data(self):
#         pass
#
#     def main(self):
#
#         thread_list = []
#         for url in self.full_url_list:
#             # 构建一个线程对象来发送请求
#             thread = SendThread(target=self.send_request, args=[url])
#             thread.start()
#             response = thread.get_response()
#             self.parse_response(response)
#             thread_list.append(thread)
#
#         # 让主线程阻塞,等待所有子线程结束后才结束
#         for thread in thread_list:
#             thread.join()
#
#         while not self.queue.empty():
#             print(self.queue.get())
#
#
# if __name__ == '__main__':
#     spider = DoubanSpider()
#     start = time.time()
#     spider.main()
#     end = time.time()
#
#     print("[INFO] : using time {}".format(end - start))