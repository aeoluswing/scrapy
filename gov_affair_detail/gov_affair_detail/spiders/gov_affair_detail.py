# -*- conding: utf-8 -*-
# author:jiangyu
# modify:2016-08-18
# gov_affair_detail.py

import scrapy
#from gov_affair_detail.items import GovAffairDetailItem
from scrapy.shell import inspect_response

class Gov_Affair_Detail_Spider(scrapy.Spider):
	name = "gov_affair_detail"
	start_urls = [
		"http://zwfw.yn.gov.cn/dls/icity/project/guide?code=1000002532901013",
	]

	def parse(self, response):
		# deal with affair detail page topic
		detail_topic = response.xpath('//div[@id="guide-thead-top"]/text()').extract()[0] if response.xpath('//div[@id="guide-thead-top"]') else ""

		# deal with perinfo contents
		perinfo = response.xpath('.//div[@class="perinfo"]')
		perinfo_contents = []
		for ele in perinfo.xpath('.//span'):
			perinfo_item_contents = []
			perinfo_item = ''
			perinfo_content = ''
			perinfo_item = ele.xpath('./b[1]/text()').extract()[0].strip()
			perinfo_item_contents = ele.xpath('./text() | ./label/text()').extract()
			for subindex in range(0,len(perinfo_item_contents)):
				perinfo_item_contents[subindex] = perinfo_item_contents[subindex].strip()
			perinfo_content = '\n'.join(perinfo_item_contents)
			perinfo_contents.append({perinfo_item:perinfo_content})

		# deal with content_guide contents
		content_guide = response.xpath('.//div[@id="content_guide"]')
		content_guide_contents = []
		for ele in content_guide.xpath('./div[@class="item-body"]'):
			content_guide_item = ''
			content_guide_item_contents = []
			content_guide_item_content = ''
			content_guide_item = ele.xpath('./div[@class="item-left"]/text()').extract()[0].strip()
			content_guide_item_contents = ele.xpath(
					'./div[@class="item-fwdx"]/p/text() | ./div[@class="item-right"]/text() | ./div[@class="item-right"]/descendant::*/text()').extract()
			for subindex in range(0,len(content_guide_item_contents)):
				content_guide_item_contents[subindex] = content_guide_item_contents[subindex].strip()
			content_guide_item_content = '\n'.join(content_guide_item_contents)
			content_guide_contents.append({content_guide_item:content_guide_item_content})

		#yield GovAffairDetailItem(affair_detail_topic=detail_topic,perinfo_contents=perinfo_contents,)