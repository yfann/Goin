import scrapy
from scrapy.contrib.spiders import CrawlSpider,Rule
import sys
reload(sys)
sys.setdefaultencoding('gbk')


class DoubanGPSpider(CrawlSpider):
    name="doubanGroup"
    allowed_domains=["dmoz.org"]
    start_urls=[
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self,response):
        filename=response.url.split("/")[-2]
        with open(filename,'wb') as f:
            f.write(response.body)