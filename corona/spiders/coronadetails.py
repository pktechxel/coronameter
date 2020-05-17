# -*- coding: utf-8 -*-
import scrapy


class CoronadetailsSpider(scrapy.Spider):
    name = 'coronadetails'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['http://www.worldometers.info/coronavirus/']

    def parse(self, response):
        tables=response.xpath("(//table[@id='main_table_countries_today']/tbody)[1]/tr")
        for table in tables:
            yield{
                
                'Sl': table.xpath(".//td[1]/text()").get(),
                'Country': table.xpath(".//td[2]/a/text()").get(),
                'Total Cases': table.xpath(".//td[3]/text()").get(),
                'New Cases': table.xpath(".//td[4]/text()").get(),
                'Total Deaths': table.xpath(".//td[5]/text()").get(),
                'New Deaths': table.xpath(".//td[6]/text()").get(),
                'Total Recovered': table.xpath(".//td[7]/text()").get(),
                'Active Cases': table.xpath(".//td[8]/text()").get(),
                'Serious Cases': table.xpath(".//td[9]/text()").get(),
                'Total Cases/1M Pop': table.xpath(".//td[10]/text()").get(),
                'Deaths/1M Pop': table.xpath(".//td[11]/text()").get(),
                'Total Tests': table.xpath(".//td[12]/text()").get(),
                'Tests/1M Pop': table.xpath(".//td[13]/text()").get(),
                'Population': table.xpath(".//td[14]/text()").get()                
            }

