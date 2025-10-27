from src.tasks.render_template import RenderTemplate
from src.components.wsgi_application import WsgiApplication

class Main:
    
    def __init__(self, app: WsgiApplication) -> None:
        self.render_template_task = RenderTemplate()
        
        @app.route("/", methods=["GET"])
        def render_application() -> str:
            return self.render_template_task.execute("main.html")
