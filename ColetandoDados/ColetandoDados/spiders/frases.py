import scrapy

class FrasesSpider(scrapy.Spider):
    name = 'frases'
    start_urls = ['https://quotes.toscrape.com']

    def parse(self, response):
        divs = response.css('.quote')
        #print(response.css('.quote'))

        for div in divs:
            frase = div.css('.text::text').get()
            autor = div.css('.author::text').get()
            tags = div.css('.tag::text').getall() #pegar todos os elementos
            yield{
                'frase': frase,
                'autor': autor,
                'tags': tags
            }
            spans = divs.css('span')
            for span in spans:
                print(span.css('span').get())


        