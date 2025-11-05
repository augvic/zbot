from src.tasks.application.render_template.task import RenderTemplate
from src.components.infra.wsgi_application import WsgiApplication

class Main:
    
    def __init__(self,
        render_template_task: RenderTemplate
    ) -> None:
        self.render_template_task = render_template_task
        
    def register(self, app: WsgiApplication) -> None:
        try:
            @app.route("/", methods=["GET"])
            def render_application() -> str | tuple[dict[str, bool | str], int]:
                try:
                    response =  self.render_template_task.execute("main.html")
                    return response.data
                except Exception as error:
                    return {"success": False, "message": f"{error}"}, 500
        except Exception as error:
            print(f"❌ Error in (Main) route: {error}.")
