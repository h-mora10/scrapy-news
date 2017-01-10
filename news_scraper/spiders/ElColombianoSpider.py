# coding=utf-8
import scrapy
from news_scraper.items import NewsScraperItem
from scrapy.selector import Selector


class ElColombianoSpider(scrapy.Spider):
    name = "elcolombianonews"
    allowed_domains = ["elcolombiano.com"]

    start_urls = ['http://www.elcolombiano.com/busqueda/-/search/"ingeniero+de+sistemas"/false/true/20040101/20141231/date/true/true/0/0/meta/0/0/5/%d' % page for page in xrange(0,33)]

    def parse(self, response):
        sel = Selector(response)
        articles = sel.select("//div[@class='noticia-resultado']")


#confoto
        for article in articles:
            description = article.select("div[@class='right']/a/p/text()").extract()
            title = article.select("div[@class='right']/a/h3[@class='titulo-noticia']/text()").extract()
            date = article.select("div[@class='left']/div[@class='fecha']/span/text()").extract()
            link = "http://www.elcolombiano.com" + article.select("div[@class='right']/a/@href").extract()[0]
            item = NewsScraperItem()
            item['title'] = title
            item['description'] = description
            item['date'] = date
            item['link'] = link

            yield item
#sinfoto
#for article in articles:
 #   description = article.select("div[@class='rightNoFoto']/a/p/text()").extract()
  #  title = article.select("div[@class='rightNoFoto']/a/h3[@class='titulo-noticia']/text()").extract()
   # date = article.select("div[@class='left']/div[@class='fechaNoFoto']/span/text()").extract()
#    link = "http://www.elcolombiano.com" + article.select("div[@class='rightNoFoto']/a/@href").extract()[0]
 #   item = NewsScraperItem()
  #  item['title'] = title
   # item['description'] = description
#    item['date'] = date
 #   item['link'] = link
  #  yield item