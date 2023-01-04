#Vamos a crear un servidor local

import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app=FastAPI()

@app.get('/')
def get_list():
    return[1,2,3,4]

@app.get('/contact',response_class=HTMLResponse)
def get_list():
    return """
    <h1>Hello</h1>
    <p>ich bin Leonardo</p>
    """

def run():
    store.get_categories()

if __name__=="__main__":
    run()