# -*- coding: utf-8 -*-
import scrapy
import flask
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ElevenStCrawlSpider(CrawlSpider):

    name = 'ElevenSt_Crawl'
    allowed_domains = ['11st.co.kr']
    start_urls = [
        'http://www.11st.co.kr/category/DisplayCategory.tmall?method=getDisplayCategory2Depth&dispCtgrNo=1001841&dispCtgrCd=v0O008',
        'http://www.11st.co.kr/category/DisplayCategory.tmall?method=getDisplayCategory2Depth&dispCtgrNo=1059019&dispCtgrCd=v0O016',
        'http://www.11st.co.kr/category/DisplayCategory.tmall?method=getDisplayCategory2Depth&dispCtgrNo=1059018&dispCtgrCd=v0O015',
        'http://www.11st.co.kr/category/DisplayCategory.tmall?method=getDisplayCategory2Depth&dispCtgrNo=1001843&dispCtgrCd=v0O010',
        'http://www.11st.co.kr/category/DisplayCategory.tmall?method=getDisplayCategory2Depth&dispCtgrNo=1001840&dispCtgrCd=v0O007',
        'http://www.11st.co.kr/category/DisplayCategory.tmall?method=getDisplayCategory2Depth&dispCtgrNo=1001834&dispCtgrCd=v0O001',
        'http://www.11st.co.kr/category/DisplayCategory.tmall?method=getDisplayCategory2Depth&dispCtgrNo=1001844&dispCtgrCd=v0O011',
        'http://www.11st.co.kr/category/DisplayCategory.tmall?method=getDisplayCategory2Depth&dispCtgrNo=1001837&dispCtgrCd=v0O004',
        'http://www.11st.co.kr/category/DisplayCategory.tmall?method=getDisplayCategory2Depth&dispCtgrNo=1001836&dispCtgrCd=v0O003',
        'http://www.11st.co.kr/category/DisplayCategory.tmall?method=getDisplayCategory2Depth&dispCtgrNo=1001842&dispCtgrCd=v0O009',
        'http://www.11st.co.kr/category/DisplayCategory.tmall?method=getDisplayCategory2Depth&dispCtgrNo=1001835&dispCtgrCd=v0O002',
        'http://www.11st.co.kr/category/DisplayCategory.tmall?method=getDisplayCategory2Depth&dispCtgrNo=1001838&dispCtgrCd=v0O005'
        'http://www.11st.co.kr/category/DisplayCategory.tmall?method=getDisplayCategory2Depth&dispCtgrNo=1001839&dispCtgrCd=v0O006',
        'http://www.11st.co.kr/category/DisplayCategory.tmall?method=getDisplayCategory2Depth&dispCtgrNo=1001845&dispCtgrCd=v0O012',
        'http://www.11st.co.kr/category/DisplayCategory.tmall?method=getDisplayCategory2Depth&dispCtgrNo=1001846&dispCtgrCd=v0O013',
        'http://www.11st.co.kr/category/DisplayCategory.tmall?method=getDisplayCategory2Depth&dispCtgrNo=1001847&dispCtgrCd=v0O014'
                ]
    rules = (
        Rule(LinkExtractor(
            allow=r'category/DisplayCategory.tmall\?method=getDisplayCategory2Depth&dispCtgrNo=.*.&dispCtgrCd=.*.#pageNum%%.*,$$viewType%%L')),
        Rule(LinkExtractor(
            allow=r'product/SellerProductDetail.tmall\?method=getSellerProductDetail&prdNo=.*.&trTypeCd=.*.&trCtgrNo=.*'),
            callback='parse_item', follow=True)
    )
    def parse_item(self, response):
        item = {}
        # 11번가 카테고리
        item['elevenSt_cat'] = response.xpath('//*[@id="headSel_3"]/text()')[0].extract().strip()
        # 11번가 상품명
        item['elevenSt_title'] = response.xpath('//*[@class="heading"]/h2/text()')[0].extract().strip()
        # 11번가 가격
        item['elevenSt_price'] = response.xpath('//*[@class="sale_price"]/text()')[0].extract().strip()
        # 11번가 배송 유무
        item['elevenSt_del'] = response.xpath('//*[@class="row"]/div[1]/text()')[0].extract().strip()
        # 11번가 제품 이미지 url
        item['elevenSt_img'] = response.xpath('//*[@id="thumb"]/div/span/img/@src')[0].extract()
        # 11번가 상세보기
        item['elevenSt_url'] = response.request.url

        return item
