# coding=utf-8
import scrapy
from news_scraper.items import NewsScraperItem
from scrapy.selector import Selector


class RevistaSemanaSpider(scrapy.Spider):
    name = "semananews"
    allowed_domains = ["semana.com"]
    #start_urls = ['http://www.semana.com/Buscador?query="ingeniero de sistemas"&post=semana&limit=10&offset=%d0' % page for page in xrange(0,3)]

    def parse(self, response):
        sel = Selector(response)
        articles = sel.select("//div[@class='medium-8 push-4 columns']")
        for article in articles:
            title = article.select("div[@class='row']/div[@class='large-12 columns']/div[@class='search-results']/div[@class='result']/div[@class='row']/div[@class='medium-8 columns result-content']/h2[@class='article-h']/a/text()").extract()
            description = article.select("div[@class='search-snippet-info']/p[@class='search-snippet']/text()").extract()
            date = article.select("div[@class='row']/div[@class='medium-8 columns result-content']/h6/span[@class='date right']/text()").extract()
            link = article.select("div[@class='row']/div[@class='large-12 columns']/div[@class='search-results']/div[@class='result']/div[@class='row']/div[@class='medium-8 columns result-content']/h2[@class='article-h']/a[@class='article-h-link']/@href").extract()

            item = NewsScraperItem()
            item['title'] = title
            item['description'] = description
            item['date'] = date
            item['link'] = link

            yield item
            #yield scrapy.Request(str(link), self.parse)

