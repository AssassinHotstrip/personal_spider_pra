import urllib.request
import urllib.parse
import logging


# https://tieba.baidu.com/f?kw=d8&ie=utf-8&pn=50(第二页)
class BaiduSpider(object):
    def __init__(self):
        self.base_url = "https://tieba.baidu.com/f?"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; "
                          "Trident/7.0; rv:11.0) like Gecko"
        }
        self.tieba_name = input("请输入贴吧名:")
        self.start_page = int(input("请输入首页:"))
        self.end_page = int(input("请输入末页:"))


    def send_request(self, url):
        """接收url地址,发送请求返回响应"""
        logging.info("正在发送请求: {}...".format(url))
        # 正在发送请求: 对应url...

        # 构建并发送请求
        request = urllib.request.Request(url, headers=self.headers)
        response = urllib.request.urlopen(request)
        # 返回响应对象
        return response

    def parse_response(self):
        pass


    def save_data(self, response, file_name):
        """接收并保存数据"""
        logging.info("saving:{}...".format(file_name))

        with open(file_name, "wb") as f:
            f.write(response.read())


    def main(self):
        """调度"""
        for page in range(self.start_page, self.end_page + 1):

            pn = (page - 1) * 50

            # 构建查询参数字典
            query_dict = {"pn" : pn, "kw" : self.tieba_name}
            # 构建查询字符串
            query_str = urllib.parse.urlencode(query_dict)

            # 完整url
            full_url = self.base_url + query_str

            response = self.send_request(full_url)

            # 构建响应文件名
            file_name = self.tieba_name + str(page) + ".html"

            self.save_data(response, file_name)



if __name__ == '__main__':
    spider = BaiduSpider()
    spider.main()