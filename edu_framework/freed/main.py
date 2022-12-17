from .views import NotFound
from .middleware import middlewares


class Freed:

    def __init__(self, routes):
        self.routes = routes

    def __call__(self, environ, start_response):

        path = environ['PATH_INFO']
        if path in self.routes:
            view = self.routes[path]
        else:
            view = NotFound()
        request = {}

        # front controller
        for mw in middlewares:
            mw(request, environ)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return body
