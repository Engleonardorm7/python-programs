import scrapy

#Titulo=//h1/a/text()
#Citas=//span[@class="text"and @itemprop="text"]/text()
#Top ten tags= //div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()
#next page button = //ul[@class="pager"]//li[@class="next"]/a/@href
#Author = //div[@class="row"]//small[@class="author"]/text()


class QuotesSpider(scrapy.Spider):
    name='quotes'
    start_urls=[
        'http://quotes.toscrape.com/'
    ]
#se configura el programa para que genere un archivo tipo json 
#con los resultados del programa
    custom_settings={
        'FEED_URI': 'quotes.json',
        'FEED_FORMAT': 'json',
        #configuraciones adicionales para mejorar
        'CONTURRENT_REQUESTS': 24,
        'MEMUSAGE_LIMIT_MB': 2048,
        'MEMUSAGE_NOTIFY_MAIL':['leonardorm7@hotmail.com'],
        'ROBORSTXT_OBEY': True,
        'USER_AGENT': 'Leonardo Rodriguez',
        'FEED_EXPORT_ENCODING': 'utf-8'

    }

    def parse_only_quotes(self, response, **kwargs):
        if kwargs:
            quotes = kwargs['quotes']
            author = kwargs['author']
        quotes.extend(response.xpath('//span[@class="text"and @itemprop="text"]/text()').getall())
        author.extend(response.xpath('//div[@class="row"]//small[@class="author"]/text()').getall())
        next_page_button_link=response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link,callback=self.parse_only_quotes, cb_kwargs={'quotes':quotes,'author':author})
        else:
            yield {
                'quotes': list(zip(quotes, author))
            }

    def parse(self,response):#analizar un archivo para extraer informacion valiosa
        

        title=response.xpath('//h1/a/text()').get()
        quotes=response.xpath('//span[@class="text"and @itemprop="text"]/text()').getall()
        author=response.xpath('//div[@class="row"]//small[@class="author"]/text()').getall()
        top_tags=response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()
        
        top = getattr(self,'top',None)
        if top:
            top=int(top)
            top_tags=top_tags[:top]


        yield {
            'title' : title,
            'top_tags' : top_tags
        }

        next_page_button_link=response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link,callback=self.parse_only_quotes, cb_kwargs={'quotes':quotes,'author':author})