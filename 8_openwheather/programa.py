# -*- coding: utf-8 -*-
from bottle import Bottle,route,run,request
import requests
from lxml import etree

@route('/') 
def login():
    return '''
        <form action="/tiempo" method="post">
            Ciudad: <input name="ciudad" type="text" />
            <br/>
            <input value="Login" type="submit" />
        </form>'''

@route('/tiempo',method='POST') 
def calcula_tiempo():
    ciudad = request.forms.get('ciudad')
    print ciudad
    r=requests.get('http://api.openweathermap.org/data/2.5/weather?q=%s&mode=xml&units=metric'%ciudad)
    print r
    if r.status_code == 200:
        doc = etree.fromstring(r.text.encode ('utf-8'))
          
        
        temp=doc.find("temperature").attrib["value"]
        return temp+" ºC"

run(host='localhost', port=8080)

