# -*- coding: utf-8 -*-
# author:jiangyu
# modify:2016-08-16
# scrapy for gov affair topics

import scrapy
class Gov_Affair_Topic_Spider(scrapy.Spider):
	name = "gov_affair_topic"
	start_urls = [
		"http://zwfw.yn.gov.cn/dls/project",
	]

	def parse(self, response):
		with open("personal_affair_topic.txt","w") as f:
			res = response.xpath('//div[@id="sxicondata"]//li//div/font/text()').extract()
			from scrapy.shell import inspect_response
			inspect_response(response, self)
			#f.write(res[0].encode("utf-8"))
