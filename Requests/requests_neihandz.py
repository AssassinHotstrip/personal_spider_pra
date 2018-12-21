import re

import requests

class NeihanSpider(object):
    """内涵段子爬虫"""
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        # 固定url地址部分
        self.base_url = "https://www.neihan8.com/article/list_5_"
        self.page = 1
        ### 匹配数据的无用字符，并通过sub进行替换为 ""
        # <.*?> 表示匹配 html标签
        # &.*?; 表示匹配html实体字符
        # \s 表示匹配空白符（如换行符、空格符等）
        # 　 或 u"\u3000".encode("utf-8")  表示中文全角空格字符
        # self.data_pattern = re.compile('<.*?>|&.*?;|\s|　')
        self.data_pattern = re.compile('<.*?>|&.*?;|\s|' + u'\u3000')



    def send_request(self, full_url):
        """接受url地址,发送请求并接收响应"""
        print("[INFO] 正在发送请求{}".format(full_url))
        response = requests.get(full_url, headers=self.headers)
        print(response)
        return response


    def parse_response(self, response):
        """接收response响应,提取内容,并返回内容列表"""
        # html = response.content.decode("gbk").encode("utf-8")  # 将网页gbk格式的内容转换为utf-8
        html = response.content.decode("gbk") # 将网页gbk格式的内容转换为utf-8
        print(html)
        print(type(html))

        # 提取页面内容
        self.page_pattern = re.compile('<div class="f18 mb20">(.*?)</div>', re.S)   # re.S 启用DOTALL模式，让 . 也可以匹配换行符
        result_list = self.page_pattern.findall(html)
        print(result_list)
        return result_list



    def save_data(self, result_list):
        print("[INFO] 正在保存第{}页数据".format(self.page))
        with open("neihanduanzi.txt", "a", encoding="utf-8") as f:
        # with open("neihanduanzi.txt", "a") as f:
            for result in result_list:
                data = self.data_pattern.sub("", result)
                f.write(data)
                f.write("\n")
            f.write("\n")





    def main(self):
        while input("按下回车抓取一页,输入Q结束抓取:") != "Q":
            # 1.各页的url地址
            full_url = self.base_url + str(self.page) + ".html"
            # 2.发送请求并接受响应
            response = self.send_request(full_url)
            # 3.解析响应并提取数据
            result_list = self.parse_response(response)
            # 4.保存数据
            self.save_data(result_list)
            # 页面自增
            self.page += 1


if __name__ == '__main__':
    neihan_spider = NeihanSpider()
    neihan_spider.main()

