import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class interparkCrawlSpider(CrawlSpider):
    name = 'interpark_crawl'
    allowed_domains = ['interpark.com']
    start_urls = [
                  'http://shopping.interpark.com/display/list.do?dispNo=001209001001&type=web&minPrice=&maxPrice=&brand=&cardDiscountYn=N&deliveryYn=N&sort=recommend&page=1&rows=60&iq=&entrGroupNo=&nq=&smid1=category&',
                  'http://shopping.interpark.com/display/list.do?dispNo=001209001002&type=web&minPrice=&maxPrice=&brand=&cardDiscountYn=N&deliveryYn=N&sort=recommend&page=1&rows=60&iq=&entrGroupNo=&nq=&smid1=category&',
                  'http://shopping.interpark.com/display/list.do?dispNo=001209001003&type=web&minPrice=&maxPrice=&brand=&cardDiscountYn=N&deliveryYn=N&sort=recommend&page=1&rows=60&iq=&entrGroupNo=&nq=&smid1=category&',
                  'http://shopping.interpark.com/display/list.do?dispNo=001209001004&type=web&minPrice=&maxPrice=&brand=&cardDiscountYn=N&deliveryYn=N&sort=recommend&page=1&rows=60&iq=&entrGroupNo=&nq=&smid1=category&',
                  'http://shopping.interpark.com/display/list.do?dispNo=001209001005&type=web&minPrice=&maxPrice=&brand=&cardDiscountYn=N&deliveryYn=N&sort=recommend&page=1&rows=60&iq=&entrGroupNo=&nq=&smid1=category&',
                  'http://shopping.interpark.com/display/list.do?dispNo=001209001006&type=web&minPrice=&maxPrice=&brand=&cardDiscountYn=N&deliveryYn=N&sort=recommend&page=1&rows=60&iq=&entrGroupNo=&nq=&smid1=category&',
    ]

    rules = (
        Rule(LinkExtractor(allow=r'product/productInfo.do\?prdNo=.*&dispNo=00120900100\d+&smid1=commom_prd'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'display/list.do?dispNo=001209001001&type=web&minPrice=&maxPrice=&brand=&cardDiscountYn=N&deliveryYn=N&sort=recommend&page=\d&rows=60&iq=&entrGroupNo=&nq=&smid1=category&'),
             callback='parse_url', follow=True),
    )
    def parse_url(self, response):
        url = {}
        url['interpark_url'] = response.xpath('//*[@id="normalListUl"]/li[1]/div[2]/a/@href').extract()
        return url
    def parse_item(self, response):
        i = {}

        i['interpark_cat'] = response.xpath('//*[@id="productWrapper"]/div[1]/div/ul/li[3]/a/text()').extract()
        i['interpark_title'] = response.xpath('//*[@id="productName"]/span[2]/text()').extract()
        i['interpark_price'] = response.xpath('//*[@id="priceWrap"]/div[2]/span[1]/em/text()').extract()
        i['interpark_del'] = response.xpath('//*[@id="deliveryInfo"]/div[1]/dl/dd/a/span/text()').extract()
        i['interpark_img'] = response.xpath('//*[@id="productView"]/div[1]/div[1]/div[1]/ul/li[1]/img/@src').extract()

        return i