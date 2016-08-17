# -*- conding: utf-8 -*-
import scrapy
from gov_affair_detail.items import GovAffairDetailItem

class Gov_Affair_Detail_Spider(scrapy.Spider):
	name = "gov_affair_detail"
	start_urls = [
		"http://zwfw.yn.gov.cn/dls/icity/project/guide?code=1000002532901013",
	]

	def parse(self, response):
		for mainclearfix in response.xpath('//div[@class="main clearfix"]'):

			for perinfo in mainclearfix.xpath('.//div[@class="perinfo"]'):
				perinfo_subitems = perinfo.xpath('.//span/b/text()').extract()
				perinfo_subdetails = perinfo.xpath('.//span/label/text()').extract()




				yield GovAffairDetailItem(author=authors,content=contents)