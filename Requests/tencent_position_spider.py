import json

import requests
from lxml import etree
from bs4 import BeautifulSoup


class TencentSpider(object):
    """爬取腾讯招聘职位信息"""
    def __init__(self):
        """init"""
        self.base_url = "https://hr.tencent.com/position.php?&start="
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.page = 0  # 页面控制数值,每页自增10,最大值2830
        self.item_list = []  # 职位信息列表,用于存放所有职位详细信息


    def send_request(self, url):
        """发送请求,返回响应"""
        print("[INFO] 正在发送请求:{}".format(url))
        response = requests.get(url, headers=self.headers)
        print(response.content)
        return response


    def parse_respons(self, response):
        """解析网页,获取到所需信息"""
        html = response.content

        # 解析方式一:用xpath解析
        # html_obj = etree.HTML(html)
        # # 获取每页的职位列表(每页10个)
        # position_list = html_obj.xpath('//tr[@class="even"] | //tr[@class="odd"]')

        # 解析方式二:用BeautifulSou解析
        soup = BeautifulSoup(html, "lxml")  # 解析html,用BeautifulSou方式查询,并使用lxml方式解析(由于BeautifulSou解析速度漫,指定使用lxml方式解析)
        position_list = soup.find_all("tr", {"class": ["even", "odd"]})

        for position in position_list:
            # 遍历个职业信息的岗位详情, 以字典形式
            item = {}

            # 解析方式一:用xpath解析
            # 注意:xpath默认返回的都是列表, 故需要取  列表[0]
            # 职位名称
            # item["position_name"] = position.xpath('./td[1]/a/text()')[0]
            #
            # # 职位链接
            # item["position_link"] = "https://hr.tencent.com/" + position.xpath('./td[1]/a/@href')[0]
            #
            # # 职位类别
            # item["position_class"] = position.xpath('./td[2]/text()')[0]
            #
            # # 人数
            # item["provide_num"] = position.xpath('./td[3]/text()')[0]
            #
            # # 地点
            # item["work_location"] = position.xpath('./td[4]/text()')[0]
            #
            # # 发布时间
            # item["publish_name"] = position.xpath('./td[5]/text()')[0]


            # 解析方式二:用BeautifulSou解析
            # 注意:find_all返回的是一个列表,需根据对应位置取值
            # 职位名称
            item["position_name"] = position.find_all("td")[0].a.text
            # item["position_name"] = position.find_all("td")[0].a.get_text
            # item["position_name"] = position.find_all("td")[0].a.string

            # 职位链接
            item["position_link"] = "https://hr.tencent.com/" + position.find_all("td")[0].a.get("href")
            try:  # 有的没有职位信息,不try会报错
                # 职位类别
                item["position_class"] = position.find_all("td")[1].text
            except:
                item["position_class"] = None
            # 人数
            item["provide_num"] = position.find_all("td")[2].text
            # 地点
            item["work_location"] = position.find_all("td")[3].text
            # 发布时间
            item["publish_name"] = position.find_all("td")[4].text

            self.item_list.append(item)

        html_obj = etree.HTML(html)
        # 判断是否为末页(xpath查询的为末页)
        if not html_obj.xpath("//a[@class='noactive' and @id='next']"):
            # 提取下一页链接，并返回
            next_url = "https://hr.tencent.com/" + html_obj.xpath("//a[@id='next']/@href")[0]
            return next_url


    def save_data(self):
        """保存数据"""

        # json_data = json.dumps(self.item_list, ensure_ascii=False)  # 将python类型转成json字符串
        # # 写入保存
        # with open("tencent.json", "w") as f:
        #     f.write(json_data)

        json.dump(self.item_list, open("tencent.json", "w"), ensure_ascii=False)



    def main(self):
        """主函数"""
        # for page in range(0, 2830, 10):  # 2830在实际网页中不是固定值
        next_url = self.base_url + str(self.page)

        while True:
            response = self.send_request(next_url)

            next_url = self.parse_respons(response)
            if next_url is None:
                break

        # 保存数据
        self.save_data()



if __name__ == '__main__':
    position_spider = TencentSpider()
    position_spider.main()

