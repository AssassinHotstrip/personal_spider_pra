import requests
from lxml import etree
from bs4 import BeautifulSoup


class HupuSpider(object):
    def __init__(self):
        self.base_url= "https://bbs.hupu.com"
        self.start_page = int(input("请输入要爬取的起始页:"))
        self.end_page = int(input("请输入要爬取的终止页:"))
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}



    def send_request(self, url):
        print("[INFO] 正在发送请求: {}".format(url))
        response = requests.get(url, headers=self.headers)
        return response


    def parse_page(self, response):
        html = response.content
        html_obj = etree.HTML(html)
        page_link_list = html_obj.xpath('//a[@class="truetit"]/@href')
        # print(page_link_list)
        return page_link_list


    def parse_image(self, response):
        html = response.content
        html_obj = etree.HTML(html)
        # image_link_list = html_obj.xpath('//a[@class="downimg"]/@download')
        image_link_list = html_obj.xpath('//img[@src]')
        print(image_link_list)

        return image_link_list

    def save_image(self, response, file_name):
        print("[INFO] 正在保存图片{}".format(file_name))
        with open(file_name, "wb") as f:
            f.write(response.content)



    def main(self):
        # 获取帖子网页链接
        for page in range(self.start_page, self.end_page + 1):
            full_url = self.base_url + "/selfie-" + str(page)
            response = self.send_request(full_url)
            page_link_list = self.parse_page(response)

            # 解析帖子链接,获取图片链接表
            for page_link in page_link_list:
                # 每个帖子的链接

                page_url = self.base_url + page_link
                print(page_url)
                response = self.send_request(page_url)

                image_link_list = self.parse_image(response)
                print(image_link_list)
                for image_link in image_link_list:
                    print(image_link)
                    response = self.send_request(image_link)
                    self.save_image(response, image_link[-8:])





if __name__ == '__main__':
    hupu_spider = HupuSpider()
    hupu_spider.main()