import scrapy
from scrapy.linkextractors import LinkExtractor

from scrapy.spiders import CrawlSpider, Rule, BaseSpider
# from scrapy.selector import HtmlXPathSelector
# from scrapy.item import Item, Field

class interparkCrawlSpider(CrawlSpider):
    name = 'coupang_crawl'
    allowed_domains = ['coupang.com']

    start_urls = [
        'http://www.coupang.com/np/categories/187071'
                  ]

    rules = (
        Rule(LinkExtractor(allow=r'vp/products/.*.\?itemId=.*.&vendorItemId=.*'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'np/categories/187071\?page=.*')),
    )
    def parse_item(self, response):
        # hxs = HtmlXPathSelector(response)

        # sites = hxs.select('//ul[@class="directory-url"]/li')
        # items = []
        i = {}

        # for site in sites:
        #     i['interpark_cat'] = site.select('a/@href').extract()
        #     i['interpark_title'] = site.select('h2/text()').extract()
        #     i['interpark_price'] = site.select('strong/text()').extract()
        #     i['interpark_del'] = site.select('span/text()').extract()
        #     i['interpark_img'] = site.select('img/@src').extract()
        #     i['interpark_url'] = site.select('a/@href').extract()
        #     items.append(i)
        i['interpark_cat'] = response.xpath('//*[@id="breadcrumb"]/li[3]/a/@href').extract()
        i['interpark_title'] = response.xpath('//*[@class="prod-buy-header"]/h2/text()').extract()
        i['interpark_price'] = response.xpath('//*[@class="total-price"]/strong/text()').extract()
        i['interpark_del'] = response.xpath('//*[@class="prod-shipping-fee-message"]/span/text()').extract()
        i['interpark_img'] = response.xpath('//*[@id="repImageContainer"]/img/@src').extract()
        # i['interpark_url'] = response.xpath('').extract()
        return i
