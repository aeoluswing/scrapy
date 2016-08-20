# -*- conding: utf-8 -*-
# author:jiangyu
# modify:2016-08-18
# gov_affair_detail.py

import scrapy
import json
import re
from ..items import GovAffairDetailItem

class Gov_Affair_Detail_Spider(scrapy.Spider):
	name = "gov_affair_detail"
	start_urls = [
		"http://zwfw.yn.gov.cn/dls/icity/project/guide?code=1000002532901013",
	]

	def parse(self, response):
		# deal with perinfo contents
		perinfo = response.xpath('.//div[@class="perinfo"]')
		perinfo_contents = {}
		for ele in perinfo.xpath('.//span'):
			perinfo_content = ''
			perinfo_item = ele.xpath('./b[1]/text()').extract()[0].strip().replace(':','')
			perinfo_item_contents = ele.xpath('./text() | ./*/text()').extract()
			for subindex in range(0,len(perinfo_item_contents)):

				perinfo_item_contents[subindex] = perinfo_item_contents[subindex].replace('\t','').replace('\n','').replace('\r','').replace(' ','')
				perinfo_content += perinfo_item_contents[subindex]
			perinfo_contents[perinfo_item] = perinfo_content
			print perinfo_contents[perinfo_item] + "!"
		perinfo_contents_json = json.dumps(perinfo_contents,ensure_ascii=False,encoding='utf-8')

		# deal with content_guide contents
		content_guide = response.xpath('.//div[@id="content_guide"]')
		content_guide_contents = {}
		for ele in content_guide.xpath('./div[@class="item-body"]'):
			content_guide_item_content = ''
			content_guide_item = ele.xpath('./div[@class="item-left"]/text()').extract()[0].strip()
			content_guide_item_contents = ele.xpath(
					'./div[@class="item-fwdx"]/p/text() | ./div[@class="item-right"]/text() | ./div[@class="item-right"]/descendant::*/text()').extract()
			for subindex in range(0,len(content_guide_item_contents)):
				content_guide_item_contents[subindex] = content_guide_item_contents[subindex].replace('\t','').replace('\n','').replace('\r','').replace(' ','').replace('&nbsp','')
				content_guide_item_content += content_guide_item_contents[subindex]
			content_guide_item_content = content_guide_item_content
			content_guide_contents[content_guide_item] = content_guide_item_content
		content_guide_contents_json = json.dumps(content_guide_contents,ensure_ascii=False,encoding='utf-8')

		yield GovAffairDetailItem(perinfo_contents=perinfo_contents_json,content_guide_contents=content_guide_contents_json)