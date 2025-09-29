from flask import Flask, request
from src.backend.tasks import ValidateLogin, VerifyIfLoggedIn

class Login:
    
    def __init__(self, app: Flask):
        self.app = app
        self.routes()
    
    def routes(self) -> None:
        @self.app.route("/login", methods=["POST"])
        def post_login() -> dict:
            data = request.json
            task = ValidateLogin()
            return task.execute(data)
        
        @self.app.route("/login", methods=["GET"])
        def get_login() -> dict:
            task = VerifyIfLoggedIn()
            return task.execute()