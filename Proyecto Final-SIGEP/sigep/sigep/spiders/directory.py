# -*- coding: utf-8 -*-

import scrapy
from scrapy import Request

from utils.string_utils import StringUtils


class DirectorySpider(scrapy.Spider):
    name = 'directory'

    custom_settings = {
        'LOG_LEVEL': 'INFO'
    }

    person_css = '.columna-datos a::attr(href)'
    next_page_css = '.next a::attr(href)'

    title_css = '.cargo_funcionario::text'
    studies_css = '.zona_directorio_detail > ul > li:first-child::text'
    birthplace_xpath = '//span[contains(text(),"Municipio de Nacimiento:")]/following-sibling::span/text()'

    def __init__(self, urls, data, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [urls]
        self.data = data

    def parse(self, response):
        for item in response.css(self.person_css).getall():
            yield Request(item, callback=self.filter_person)

        next_page = response.css(self.next_page_css).get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield Request(next_page, callback=self.parse)
        pass

    @staticmethod
    def clean(text):
        text = StringUtils.get_monospaced_text(text)
        text = StringUtils.get_titled_text(text)
        text = StringUtils.get_no_accent_text(text)
        return text

    def get_title(self, response):
        title = str(response.css(self.title_css).get())
        title = StringUtils.get_text_without_digits(title)
        return self.clean(title)

    def get_studies(self, response):
        studies = str(response.css(self.studies_css).get())
        if studies == 'None':
            studies = 'No Reportado'
        studies = StringUtils.get_text_without_dashes(studies)
        return self.clean(studies)

    def get_birthplace(self, response):
        birthplace = str(response.xpath(self.birthplace_xpath).get())
        if birthplace == ', - ':
            birthplace = 'No Reportado'
        return self.clean(birthplace)

    def filter_person(self, response):
        self.data[0].append(self.get_title(response))
        self.data[1].append(self.get_studies(response))
        self.data[2].append(self.get_birthplace(response))
        pass
