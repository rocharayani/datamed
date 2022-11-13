import scrapy

class ArtigoSpider(scrapy.Spider):
    name = 'artigos'
    start_urls = ['https://www.scielo.br/j/csc/a/8pWRXdtnjTQ6cjWzZwmwKbB/?lang=en']

    def parse(self, response):
        divs = response.css('.articleSection')

        for div in divs:
            #print(div.css('p::text').get())
            artigo = div.css('p::text').get()
            yield{
                'artigo': artigo
            }






