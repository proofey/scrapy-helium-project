import scrapy
from task_1.items import MangoItem
from helium import *
from time import sleep
from webdrivers import install_webdrivers


class MangoSpider(scrapy.Spider):
    name = "mango"
    start_urls = ["https://shop.mango.com/gb/women/skirts-midi/midi-satin-skirt_17042020.html?c=99"]

        
    def parse(self, response):
        install_webdrivers()
        go_to(self.start_urls[0])
        click("Accept all")
        sleep(2)
        click("English")
        sleep(2)
        click("Choose your size")

        name = find_all(S(".product-name"))[0].web_element.text
        color = find_all(S(".colors-info-name"))[0].web_element.text
        price = find_all(S("div.product-prices > span.product-sale.product-sale--discount"))[0].web_element.text
        sizes = find_all(S(".selector-list--opened"))

        all_sizes = [item.web_element.text for item in sizes]

        item = MangoItem()

        item["name"] = name
        item["color"] = color
        item["price"] = float(price[3:])
        item["size"] = all_sizes[0].split("\n")

        kill_browser()
        return item