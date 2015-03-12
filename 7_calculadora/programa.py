from bottle import Bottle,route,run,request,template,static_file
@route('/') 
def principal():
    return template("index.tpl")


@route('/calcular',method='POST') 
def calcular():
	n1=request.forms.get('num1')
	n2=request.forms.get('num2')
	op=request.forms.get('op')
	return template("calcular.tpl",numero1=n1,numero2=n2,ope=op)


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

run(host='localhost', port=8080)