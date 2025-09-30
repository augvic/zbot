from flask import Flask, Response
from src.backend.tasks import SendTask

class TaskBundle:
    
    def __init__(self, app: Flask):
        self.app = app
        self.routes()
    
    def routes(self) -> None:
        @self.app.route("/task-bundle/<bundle>", methods=["GET"])
        def get_task_bundle(bundle: str) -> Response:
            task = SendTask()
            return task.execute(bundle)
