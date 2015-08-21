# -*- coding: utf-8 -*-
import scrapy


class AzlyricsSpider(scrapy.Spider):
    name = "azlyrics"
    allowed_domains = ["azlyrics.com"]
    file = open("../urls.txt")
    start_urls = file.read().split("\n")
    file.close()

    def parse(self, response):
        print response
