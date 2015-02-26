from bottle import route, run

@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
    return 'Hello %s, how are you?'%name

run(host='localhost', port=8080, debug=True)
