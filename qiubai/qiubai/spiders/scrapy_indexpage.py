# -*- conding: utf-8 -*-
import scrapy
class QiubaiSpider(scrapy.Spider):
	name = "qiubai"
	start_urls = [
		"http://www.qiushibaike.com/",
	]

	def parse(self, response):
		with open("res.txt","w") as f:
			reslist = response.xpath('//*[@id="qiushi_tag_117292272"]/div[@class="content"]/text()').extract()
			for i in range(0,len(reslist)):
				res =reslist[i].strip()
				print res
				f.write(res.strip().encode("utf-8"))
				f.write("\n")