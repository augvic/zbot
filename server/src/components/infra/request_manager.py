from flask import request, Request

class RequestManager:
    
    def get_request(self) -> Request:
        return request
