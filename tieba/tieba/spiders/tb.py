# -*- coding: utf-8 -*-
import scrapy

allowed_domains = ['tieba.baidu.com']
start_urls = ['https://tieba.baidu.com/f?kw=%E5%A5%87%E5%BC%82%E4%BA%BA%E7%94%9F']


def parse(self, response):
    li_list = response.xpath("//li[@class=' j_thread_list clearfix']")
    print(li_list, "*" * 50)


class TbSpider(scrapy.Spider):
    name = 'tb'


