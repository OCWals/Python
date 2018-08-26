# -*- conding: utf8 -*-
import scrapy

class BlogSpider(scrapy.Spider):
    name = 'diplomaticSpider'
    start_urls = ['https://fr.wikipedia.org/wiki/Plaque_diplomatique_en_France']

    def parse(self, response):
        i = 0
        for link in response.css('div.colonnes li'):
            i=i+1
            yield {
            	'N°': i,
            	'Pays': link.css('li ::text').extract_first()
            }
