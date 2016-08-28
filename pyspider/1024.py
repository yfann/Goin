#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2016-08-28 11:03:17
# Project: cao

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }
    def __init__(self):
        self.baseUrl='http://aimeizi.ml/thread0806.php?fid=16&search=&page='
        self.page_num=1
        self.total_num=1

    @every(minutes=24 * 60)
    def on_start(self):
        while self.page_num<=self.total_num:
            url=self.baseUrl+str(self.page_num)
            print url
            self.crawl(url,callback=self.index_page)
            self.page_num+=1

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('.tr3.t_one').items():
            print each('h3 a').attr.href