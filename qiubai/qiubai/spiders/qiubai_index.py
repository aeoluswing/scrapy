# -*- conding: utf-8 -*-
import scrapy
class QiubaiSpider(scrapy.Spider):
	name = "qiubai"
	start_urls = [
		"http://www.qiushibaike.com/",
	]

	def parse(self, response):
		with open("res.txt","w") as f:
			reslist = response.xpath('//div[@class="content"]/text()').extract()
			for i in range(len(reslist)):
				res =reslist[i].strip()
				print res
				f.write(res.strip().encode("utf-8"))
				f.write("\n")