# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GovAffairDetailItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    affair_topic = scrapy.Field()
    affair_type = scrapy.Field()
    perinfo_contents = scrapy.Field()
    content_guide_contents = scrapy.Field()