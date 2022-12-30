from wsgiref.simple_server import make_server

from freed.main import Freed
from edu_framework.urls import routes, fronts

app = Freed(routes, fronts)

with make_server('', 8000, app) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
