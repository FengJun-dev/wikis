import psycopg2

from wikis.settings import DATABASES


class WikisPipeline(object):
    def __init__(self):
        self.conn = psycopg2.connect(**DATABASES)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        title = item['title']
        content = item['content']
        comment = item['comment']
        page = item['page']
        main_category = item['main_category']
        category = item['category']
        sql = ""
        self.cursor.execute(sql, (title, content, comment, page, main_category, category))
        self.conn.commit()
        return item

    def close_spider(self):
        self.conn.close()
