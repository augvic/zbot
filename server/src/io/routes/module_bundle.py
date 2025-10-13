from flask import Flask, Response
from src.tasks.send_module import SendModule
from src.tasks.verify_if_have_access import VerifyIfHaveAccess

class ModuleBundle:
    
    def __init__(self, app: Flask) -> None:
        
        @app.route("/module-bundle/<module>", methods=["GET"])
        def send_module(module: str) -> Response | str | tuple[str, int]:
            task1 = VerifyIfHaveAccess()
            task2 = SendModule()
            if not task1.execute(module):
                return "Sem autorização.", 401
            return task2.execute(module)
