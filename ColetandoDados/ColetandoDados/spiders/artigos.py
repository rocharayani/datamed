import scrapy

class ArtigoSpider(scrapy.Spider):
    name = 'artigos'
    start_urls = ['https://www.sanarmed.com/artigos-cientificos/oleo-de-cartamo-carthamus-tinctorius-aumenta-os-niveis-de-colesterol-total-e-ldl-colesterol-em-modelo-experimental-de-sindrome-metabolica']

    def parse(self, response):
        divs = response.css('.section')
        #print(response.css('.section').get())

        for div in divs:
            paragrafo = response.css('p*')
            print(paragrafos)

          #  paragrafo = div.css('.text::text').get()
          #  autor = div.css('.author::text').get()
           # tags = div.css('.tag::text').getall() #pegar todos os elementos
            #yield{
             #   'frase': frase,
              #  'autor': autor,
               #'tags': tags
            #}