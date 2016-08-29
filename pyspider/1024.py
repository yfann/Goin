#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2016-08-28 11:03:17
# Project: cao

from pyspider.libs.base_handler import *
from pymongo import MongoClient

        
class Handler(BaseHandler):
    crawl_config = {
    }
    def __init__(self):
        self.baseUrl='http://aimeizi.ml/thread0806.php?fid=16&search=&page='
        self.page_num=1
        self.total_num=1
        self.store=MongoStore('mongodb://localhost:27017/')

    @every(minutes=24 * 60)
    def on_start(self):
        while self.page_num<=self.total_num:
            url=self.baseUrl+str(self.page_num)
            print url
            self.crawl(url,callback=self.index_page)
            self.page_num+=1

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):    
        results=[{"title":each('h3 a').text(),
         "url":each('h3 a').attr.href,
         "author":each('td:nth-child(3) a').text(),
         "authorUrl":each('td:nth-child(3) a').attr.href} for each in response.doc('.tr3.t_one').items()]
        self.store.insert_all(results)
        

        
class MongoStore(object):
    
    def __init__(self,connectionStr):
        self.client=MongoClient(connectionStr)
        self.db=self.client['caoDB']
        self.collection=self.db['dgrCol']
        
    def insert(self,obj):
        return self.collection.insert_one(obj).inserted_id
    
    def insert_all(self,objs):
        result=self.collection.insert_many(objs)
        return result.inserted_ids