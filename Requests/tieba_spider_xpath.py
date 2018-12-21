# 使用xpath方法提取

import requests
from lxml import etree


class TiebaSpider(object):
    """爬取贴吧"""
    def __init__(self):
        """初始化"""
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.base_url = "http://tieba.baidu.com"

        self.tieba_name = input("请输入需要爬取的贴吧名:")
        self.start_page = int(input("请输入需要爬取的起始页:"))
        self.end_page = int(input("请输入需要爬取的终止页:"))


    def send_request(self, url, params={}):
        """发送请求,返回响应"""
        response = requests.get(url, params=params, headers=self.headers)
        return response


    def parse_page(self, response):
        """解析各个页面"""
        html = response.content
        html_obj = etree.HTML(html)
        # 获取到单个帖子的页面的url后半部分(前半部分为base_url)
        page_link_list = html_obj.xpath('//a[@class="j_th_tit "]/@href')
        print(page_link_list)
        return page_link_list

    def parse_iamge(self, response):
        """解析图片链接"""
        html = response.content
        html_obj = etree.HTML(html)
        # 获取到单个帖子的页面的url后半部分(前半部分为base_url)
        image_link_list = html_obj.xpath('//img[@class ="BDE_Image"]/@src')
        return image_link_list


    def save_image(self, response, file_name):
        """保存图片"""
        print("[INFO] 正在保存图片{}".format(file_name))
        with open(file_name, "wb") as f:
            f.write(response.content)


    def mian(self):

        # 从一级页面(目标贴吧页面)获取单个帖子的链接
        for page in range(self.start_page, self.end_page + 1):
            pn = (page - 1) * 50
            query_dict = {"kw" : self.tieba_name, "pn" : pn}  # 查询字典
            full_url = self.base_url + "/f?"
            response = self.send_request(full_url, query_dict)

            # 获取每个帖子的页面信息
            page_link_list = self.parse_page(response)

            # 从二级页面(单个帖子)获取图片的链接
            for page_link in page_link_list:
                page_url = self.base_url + page_link
                response = self.send_request(page_url)

                # 获取图片链接表
                image_link_list = self.parse_iamge(response)

                # 从三级页面(图片)保存图片地址
                for image_link in image_link_list:
                    response = self.send_request(image_link)
                    self.save_image(response, image_link[-15:])

if __name__ == '__main__':
    tieba_image = TiebaSpider()
    tieba_image.mian()