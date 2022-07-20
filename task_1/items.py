import scrapy


class MangoItem(scrapy.Item):
    name = scrapy.Field()
    color = scrapy.Field()
    price = scrapy.Field()
    size = scrapy.Field()
