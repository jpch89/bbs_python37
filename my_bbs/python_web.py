from wsgiref.simple_server import make_server


def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [b'Hello World!\n']

# 创建 WSGI 服务器，绑定端口号，并指定调用的 application
httpd = make_server('127.0.0.1', 8000, application)
# 处理一次请求之后退出
httpd.handle_request()
