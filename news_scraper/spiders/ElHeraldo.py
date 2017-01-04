# coding=utf-8
import scrapy
from news_scraper.items import NewsScraperItem
from scrapy.selector import Selector


class ElTiempoSpider(scrapy.Spider):
    name = "elherladonews"
    allowed_domains = ["elheraldo.co"]
    start_urls = ['http://www.elheraldo.co/search?keyword="ingeniero+de+sistemas"&type=']

    def parse(self, response):
        sel = Selector(response)
        articles = sel.select("//div[@class='content']")
        for article in articles:
            title = article.select("div[@class='titulo']/h2/a/text()").extract()
            description = article.select(
                "div[@class='descripcion']/p/text()").extract()
            date = article.select("div[@class='detail']/div[@class='postdate']/text()").extract()
            link = article.select("div[@class='titulo']/h2/a/@href").extract()

            item = NewsScraperItem()
            item['title'] = title
            item['description'] = description
            item['date'] = date
            item['link'] = link

            yield item
