
import scrapy

class BiaoqingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    page = scrapy.Field()
    pass
