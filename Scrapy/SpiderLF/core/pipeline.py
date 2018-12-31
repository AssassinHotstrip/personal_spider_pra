# coding:utf-8

class Pipeline(object):
    def process_item(self, item):
        print("[pipeline] : process_item {}".format(item.data))