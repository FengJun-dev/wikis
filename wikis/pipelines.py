import psycopg2

from wikis.settings import DATABASES
from wikis.sql.models import Book, Article
from wikis.sql.settings import Session


class WikisPipeline(object):
    def __init__(self):
        self.conn = psycopg2.connect(**DATABASES)
        self.cursor = self.conn.cursor()
        self.session = Session()

    def process_item(self, item, spider):
        title = item['title']
        name = item['name']
        author = item['author']
        content = item['content']
        comment = item['comment']
        main_category = item['main_category']
        category = item['category']
        book = Book(
            category=category,
            name=name,
            author=author
        )
        article = Article(
            title=title,
            content=content,
        )
        session = Session()
        session.add(book)
        session.add(article)
        session.commit()
        self.conn.commit()
        return item

    def close_spider(self):
        self.conn.close()
