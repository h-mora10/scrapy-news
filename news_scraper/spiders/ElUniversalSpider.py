# coding=utf-8
import scrapy
from news_scraper.items import NewsScraperItem
from scrapy.selector import Selector


class ElUniversalSpider(scrapy.Spider):
    name = "eluniversalnews"
    allowed_domains = ["eluniversal.com.co"]

    start_urls = ['http://www.eluniversal.com.co/search/site/"ingeniero+de+sistemas"?page=%d' % page for page in xrange(0,16)]

    def parse(self, response):
        sel = Selector(response)
        articles = sel.select("//div[@class='result']")

        for article in articles:
            title = article.select("li[@class='search-result']/h3[@class='title']/a/text()").extract()
            description = article.select("li[@class='search-result']/ div[@class='search-snippet-info']/p[@¢lass='search-snippet']/text()")
            date = article.select("li[@class='search-result']/ div[@class='search-snippet-info']/p[@¢lass='search-info']/text()").extract()
            link = article.select("li[@class='search-result']/a/@href").extract()

            item = NewsScraperItem()
            item['title'] = title
            item['description'] = description
            item['date'] = date
            item['link'] = link

            yield item
