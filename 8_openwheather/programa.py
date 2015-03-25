from bottle import Bottle,route,run,request
import requests
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
    r=requests.get('api.openweathermap.org/data/2.5/weather?q=%s&mode=xml&units=metric'%ciudad)
    if r.status_code = 200:
        return r.text

run(host='localhost', port=8080)

