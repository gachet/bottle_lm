from bottle import route, run

@route('/hello')
def hello():
    return "Hola mundo"

run(host='localhost', port=8080, debug=True)
