import pyautogui
import scrapy
#from key import password, user


# pyautogui.sleep(5)
# pyautogui.write(['f6'])

# link ='https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Faccounts.google.com%2Fo%2Fsaml2%2Fidp%3Ffrom_login%3D1%26zt%3DChRwMnVOT0x2VGVDYXRVeHlULVdCYxIfSTlBSnVTeWo3b3dRd0ktM2lWMU9TaWRYTldmLU9oZw%25E2%2588%2599AD98QVYAAAAAY0DH4_6QGRtrUm_1AyEgEQdOJ_lp-rdK%26as%3DUiBkT26KiCGb_CowTLBrVgOjG09IzqF-1QEGHhtLkZU&followup=https%3A%2F%2Faccounts.google.com%2Fo%2Fsaml2%2Fidp%3Ffrom_login%3D1%26zt%3DChRwMnVOT0x2VGVDYXRVeHlULVdCYxIfSTlBSnVTeWo3b3dRd0ktM2lWMU9TaWRYTldmLU9oZw%25E2%2588%2599AD98QVYAAAAAY0DH4_6QGRtrUm_1AyEgEQdOJ_lp-rdK%26as%3DUiBkT26KiCGb_CowTLBrVgOjG09IzqF-1QEGHhtLkZU&ltmpl=popup&oauth=1&faa=1&sarp=1&scc=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'

# pyautogui.typewrite(link)
# pyautogui.typewrite('\n')

# pyautogui.sleep(5)
# pyautogui.typewrite('technology01')
# pyautogui.hotkey('altright','q')
    
# pyautogui.sleep(1)
# pyautogui.typewrite('mbs.edu.co')
# pyautogui.typewrite('\n')
# pyautogui.sleep(5)
# pyautogui.typewrite('21665454408987')
# pyautogui.sleep(2)
# pyautogui.hotkey('altright','q')
# pyautogui.sleep(2)
# pyautogui.typewrite('l')
# pyautogui.sleep(2)
# pyautogui.typewrite('\n')
# pyautogui.sleep(5)
# pyautogui.write(['f6'])

# link ='https://virtualmbs.instructure.com/courses/1348/gradebook'
# pyautogui.typewrite(link)
# pyautogui.typewrite('\n')

#.........intento 2
# import requests
# from bs4 import BeautifulSoup

# client = requests.Session()
# html=client.get('https://virtualmbs.instructure.com/courses/1348/gradebook').content
# soup=BeautifulSoup(html,'html.parser')
# print(soup.find("button",attrs={"jsname":"Cuz2Ue"}))

# login_information={
#     'email':'technology01@mbs.edu.co'
# }

# client.post('https://virtualmbs.instructure.com/courses/1348/gradebook', data=login_information)

from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
import os

class QuotesSpider(Spider):
    name='gradeswith'
    starts_urls=['https://virtualmbs.instructure.com/courses/1348/gradebook']

def parse(self, response):
    yield FormRequest(url=self.start_urls[0], formdata={'txtEmail': os.environ.get('technology01@mbs.edu.co'), 'txtPassword': os.environ.get('21665454408987@l')}, callback=self.scrape_ftse100_page)






# class QuotesSpider(scrapy.Spider):
#     name='grades'
#     start_urls={
#         'https://virtualmbs.instructure.com/courses/1348/gradebook'
#     }

#     custom_settings = {
#         'FEEDS': {
#             'grades.json': {
#                 'format': 'json',
#                 'encoding': 'utf-8',
#                 'indent': 4,
#             }
#         },
#         'ROBORSTXT_OBEY': True,
#     }

# def parse(self,response):
#     grades=response.xpath('//div[@class="viewport_1 slick-viewport"]//div[@class="Grid__GradeCell__Content"]/span[@class="Grade"]/text()').getall()
#     students=response.xpath('//div[@class="viewport_0 slick-viewport"]//a[@class="student-grades-link student_context_card_trigger"]/text()').getall()

#     yield {
#         'student' : students,
#         'Grade' : grades
        
#     }