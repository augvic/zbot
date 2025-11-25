from src.tasks.application.render_template.task import RenderTemplate

class Main:
    
    def __init__(self,
        render_template_task: RenderTemplate
    ) -> None:
        self.render_template_task = render_template_task
        
    def render_application(self) -> str | tuple[dict[str, bool | str], int]:
        try:
            response =  self.render_template_task.main("main.html")
            return response.data
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500   
