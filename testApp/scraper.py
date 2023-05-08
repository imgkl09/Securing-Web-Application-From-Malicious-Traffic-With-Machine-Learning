import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quote-spdier'
    start_urls = ['http://localhost:3000/']