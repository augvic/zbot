from src.infrastructure.storage_managers.template_manager import TemplateManager
from datetime import datetime

class RenderTemplate:
    
    def _setup(self) -> None:
        self.template_renderer = TemplateManager()
    
    def execute(self, template: str) -> str:
        self._setup()
        try:
            return self.template_renderer.render(template)
        except Exception as error:
            print(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n{error}\n")
            return "Erro ao renderizar aplicação."
