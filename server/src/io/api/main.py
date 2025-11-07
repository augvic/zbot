from src.tasks.application.render_template.task import RenderTemplate
from src.tasks.application.route_registry import RouteRegistryTask

class Main:
    
    def __init__(self,
        render_template_task: RenderTemplate,
        route_registry_task: RouteRegistryTask
    ) -> None:
        self.render_template_task = render_template_task
        self.route_registry_task = route_registry_task
        
    def render_application(self) -> str | tuple[dict[str, bool | str], int]:
        try:
            response =  self.render_template_task.execute("main.html")
            return response.data
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500   
