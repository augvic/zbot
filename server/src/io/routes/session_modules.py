from flask import Flask

class ModulesAllowed:
    
    def __init__(self, app: Flask):
        self.app = app
        self.routes()
    
    def routes(self) -> None:
        @self.app.route("/session-modules", methods=["GET"])
        def get_session_modules() -> dict:
            if not self.session_manager.is_user_in_session():
                return "Faça login.", 401
            return self.session_manager.get_from_session("session_modules")
