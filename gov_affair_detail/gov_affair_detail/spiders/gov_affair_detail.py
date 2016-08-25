# -*- coding: utf-8 -*-
# author:jiangyu
# modify:2016-08-18
# gov_affair_detail.py

import scrapy
import re
import time
from ..items import GovAffairDetailItem

# read from excel file
def get_url_dict(filepath,sheetname,dict):
	import xlrd
	try:
		data = xlrd.open_workbook(filepath)
		table = data.sheet_by_name(sheetname)
		nrows = table.nrows
		for row in range(nrows):
			affair_type = table.cell(row,0).value
			affair_detail_url = table.cell(row,1).value
			dict[affair_detail_url] = affair_type
	except IOError as e:
		print e
	return dict

class Gov_Affair_Detail_Spider(scrapy.Spider):
	name = "gov_affair_detail"

	# config excel params
	# edit this part per script
	data_dict = {}
	exc_file_path = "F:/document/dailywork/2016-8-1scrapy/gov_affair_urls_private.xlsx"
	exc_sheet_name = "Sheet2"

	start_urls = get_url_dict(exc_file_path,exc_sheet_name,data_dict).keys()
	# start_urls = [
	# 	"http://zwfw.yn.gov.cn/dls/icity/project/guide?code=2000037532901049",
	# ]

	# config re pattern
	pattern = re.compile(r'[\s:]+',re.I | re.M)
	#pattern_nbsp = re.compile(u'\xa0+',re.I | re.M) # \xa0 = &nbsp;

	def parse(self, response):
		affair_type = self.data_dict.get(response.url)
		perinfo_contents = {}
		content_guide_contents = {}
		try:
			# deal with affair topic
			affair_topic = response.xpath('//*[@id="guide-thead-top"]/text()').extract()[0]
			if affair_topic is None:
				raise AttributeError
		except AttributeError as e:
			print e

		try:
			# deal with perinfo contents
			perinfo = response.xpath('.//div[@class="perinfo"]')
			if perinfo is None:
				raise AttributeError
		except AttributeError as e:
			print e

		for ele in perinfo.xpath('.//span'):
			perinfo_content = ''
			perinfo_item = self.pattern.sub(r'',ele.xpath('./b/text()').extract()[0])
			perinfo_item_contents = ele.xpath('./label/text() | ./text()').extract()
			for subindex in range(0,len(perinfo_item_contents)):
				perinfo_content += self.pattern.sub(r'',perinfo_item_contents[subindex])
			perinfo_contents[perinfo_item] = perinfo_content

		try:
			# deal with content_guide contents
			content_guide = response.xpath('.//div[@id="content_guide"]')
			if content_guide is None:
				raise AttributeError
		except AttributeError as e:
			print e

		try:
			item_bodys = content_guide.xpath('./div[@class="item-body"]')
			if item_bodys is None:
				raise AttributeError
		except AttributeError as e:
			print e
		for ele in item_bodys:
			content_guide_item_content = ''
			content_guide_item = self.pattern.sub(r'',ele.xpath('./div[@class="item-left"]/text()').extract()[0])
			try:
				content_guide_item_contents = ele.xpath(
						'./div[@class="item-fwdx"]/p/text() | ./div[@class="item-right"]/text() | ./div[@class="item-right"]/descendant::*/text()').extract()
				if content_guide_item_contents is None:
					raise AttributeError
			except AttributeError as e:
				print e
			for subindex in range(0,len(content_guide_item_contents)):
				content_guide_item_content += unicode(self.pattern.sub(r'',content_guide_item_contents[subindex])).replace(u'\xa0','').encode("utf-8")
			content_guide_contents[content_guide_item] = content_guide_item_content

		yield GovAffairDetailItem(
				affair_topic=affair_topic,
				affair_type=affair_type,
				perinfo_contents=perinfo_contents,
				content_guide_contents=content_guide_contents)