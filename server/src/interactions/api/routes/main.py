from src.tasks.render_template.render_template import RenderTemplate
from src.tasks.register_route import RegisterRoute

class Main:
    
    def __init__(self,
        render_template_task: RenderTemplate,
        register_route_task: RegisterRoute
    ) -> None:
        self.render_template_task = render_template_task
        register_route_task.main("/", ["GET"], self.render_application)
        
    def render_application(self) -> str | tuple[dict[str, bool | str], int]:
        try:
            response =  self.render_template_task.main("main.html")
            return response.data
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500   
