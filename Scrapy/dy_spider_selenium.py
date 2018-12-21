import time
import unittest

from selenium import webdriver
from lxml import etree


import pymongo

class DySpider(unittest.TestCase):
    """斗鱼主播信息"""
    def setUp(self):
        """初始化"""
        # 创建一个PhantonJS浏览器
        self.driver = webdriver.PhantomJS()
        # 计数器,计算主播数
        self.count = 0

        # 创建MongoDB数据库链接和集合，用来保存数据
        self.client = pymongo.MongoClient()
        #                             数据库名  集合名
        self.collection = self.client.douyu.directory


    def testDy(self):
        # 通过浏览器打开页面
        self.driver.get("https://www.douyu.com/directory/all")
        while True:
            # 通过xpath获取当前页面所有主播节点

            # 获取当前页面unicode源码字符串
            html = self.driver.page_source
            html_obj = etree.HTML(html)
            node_list = html_obj.xpath('//div[@id="live-list-content"]//div[@class="mes"]')

            # 迭代每个节点,并获取信息
            for node in node_list:
                item = {}
                item["room"] = node.xpath(".//h3[@class='ellipsis']/text()")[0].strip()
                item["tag"] = node.xpath(".//span[@class='tag ellipsis']/text()")[0].strip()
                try:
                    item["name"] = node.xpath(".//span[@class='dy-name ellipsis fl']/text()")[0].strip()
                except:
                    item["name"] = ""
                    # 防止观看人数为0获取不到数据时报错
                try:
                    item["num"] = node.xpath(".//span[@class='dy-num fr']/text()")[0].strip()
                except:
                    item["num"] = 0
                print(item)
                # 将数据插入MongoDB的集合中
                self.collection.insert(item)

                self.count += 1

            # 换页
            # find()会返回查找数据的索引,若查询不到则返回-1
            # if 判断当前页面是否是最后一页，如果是:
            # 在页面里查找指定字符串，如果没找到，返回-1，表示没到最后一页
            # 如果找到了，返回是下标值（不是-1）,表示到了最后一页，可以退出循环
            if html.find("shark-pager-disable-next") != -1:
                return
            else:
                self.driver.find_element_by_class_name("shark-pager-next").click()
                # 等待页面渲染完成后才进行下一步,以防报错
                time.sleep(3)



    def tearDown(self):
        print()
        print("爬取结束")
        print(self.count)

        # 退出
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()