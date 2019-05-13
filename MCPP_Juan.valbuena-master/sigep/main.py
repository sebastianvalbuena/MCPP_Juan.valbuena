# -*- coding: utf-8 -*-

from plotter.pandas import Pandas
from sigep.crawler import Crawler
from sigep.utils.url_utils import UrlUtils
from utils.utils import Utils


def get_urls(codes):
    urls = {}
    for location in codes:
        urls[location] = UrlUtils.get_url_by_entity(codes[location])
    return urls


def main():
    directory = {}
    crawler = Crawler()
    pandas = Pandas()

    codes = Utils.get_codes()
    urls = get_urls(codes)

    for location in codes:
        data = {location: [[], [], []]}
        crawler.crawl_url(urls[location], data[location])
        directory[location] = data[location]

    crawler.start()
    pandas.plot_directory(directory)


main()