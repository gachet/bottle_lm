from bottle import Bottle,route,run,request,template
@route('/hello')
@route('/hello/<name>')
def hello(name='World'):
    return template('hello_template.tpl', nombre=name)



run(host='0.0.0.0', port=8080)

