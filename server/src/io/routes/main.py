from flask import Flask
from src.tasks.render_template import RenderTemplate

class Main:
    
    def __init__(self, app: Flask) -> None:
        
        @app.route("/", methods=["GET"])
        def render_application() -> str:
            task = RenderTemplate()
            return task.execute("main.html")
