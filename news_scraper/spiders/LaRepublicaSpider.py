# coding=utf-8
import scrapy
from news_scraper.items import NewsScraperItem
from scrapy.selector import Selector


class LaRepublicaSpider(scrapy.Spider):
    name = "larepublicanews"
    allowed_domains = ["larepublica.co"]
    start_urls = ['http://www.larepublica.co/search/content/"ingeniero+de+sistemas"?page=%d' % page for page in xrange(0,4)]

    def parse(self, response):
        sel = Selector(response)
        articles = sel.select("//li[@class='search-result']")
        for article in articles:
            title = article.select("h3[@class='title']/a/text()").extract()
            description = article.select("div[@class='search-snippet-info']/p[@class='search-snippet']/text()").extract()
            date = article.select("div[@class='search-snippet-info']/p[@class='search-info']/text()").extract()
            link = article.select("h3[@class='title']/a/@href").extract()

            item = NewsScraperItem()
            item['title'] = title
            item['description'] = description
            item['date'] = date
            item['link'] = link

            yield item
            #yield scrapy.Request(str(link), self.parse)

