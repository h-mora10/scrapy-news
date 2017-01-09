# coding=utf-8
import scrapy
from news_scraper.items import NewsScraperItem
from scrapy.selector import Selector


class SemanaSpider(scrapy.Spider):
    name = "semananews"
    allowed_domains = ["semana.com"]
    start_urls = ['http://www.semana.com/Buscador?query="ingeniero%20de%20sistemas"&post=semana&limit=10&offset=%d0' % page for page in xrange(0,104)]

    def parse(self, response):
        sel = Selector(response)
        articles = sel.xpath("//div[@class='result']")


        for article in articles:
            title = article.select("div[@class='row']/div[@class='medium-8 columns result-content']/h2[@class='article-h']/a[@class='article-h-link']/text").extract()
            description = article.select("div[@class='row']/div[@class='medium-8 columns result-content']/p[@class='result-intro']/text").extract()
            date = article.select("div[@class='row']/div[@class='medium-8 columns result-content']/h6/span[@class='date right']/text").extract()
            link =  article.select("div[@class='row']/div[@class='medium-8 columns result-content']/h2[@class='article-h']/a[@class='article-h-link']/@href").extract()

            item = NewsScraperItem()
            item['title'] = title
            item['description'] = description
            item['date'] = date
            item['link'] = link

            yield item
