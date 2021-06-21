from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from russia24.items import Russia24Item


class Russia24Spider(CrawlSpider):
    name = "russia24pro"
    allowed_domains = ['russia24.pro']
    start_urls = ['https://russia24.pro/','https://russia24.pro/news/']

#задаём адрес и формат файла с данными
    custom_settings={ 'FEED_URI': "russia24pro.xml",
                       'FEED_FORMAT': 'xml'}

#определяем правила формирования валидных url адресов
    rules = (
        Rule(LinkExtractor(allow=('https://russia24.pro/\w+/\d+/',)), callback='parse_page'),    
    
    )
    
    
    def parse_page(self, response):
        root = Selector(response)
        item = Russia24Item()
#Извлекаем со страниц требуемые данные: url адрес, заголовок, текст новости, дату
        item['url'] = response.url
        item['title'] = root.xpath('.//h1/text()').extract()[0]
        item['text'] = root.xpath('//div[@class="r24_text"]')[0]
        item['date'] = root.xpath('.//div[@class="r24_info"]/time/@datetime').extract()[0]
        yield item            