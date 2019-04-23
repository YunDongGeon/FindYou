
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FindyoucrawlItem(scrapy.Item):
    # define the fields for your item here like:
    #옥션 제품 카테고리
    auction_cat = scrapy.Field()
    #옥션 제품명
    auction_title = scrapy.Field()
    #옥션 제품가격
    auction_price1 = scrapy.Field()
    auction_price2 = scrapy.Field()
    #옥션 배송비 유뮤
    auction_del = scrapy.Field()
    #옥션 제품 이미지
    auction_img = scrapy.Field()
    #옥션 제품 상세보기
    auction_url = scrapy.Field()
    pass


# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FindyoucrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

