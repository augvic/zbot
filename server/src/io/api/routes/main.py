from src.tasks.application.render_template.task import RenderTemplate
from src.components.infra.wsgi_application import WsgiApplication
from src.tasks.application.render_template.models import Response

class Main:
    
    def __init__(self, app: WsgiApplication) -> None:
        self.render_template_task = RenderTemplate()
        
        @app.route("/", methods=["GET"])
        def render_application() -> str | dict[str, bool | str]:
            try:
                response =  self.render_template_task.execute("main.html")
                return response.data
            except Exception as error:
                return {"success": False, "message": f"{error}"}
