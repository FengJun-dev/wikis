import scrapy

from urllib.parse import unquote
from scrapy.loader import ItemLoader

from wikis.items import WikisItem
from wikis.handle_urls import get_article_url, get_book_url


class WikiSpider(scrapy.Spider):
    name = 'wikisource'
    allow_domains = ['en.wikisource.org']
    start_urls = [
        # 'https://en.wikisource.org/wiki/Main_Page',
        'https://en.wikisource.org/wiki/The_Bird_of_Time/Songs_of_Love_and_Death/The_Bird_of_Time',
    ]

    def __init__(self):
        super(WikiSpider, self).__init__()
        self.book_id = 0
        self.article_id = 0

    def parse(self, response):
        category_url = unquote(response.url)
        category = response.xpath('//h1[@class="firstHeading"]/text()').extract_first()

        book_url_list = response.xpath()
        book_url = get_book_url(self.book_id, book_url_list)

        yield scrapy.Request(
            book_url,
            meta={
                'category': category,
                'category_url': category_url
            },
            callback=self.parse_book,
            dont_filter=True,
        )

    def parse_book(self, response):
        category_url = response.meta['category_url']
        book_url = unquote(response.url)

        book_name = response.xpath('//span[@id="header_title_text"]/text()').extract_first()

        article_url_list = response.xpath('//div[@class="prp-pages-output"]//a/starswith(@href, "")').extract()
        article_url = get_article_url(self.article_id, article_url_list)

        yield scrapy.Request(
            article_url,
            meta={
                'category_url': category_url,
                'book_url': book_url,
                'book_name': book_name,
            },
            callback=self.parse_single_artile,
            dont_filter=True,
        )

    def parse_single_artile(self, response):
        category_url = response.meta['category_url']
        book_url = response.meta['book_url']

        book_name = response.meta['book_name']

        current_url = unquote(response.url)

        title = response.xpath()
        content = response.xpath('//div[@class="prp-pages-output"]/div/p/text()').extract()

        l = ItemLoader(item=WikisItem(), response=response)
        l.add_value('title', title)
        l.add_value('main_category', main_category)
        l.add_value('category', category)
        l.add_value('book', book_name)
        l.add_value('content', content)
        l.add_value('comment', comment)
        l.add_value('quality', quality)
        yield l.load_item()

        next_page = response.xpath('//div[@id="footertemplate"]/div/div/span/a').extract_first()





