try:
    from queue import Queue  # python3
except:
    from Queue import Queue  # python2
import time

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
        return response


    def parse_response(self, response):
        html = response.content
        html_obj = etree.HTML(html)
        movie_list = html_obj.xpath("//div[@class='info']")

        for movie in movie_list:
            movie_name = movie.xpath(".//span[@class='title'][1]/text()")[0]
            self.queue.put(movie_name)


    def save_data(self):
        pass

    def main(self):
        for url in self.full_url_list:
            response = self.send_request(url)
            self.parse_response(response)

        while not self.queue.empty():
            print(self.queue.get())


if __name__ == '__main__':
    spider = DoubanSpider()
    start = time.time()
    spider.main()
    end = time.time()

    print("[INFO] : using time {}".format(end - start))


