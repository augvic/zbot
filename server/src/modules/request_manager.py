from flask import request, Request

class RequestManager:
    
    def get_request(self) -> Request:
        try:
            return request
        except Exception as error:
            raise Exception(f"Error in (RequestManager) module in (get_request) method: {error}")
    
    def get_endpoint(self) -> str | None:
        try:
            return request.endpoint
        except Exception as error:
            raise Exception(f"Error in (RequestManager) module in (get_endpoint) method: {error}")
    
    def get_user_ip(self) -> str | None:
        try:
            return request.remote_addr
        except Exception as error:
            raise Exception(f"Error in (RequestManager) module in (get_user_ip) method: {error}")
