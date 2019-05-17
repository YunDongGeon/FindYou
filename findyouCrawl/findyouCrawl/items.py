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
    auction_price = scrapy.Field()
    #옥션 배송비 유뮤
    auction_del = scrapy.Field()
    #옥션 제품 이미지
    auction_img = scrapy.Field()
    #옥션 제품 상세보기
    auction_url = scrapy.Field()

   #인터파크 카테고리
    interpark_cat = scrapy.Field()
    #인터파크 제품명
    interpark_title = scrapy.Field()
    #인터파크 제품 가격
    interpark_price = scrapy.Field()
    #인터파크 배송비유무
    interpark_del = scrapy.Field()
    #인터파크 이미지
    interpark_img = scrapy.Field()
    #인터파크 url
    interpark_url = scrapy.Field()

    # 11번가 카테고리
    elevenSt_cat = scrapy.Field()
    # 11번가 상품명
    elevenSt_title = scrapy.Field()
    # 11번가 가격
    elevenSt_price = scrapy.Field()
    # 11번가 배송 유무
    elevenSt_del = scrapy.Field()
    # 11번가 제품 이미지 url
    elevenSt_img = scrapy.Field()
    # 11번가 제품 상세보기 url
    elevenSt_url = scrapy.Field()
    pass
