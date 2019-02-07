import scrapy


class WikiSpider(scrapy.Spider):
    name = 'wikisource'
    allow_domains = ['en.wikisource.org']

    start_urls = []

    def parse(self, response):
        pass




