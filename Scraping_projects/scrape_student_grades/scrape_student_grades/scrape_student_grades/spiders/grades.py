import scrapy

class QuotesSpider(scrapy.Spider):
    name='grades'
    start_urls={
        'https://virtualmbs.instructure.com/courses/1348/gradebook'
    }

    custom_settings = {
        'FEEDS': {
            'grades.json': {
                'format': 'json',
                'encoding': 'utf-8',
                'indent': 4,
            }
        },
        'ROBORSTXT_OBEY': True,
    }

def parse(self,response):
    grades=response.xpath('//div[@class="viewport_1 slick-viewport"]//div[@class="Grid__GradeCell__Content"]/span[@class="Grade"]/text()').getall()
    students=response.xpath('//div[@class="viewport_0 slick-viewport"]//a[@class="student-grades-link student_context_card_trigger"]/text()').getall()

    yield {
        'student' : students,
        'Grade' : grades
        
    }