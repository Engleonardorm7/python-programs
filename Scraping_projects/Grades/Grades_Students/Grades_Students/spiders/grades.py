import scrapy

class QuotesSpider(scrapy.Spider):
    name='grades'
    start_urls={
        'https://virtualmbs.instructure.com/courses/1348/gradebook'
    }

    custom_settings={
        'FEED_URI': 'quotes.json',
        'FEED_FORMAT': 'json',
        #configuraciones adicionales para mejorar
        'CONTURRENT_REQUESTS': 24,
        'MEMUSAGE_LIMIT_MB': 2048,
        'MEMUSAGE_NOTIFY_MAIL':['leonardorm7@hotmail.com'],
        'ROBORSTXT_OBEY': False,
        'USER_AGENT': 'Leonardo Rodriguez',
        'FEED_EXPORT_ENCODING': 'utf-8'

    }

def parse(self,response):
    grades=response.xpath('//div[@class="viewport_1 slick-viewport"]//div[@class="Grid__GradeCell__Content"]/span[@class="Grade"]/text()').getall()
    students=response.xpath('//div[@class="viewport_0 slick-viewport"]//a[@class="student-grades-link student_context_card_trigger"]/text()').getall()

    yield {
        'student' : students,
        'Grade' : grades
        
    }