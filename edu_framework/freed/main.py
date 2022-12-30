from quopri import decodestring
from .fr_request import PostRequests, GetRequests
from edu_framework.views import NotFound
from .middleware import middlewares


class Freed:

    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        request = {}

        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'POST':
            data = PostRequests().get_request_params(environ)
            request['data'] = Freed.decode_value(data)
            print(f"Содержимое POST: {request['data']}")
        if method == 'GET':
            request_params = GetRequests().get_request_params(environ)
            request['request_params'] = Freed.decode_value(request_params)
            print(f"Содержимое GET: {request['request_params']}")

        path = environ['PATH_INFO']
        if path in self.routes:
            view = self.routes[path]
        else:
            view = NotFound()

        # front controller
        for front in self.fronts:
            front(request)

        # middleware
        for mw in middlewares:
            mw(request, environ)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return body

    @staticmethod
    def decode_value(data):
        decode_data = {}
        for k, v in data.items():
            value = bytes(v.replace('%', '=').replace('+', ' '), 'UTF-8')
            decode_value = decodestring(value).decode('UTF-8')
            decode_data[k] = decode_value
        return decode_data
