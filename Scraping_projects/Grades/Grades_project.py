import requests 
import lxml.html as html
import os

HOME_URL='https://virtualmbs.instructure.com/courses/1348/gradebook'
GRADES='//div[@class="viewport_1 slick-viewport"]//div[@class="Grid__GradeCell__Content"]/span[@class="Grade"]/text()'
STUDENTS='//div[@class="viewport_0 slick-viewport"]//a[@class="student-grades-link student_context_card_trigger"]/text()'
def parse_home():
    try:
        response=requests.get(HOME_URL)
        if response.status_code ==200:
            home=response.content.decode('utf-8')
            parsed=html.fromstring(home)
            links_to_notices=parsed.xpath(STUDENTS)

            for i in links_to_notices:
                print(i)

           
        else:
            raise ValueError(f'Error:{response.status_code}')
    except ValueError as ve:
        print(ve)
        

def run():
    parse_home()

if __name__=="__main__":
    run()