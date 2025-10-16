from flask import Flask
from src.tasks.render_template import RenderTemplate

class Main:
    
    def __init__(self, app: Flask) -> None:
        self.render_template_task = RenderTemplate()
        
        @app.route("/", methods=["GET"])
        def render_application() -> str:
            return self.render_template_task.execute("main.html")
