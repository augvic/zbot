from flask import request, Request

class RequestManager:
    
    def get_request(self) -> Request:
        return request
    
    def get_endpoint(self) -> str | None:
        return request.endpoint
    
    def get_user_ip(self) -> str | None:
        return request.remote_addr