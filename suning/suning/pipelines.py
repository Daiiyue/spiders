# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from suning.settings import MONGO_HOST
from pymongo import MongoClient

class SuningPipeline(object):
    def open_spider(self, spider):
        client = MongoClient()
        self.collection = client['test']['test']


    def process_item(self, item, spider):
        spider.settings.get("MONGO_HOST")
        self.collection.insert(dict(item))
        return item