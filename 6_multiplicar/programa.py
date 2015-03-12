from bottle import Bottle,route,run,request,template,static_file
@route('/tabla/<num>')
def tabla(num):
    return template('template_tabla.tpl', numero=num)

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

run(host='0.0.0.0', port=8080)


