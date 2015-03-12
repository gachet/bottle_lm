from bottle import Bottle,route,run,request,template
@route('/tabla/<num>')
def tabla(num):
    return template('template_tabla.tpl', numero=num)

run(host='0.0.0.0', port=8080)


