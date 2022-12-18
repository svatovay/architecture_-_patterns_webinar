class GetRequests:

    @staticmethod
    def parse_input_data(data: str) -> dict:
        result = {}
        if data:
            pairs = data.split('&')
            for pair in pairs:
                k, v = pair.split('=')
                result[k] = v
        return result

    @staticmethod
    def get_request_params(environ: dict) -> dict:
        query_str = environ['QUERY_STRING']
        request_params = GetRequests.parse_input_data(query_str)
        return request_params


class PostRequests:

    @staticmethod
    def parse_input_data(data: str) -> dict:
        result = {}
        if data:
            pairs = data.split('&')
            for pair in pairs:
                k, v = pair.split('=')
                result[k] = v
        return result

    @staticmethod
    def get_request_body(environ: dict) -> bytes:
        content_length_str = environ.get('CONTENT_LENGTH')
        content_length = int(content_length_str) if content_length_str else 0
        data = environ['wsgi.input'].read(content_length) if content_length else b''
        return data

    def parse_request_body(self, data: bytes) -> dict:
        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            result = self.parse_input_data(data_str)
        return result

    def get_request_params(self, environ: dict) -> dict:
        query_str = self.get_request_body(environ)
        request_params = self.parse_request_body(query_str)
        return request_params
