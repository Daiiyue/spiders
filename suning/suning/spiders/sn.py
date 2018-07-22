# -*- coding: utf-8 -*-
import scrapy
import re


class SnSpider(scrapy.Spider):
    name = 'sn'
    allowed_domains = ['snbook.suning.com']
    start_urls = ['http://snbook.suning.com/web/trd-fl/999999/0.htm']
    # http://snbook.suning.com/

    def parse(self, response):
        a_list = response.xpath("//ul[@class='ulwrap']/li//a")
        for a in a_list:
            # item = {}
            class_href = a.xpath("./@href").extract_first()
            class_href = 'http://snbook.suning.com'+ str(class_href)
            # item['class_href'] = a.xpath("./@href").extract_first()
            # item['class_href'] = 'http://snbook.suning.com/'+ str(item['class_href'])
            # item['class_title'] = a.xpath("./text()").extract_first()

            yield scrapy.Request(
                # item['class_href'],
                class_href,
                callback=self.parse_class_detail,
                # meta={"item":item}
            )

    def parse_class_next_detail(self, response):
        # item = response.meta["item"]
        li_list = response.xpath("//li[@class='clearfix']|//li[@class='last clearfix']")
        class_title = response.xpath("//ul[@class='ulwrap']/li//a[@id='{}']/text()".format
                                     (re.findall(r'/web/trd-fl/\d+/(\d+).htm', response.url)[0])).extract_first()
        # class_title = re.findall(r'>(.+)</a>', class_title)[0]
        for li in li_list:
            item = {}
            item['class_title'] = class_title
            item['book_url'] = li.xpath(".//div[@class='book-title']/a/@href").extract_first()
            item['book_name'] = li.xpath(".//div[@class='book-title']/a/text()").extract_first()
            item['book_img'] = li.xpath(".//div[@class='book-img']/a/@href").extract_first()
            item['book_author'] = li.xpath(".//div[@class='book-author']/a/text()").extract_first()
            item['book_descrip'] = li.xpath(".//div[@class='book-descrip c6']/text()").extract_first()
            yield item

    def parse_class_detail(self, response):
        # item = response.meta["item"]
        li_list = response.xpath("//li[@class='clearfix']|//li[@class='last clearfix']")
        class_title = response.xpath("//ul[@class='ulwrap']/li//a[@id='{}']/te"
                                     "ikxt()".format
                                     (re.findall(r'/web/trd-fl/\d+/(\d+).htm',response.url)[0])).extract_first()
        # class_title = re.findall(r'>(.+)</a>',class_title)[0]
        for li in li_list:
            item = {}
            item['class_title'] = class_title
            item['book_url'] = li.xpath(".//div[@class='book-title']/a/@href").extract_first()
            item['book_name'] = li.xpath(".//div[@class='book-title']/a/text()").extract_first()
            item['book_img'] = li.xpath(".//div[@class='book-img']/a/@href").extract_first()
            item['book_author'] = li.xpath(".//div[@class='book-author']/a/text()").extract_first()
            item['book_descrip'] = li.xpath(".//div[@class='book-descrip c6']/text()").extract_first()
            yield item

        # http://snbook.suning.com/web/ebook/checkPriceShowNew.do?bookId=107186698&completeFlag=2&_=1530152880491
        total_page = response.xpath("//script[1]/text()").extract_first()
        total_page = re.findall("var pagecount=(\d+)",total_page)[0]
        # print(response.url+"#"*50+total_page)

        if int(total_page) > 1:
            for i in range (int(total_page)+1):
                # next_url = str(item['class_href'])+'?pageNumber={}&sort=0'.format(i)
                next_url = response.url +'?pageNumber={}&sort=0'.format(i+2)
                yield scrapy.Request(
                    next_url,
                    callback=self.parse_class_next_detail
                )







