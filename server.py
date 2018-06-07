
from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    content = ''
    with open('data/index.html', 'r') as f:
        content = f.read()
    return [content.encode('utf-8')]


httpd = make_server('', 8000, application)
print('Serving HTTP on port http://localhost:8000')

httpd.serve_forever()
