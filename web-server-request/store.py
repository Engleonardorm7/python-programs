import requests

def get_categories():
    r=requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    categories=r.json() #transforma el string en una lista
    for category in categories:
        print(category["name"])