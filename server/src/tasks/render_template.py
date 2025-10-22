from src.components.template_manager import TemplateManager
from datetime import datetime

class RenderTemplate:
    
    def __init__(self) -> None:
        self.template_renderer = TemplateManager()
    
    def execute(self, template: str) -> str:
        try:
            return self.template_renderer.render(template)
        except Exception as error:
            print(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n{error}\n")
            return "Erro ao renderizar aplicação."
