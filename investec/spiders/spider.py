import scrapy
from scrapy.exceptions import CloseSpider

from scrapy.loader import ItemLoader
from ..items import InvestecItem
from itemloaders.processors import TakeFirst


class InvestecSpider(scrapy.Spider):
	name = 'investec'
	start_urls = ['https://www.investec.com/en_ie/welcome-to-investec/press.html']

	def parse(self, response):
		post_links = response.xpath('//div[@class="col-12 col-sm-6 col-lg-3 sub-nav__link"]/secondary-cta/@ng-href')
		yield from response.follow_all(post_links, self.parse_post)

	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//h3/text()|//div[@class="detailed-information parbase"]/descendant-or-self::*/text()[normalize-space() and not(ancestor::noscript | ancestor::script | ancestor::div[@class="footer__wrapper"])]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//div[@class="articles-header__date"]/p/text()').get()

		item = ItemLoader(item=InvestecItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
