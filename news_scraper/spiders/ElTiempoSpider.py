# coding=utf-8
import scrapy
from news_scraper.items import NewsScraperItem
from scrapy.selector import Selector


class ElTiempoSpider(scrapy.Spider):
    name = "eltiemponews"
    allowed_domains = ["eltiempo.com"]
    start_urls = ['http://www.eltiempo.com/archivo/buscar?q="ingeniería+de+sistemas"&producto=eltiempo&orden=antigua&pagina=%s&a=2004' % page for page in xrange(1,101)]

    def parse(self, response):
        sel = Selector(response)
        articles = sel.select("//article")
        for article in articles:
            title = article.select("h2/a/text()").extract()
            description = article.select("p/a/text()").extract()
            date = article.select("time/text()").extract()
            link = article.select("h2/a/@href").extract()

            item = NewsScraperItem()
            item['title'] = title
            item['description'] = description
            item['date'] = date
            item['link'] = link

            yield item
            #yield scrapy.Request(str(link), self.parse)
