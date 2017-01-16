# coding=utf-8
import scrapy
from news_scraper.items import NewsScraperItem
from scrapy.selector import Selector


class ElUniversalSpider(scrapy.Spider):
    name = "eluniversalnews"
    allowed_domains = ["eluniversal.com.co"]
    start_urls = ['http://www.eluniversal.com.co/search/site/"ingeniero de sistemas"?page=%d' % page for page in xrange(0,15)]

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

