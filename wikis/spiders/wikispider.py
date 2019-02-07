import scrapy

from urllib.parse import unquote
from scrapy.loader import ItemLoader

from wikis.items import WikisItem


class WikiSpider(scrapy.Spider):
    name = 'wikisource'
    allow_domains = ['en.wikisource.org']
    start_urls = [
        # 'https://en.wikisource.org/wiki/Main_Page',
        'https://en.wikisource.org/wiki/The_Bird_of_Time/Songs_of_Love_and_Death/The_Bird_of_Time',
    ]

    def parse(self, response):
        current_url = unquote(response.url)


        content = response.xpath('//*[@id="columnContainer"]/div[1]/div/div/div[@class="prp-pages-output"]/p/text()')
        l = ItemLoader(item=WikisItem(), response=response)
        l.add_value('title', title)
        l.add_value('main_category', main_category)
        l.add_value('en_category', en_category)
        l.add_value('category', category)
        l.add_value('book', book_name)
        l.add_value('content', new_content)
        l.add_value('comment', new_reference)
        l.add_value('quality', quality)
        yield l.load_item()




