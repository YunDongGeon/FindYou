# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql.cursors

class FindyoucrawlPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect('localhost', 'root', '1234', 'findyou')
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        # create record if doesn't exist.
        self.cursor.execute(
            "insert into 11st(cat, title, price, delivery, img, detail) values (%s, %s, %s, %s, %s, %s)",
            (item['elevenSt_cat'],
             item['elevenSt_title'],
             item['elevenSt_price'],
             item['elevenSt_del'],
             item['elevenSt_img'],
             item['elevenSt_url']))
        self.conn.commit()
        return item
    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()
