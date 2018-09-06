# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
from pymongo import MongoClient

class YangguangPipeline(object):

    def open_spider(self, spider):
        client = MongoClient(host='132.232.19.246', port=27017)
        self.collection = client["tencent"]["test"]

    def process_item(self, item, spider):
        item["content"] = self.process_content(item["content"])
        # print(item)
        self.collection.insert(dict(item))
        return item

    def process_content(self, content):
        content = [re.sub(r"\xa0|\s", "",i) for i in content] # 将\xa0字符串转换为空格
        content = [i for i in content if len(i) > 0] # 去除content中的空字符串
        return content