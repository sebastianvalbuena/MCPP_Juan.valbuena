from scrapy.crawler import CrawlerProcess

from sigep.spiders.directory import DirectorySpider

process = CrawlerProcess()


class Crawler:
    @staticmethod
    def crawl_url(url, data):
        process.crawl(DirectorySpider, url, data)

    @staticmethod
    def start():
        process.start()
