# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DoubanmoviespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 电影排行
    movieRank = scrapy.Field()
    # 电影名称
    movieName = scrapy.Field()
    # 电影简评
    movieScore = scrapy.Field()
    # 简评
    movieQuote = scrapy.Field()
