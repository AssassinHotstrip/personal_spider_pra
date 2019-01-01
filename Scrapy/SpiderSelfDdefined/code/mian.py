# coding:utf-8


from SpiderAssassin.core.engine import Engine

# from baidu_spider import BaiduSpider
from douban_spider import DoubanSpider


def main():
    # baidu_spider = BaiduSpider()
    douban_spider = DoubanSpider()
    engine = Engine(douban_spider)
    engine.start()

if __name__ == '__main__':
    main()