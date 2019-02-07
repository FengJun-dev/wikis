# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2

from wikis.settings import DATABASES


class WikisPipeline(object):

    def process_item(self, item, spider):
        conn = psycopg2.connect(**DATABASES)
        return item
