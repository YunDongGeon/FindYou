import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class AuctionCrawlSpider(CrawlSpider):
    name = 'auction_crawl'
    allow_domains = ['auction.co.kr']

    start_urls=[
                # 1.반팔티셔츠
                # 1-1. 라운드넥티셔츠
                'http://browse.auction.co.kr/list?category=13290300&s=8',
                # 1-2. 카라넥티셔츠
                'http://browse.auction.co.kr/list?category=13290200&s=8',
                # 1-3. 브이넥티셔츠
                'http://browse.auction.co.kr/list?category=13290100&s=8',
                # 1-4. 민소매/나시티셔츠
                'http://browse.auction.co.kr/list?category=13290500&s=8'
                ]
    rules = (
        Rule(LinkExtractor(allow=r'http://itempage3.auction.co.kr/DetailView.aspx\?itemno=.*'),
             callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'http://browse.auction.co.kr/list\?category=.*.+&s=8+&k=0+&p=\d'),
             callback='parse_url', follow=True))

    def parse_url(self, response):
        url = {}
        return url

    def parse_item(self, response):
        i = {}
        # 옥션 제품 카테고리
        i['auction_cat'] = response.xpath('//*[@id="locbar"]/div/div[1]/div[3]/a/strong/text()').extract()
        # 옥션 제품명
        i['auction_title'] = response.xpath('//*[@id="frmMain"]/h1/span/text()').extract()
        # 옥션 제품가격
        i['auction_price1'] = response.xpath('//*[@id="frmMain"]/div[3]/div[1]/div/span/strong/text()').extract()
        i['auction_price2'] = response.xpath('//*[@id="frmMain"]/div[2]/div[1]/div/span/strong/text()').extract()
        # # 옥션 배송비 유뮤
        i['auction_del'] = response.xpath('//*[@id="ucShippingInfo_btnShippingInfoTitleText"]/em/text()').extract()
        # i['auction_del'] = response.xpath('//*[@id="ucShippingInfo_btnShippingInfoTitleText"]//text()').extract()
        # 옥션 제품 이미지
        i['auction_img'] = response.xpath('///*[@id="content"]/div[2]/div[1]/div/div/ul/li[1]/a/img/@src').extract()
        # 옥션 제품 상세보기
        i['auction_url'] = response.xpath('').extract()
        return i

