import scrapy

from urllib.parse import unquote
from scrapy.loader import ItemLoader

from wikis.items import WikisItem
from wikis.handle_urls import get_url, set_start_urls
from wikis.utils.handle_xpath import xpath_handler
from wikis.utils.handle_content import content_handler
from wikis.sql.settings import session
from wikis.sql.models import Book, Article


class WikiSpider(scrapy.Spider):
    name = 'wikisource'
    allow_domains = ['en.wikisource.org']
    url_prefix = 'https://en.wikisource.org/wiki'
    category = ['Featured_texts']
    start_urls = set_start_urls(prefix=url_prefix, category=category)

    def __init__(self):
        super(WikiSpider, self).__init__()
        self.book_id = 1
        self.article_id = 1

    def parse(self, response):
        category_url = unquote(response.url)
        category = response.xpath('//h1[@class="firstHeading"]/text()').extract_first()

        book_url_xpath = '//div[@class="mw-category-group"]/ul/li/a/@href'

        book_url_list = response.xpath(book_url_xpath).extract()
        book_url = get_url(self.book_id, book_url_list)

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

        author_xpath = '//span[@id="header_author_text"]/span[@class="fn"]/text()'
        book_name_xpath = '//span[@id="header_title_text"]/text()'
        title_xpath = '//div[@class="gen_header_title"]/b/span[@id="header_title_text"]/text()'

        category = response.meta['category']
        book_name = xpath_handler(response, book_name_xpath)
        author = xpath_handler(response, author_xpath)

        title = xpath_handler(response=response, item_xpath=title_xpath)
        content = content_handler(response=response)

        if title and content:
            article = Article(
                title=title,
                content=content,
            )
            session.add(article)
            session.commit()

        book = Book(
            category=category,
            name=book_name,
            author=author,
        )
        session.add(book)
        session.commit()

        article_url_list = response.xpath('//div[@class="prp-pages-output"]/a/@href[stars-with(@href, "/wiki/")]').extract()
        article_url = get_url(self.article_id, article_url_list)

        if article_url:
            yield scrapy.Request(
                article_url,
                meta={
                    'category_url': category_url,
                    'book_url': book_url,
                    'book_name': book_name,
                    'content': content
                },
                callback=self.parse_single_artile,
                dont_filter=True,
            )
        yield scrapy.Request(
            category_url,
            callback=self.parse,
            dont_filter=True
        )

    def parse_single_artile(self, response):
        category_url = response.meta['category_url']
        book_url = response.meta['book_url']

        category = response.meta['category']
        book_name = response.meta['book_name']

        title_xpath = '//div[@class="gen_header_title"]/b/span[@id="header_title_text"]/text()'

        comment_xpath = ''
        quality_xpath = '//div[@class="mw-normal-catlinks"]/text()'

        title = xpath_handler(response=response, item_xpath=title_xpath)
        content = content_handler(response=response)
        comment = xpath_handler(response=response, item_xpath=comment_xpath)
        quality = xpath_handler(response=response, item_xpath=quality_xpath)

        article = Article(
            title=title,
            content=content,
        )
        session.add(article)
        session.commit()

        loader = ItemLoader(item=WikisItem(), response=response)
        loader.add_value('article_id', self.article_id)
        loader.add_value('title', title)
        loader.add_value('category', category)
        loader.add_value('book', book_name)
        loader.add_value('content', content)
        loader.add_value('comment', comment)
        loader.add_value('quality', quality)
        yield loader.load_item()

        yield scrapy.Request(
            unquote(book_url),
            meta={
                'category_url': category_url,
                'category': category,
                'book_name': book_name,
            },
            callback=self.parse_book,
            dont_filter=True,
        )
