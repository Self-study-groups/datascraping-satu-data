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
        for i in range (1, 10):
            yield {
                'Tahun' : response.css('#example > tbody:nth-child(2) > tr:nth-child('+ str(i) +') > td:nth-child(1)::text').extract(),
                'Total' : response.css('#example > tbody:nth-child(2) > tr:nth-child('+ str(i) +') > td:nth-child(2)::text').extract(),
                'Migas' : response.css('#example > tbody:nth-child(2) > tr:nth-child('+ str(i) +') > td:nth-child(3)::text').extract(),
                'Non Migas' : response.css('#example > tbody:nth-child(2) > tr:nth-child('+ str(i) +') > td:nth-child(4)::text').extract(),
                'Agriculture' : response.css('#example > tbody:nth-child(2) > tr:nth-child('+ str(i) +') > td:nth-child(5)::text').extract(),
                'Industry' : response.css('#example > tbody:nth-child(2) > tr:nth-child('+ str(i) +') > td:nth-child(6)::text').extract(),
                'Mining' : response.css('#example > tbody:nth-child(2) > tr:nth-child('+ str(i) +') > td:nth-child(7)::text').extract(),
                'Others' : response.css('#example > tbody:nth-child(2) > tr:nth-child('+ str(i) +') > td:nth-child(8)::text').extract()
            }

##example > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1)
##example > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(1)