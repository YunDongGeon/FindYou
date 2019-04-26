# -*- coding: utf-8 -*-
import scrapy
import flask
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ElevenStCrawlSpider(CrawlSpider):
    name = 'ElevenSt_Crawl'
    allowed_domains = ['11st.co.kr']
    start_urls = [
        'http://www.11st.co.kr/category/DisplayCategory.tmall?method=getDisplayCategory4Depth&dispCtgrNo=1012884',
        'http://www.11st.co.kr/category/DisplayCategory.tmall?method=getDisplayCategory4Depth&dispCtgrNo=1012889',
        'http://www.11st.co.kr/category/DisplayCategory.tmall?method=getDisplayCategory4Depth&dispCtgrNo=1012890',
        'http://www.11st.co.kr/category/DisplayCategory.tmall?method=getDisplayCategory4Depth&dispCtgrNo=1012888',
                ]
    rules = (
        Rule(LinkExtractor(allow=r'product/SellerProductDetail.tmall\?method=getSellerProductDetail&prdNo=.*.&trTypeCd=.*.&trCtgrNo=.*')),
        Rule(LinkExtractor(allow=r'category/DisplayCategory.tmall\?method=getDisplayCategory3Depth&dispCtgrNo=.*.#pageNum%%\d$$sortCd%%SPC'),
        callback='parse_url', follow=True)
    )
    def parse_item(self, response):
        item = {}
        # 11번가 카테고리
        item['elevenSt_cat'] = response.xpath('//*[@id="headSel_3"]/text()').extract()
        # 11번가 상품명
        item['elevenSt_title'] = response.xpath('//*[@id="productInfoMain"]/div[2]/div[2]/h2/text()').extract()
        # 11번가 가격
        #item['elevenSt_price'] = response.xpath('//*[@id="prdcInfoColumn2"]/div[1]/div[1]/span[2]/strong/text()').extract()
        item['elevenSt_price'] = response.xpath('//strong[@class, "sale_price"]/text()').get()
        # 11번가 배송 유무
        item['elevenSt_del'] = response.xpath('//*[@id="prdcInfoColumn2"]/div[3]/div[1]/div/text()').extract()
        # 11번가 제품 이미지 url
        item['elevenSt_img'] = response.xpath('//*[@id="thumb"]/div/span/img/@src').extract()
        # 11번가 상세보기
        item['elevenSt_url'] = response.request.url
        return item
