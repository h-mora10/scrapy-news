# coding=utf-8
import scrapy
from news_scraper.items import NewsScraperItem
from scrapy.selector import Selector


class PortafolioSpider(scrapy.Spider):
    name = "portafolionews"
    allowed_domains = ["portafolio.co"]
    start_urls = ['http://www.portafolio.co/buscar?q=ingeniero+de+sistemas&page=%d' % page for page in xrange(1,27)]

    def parse(self, response):
        sel = Selector(response)
        articles = sel.select("//div[@class='listing-item  ']")
        articles.extend(sel.select("//div[@class='listing-item  listing-no-image']"))

        for article in articles:
            title = article.select("h3[@class='listing-title']/a/text()").extract()
            description = article.select("div[@class='listing-epigraph']/text()").extract()
            date = article.select("div[@class='listing-time']/div[@class='time']/text()").extract()
            link = "http://www.portafolio.co" + article.select("h3[@class='listing-title']/a/@href").extract()[0]

            item = NewsScraperItem()
            item['title'] = title
            item['description'] = description
            item['date'] = date
            item['link'] = link

            yield item
