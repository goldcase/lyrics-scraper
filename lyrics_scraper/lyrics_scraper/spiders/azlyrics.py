# -*- coding: utf-8 -*-
import scrapy


class AzlyricsSpider(scrapy.Spider):
    name = "azlyrics"
    allowed_domains = ["azlyrics.com"]
    start_urls = (
        'http://www.azlyrics.com/',
    )

    def parse(self, response):
        pass
