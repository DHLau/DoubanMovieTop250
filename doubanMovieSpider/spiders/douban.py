# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from doubanMovieSpider.items import DoubanmoviespiderItem


class DoubanSpider(CrawlSpider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )
    """
            movieRank = scrapy.Field()
    # 电影名称
            movieName = scrapy.Field()
    # 电影简评
            movieScore = scrapy.Field()
    # 简评
            movieQuote = scrapy.Field()
    """

    def parse_item(self, response):
        print(response.url)
        data = response.xpath('//li/div[@class="item"]')
        for each in data:
            item = DoubanmoviespiderItem()

            item['movieRank'] = each.xpath('./div[@class="pic"]/em/text()').extract()[0]

            item['movieName'] = each.xpath('.//div[@class="hd"]/a/span[1]/text()').extract()[0]

            quote = each.xpath('.//p[@class="quote"]/span/text()').extract()
            if len(quote) != 0:
                item['movieQuote'] = quote[0]

            yield item

