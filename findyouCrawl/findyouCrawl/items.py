# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FindyoucrawlItem(scrapy.Item):















    #카테고리
    interpark_cat = scrapy.Field()
    #제품명
    interpark_title = scrapy.Field()
    #제품 가격
    interpark_price = scrapy.Field()
    #배송비유무
    interpark_del = scrapy.Field()
    #이미지
    interpark_img = scrapy.Field()
    #url
    interpark_url = scrapy.Field()

    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
