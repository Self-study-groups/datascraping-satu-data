import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://satudata.kemendag.go.id/data-informasi/perdagangan-luar-negeri/ekspor-impor',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for i in range(1, 10):
            yield {
                'Tahun': response.css(
                    '#impor > tbody:nth-child(2) > tr:nth-child(' + str(i) + ') > td:nth-child(1)::text').extract(),
                'Total': response.css(
                    '#impor > tbody:nth-child(2) > tr:nth-child(' + str(i) + ') > td:nth-child(2)::text').extract(),
                'Consumption Goods': response.css(
                    '#impor > tbody:nth-child(2) > tr:nth-child(' + str(i) + ') > td:nth-child(3)::text').extract(),
                'Raw Material Support': response.css(
                    '#impor > tbody:nth-child(2) > tr:nth-child(' + str(i) + ') > td:nth-child(4)::text').extract(),
                'Capital Goods': response.css(
                    '#impor > tbody:nth-child(2) > tr:nth-child(' + str(i) + ') > td:nth-child(5)::text').extract(),
            }

#  #impor > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1)
# #impor > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(1)
