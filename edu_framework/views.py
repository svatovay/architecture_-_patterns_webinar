from edu_framework.freed.templator import render


class _BaseSuccessView:
    def __init__(self):
        self.response = None

    def __call__(self, request):
        return '200 OK', [self.response]


class Index(_BaseSuccessView):
    def __call__(self, request):
        self.response = bytes(render('index.html', **request), 'UTF-8')
        return '200 OK', [self.response]


class About(_BaseSuccessView):
    def __init__(self):
        self.response = bytes(render('about.html'), 'UTF-8')


class NotFound:
    def __init__(self):
        self.response = b'404 PAGE Not Found'

    def __call__(self, request):
        return '404 WHAT', [self.response]
