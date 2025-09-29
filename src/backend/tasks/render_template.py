from src.backend.infrastructure.managers import TemplateManager

class RenderTemplate:
    
    def _setup(self) -> None:
        self.template_renderer = TemplateManager()
    
    def execute(self, template: str) -> str:
        self._setup()
        return self.template_renderer.render(template)
