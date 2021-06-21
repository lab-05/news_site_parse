from datetime import datetime
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter
#

class Russia24Pipeline(object):
    def process_item(self, item, spider):
        item['date'] = datetime.strptime(item['date'].split('+')[0], "%Y-%m-%dT%H:%M:%S")
        item['text'] = ''.join(item['text'].xpath('descendant::text()').extract())
        return item