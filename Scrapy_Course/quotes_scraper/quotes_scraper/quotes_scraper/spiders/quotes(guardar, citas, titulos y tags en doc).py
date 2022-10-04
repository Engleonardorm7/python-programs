# import scrapy

# #Titulo=//h1/a/text()
# #Citas=//span[@class="text"and @itemprop="text"]/text()
# #Top ten tags= //div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()



# class QuotesSpider(scrapy.Spider):
#     name='quotes'
#     start_urls=[
#         'http://quotes.toscrape.com/'
#     ]

#     def parse(self,response):#analizar un archivo para extraer informacion valiosa
#         print('*'*10)
#         print('\n\n\n')

#         title=response.xpath('//h1/a/text()').get()
#         print(f'Titulo: {title}')
#         #print(response.status, response.headers)
#         print('\n\n')
        
#         quotes=response.xpath('//span[@class="text"and @itemprop="text"]/text()').getall()
#         print('citas: ')
#         for quote in quotes:
#             print(f'- {quote}')
#         print('\n\n')

#         top_ten_tags=response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()
#         print('Top Ten Tags: ')
#         for tag in top_ten_tags:
#             print(f'-{tag}')
#         print('\n\n')

#         print('\n\n\n')
#         print('*'*10)
#------------------------------------------------------------------------------------------
# 
# 
# 
import scrapy

#Titulo=//h1/a/text()
#Citas=//span[@class="text"and @itemprop="text"]/text()
#Top ten tags= //div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()



class QuotesSpider(scrapy.Spider):
    name='quotes'
    start_urls=[
        'http://quotes.toscrape.com/'
    ]

    def parse(self,response):#analizar un archivo para extraer informacion valiosa
        

        title=response.xpath('//h1/a/text()').get()
        quotes=response.xpath('//span[@class="text"and @itemprop="text"]/text()').getall()
        top_ten_tags=response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()
        
        yield {
            'title' : title,
            'quotes' : quotes,
            'top_ten_tags' : top_ten_tags
        }