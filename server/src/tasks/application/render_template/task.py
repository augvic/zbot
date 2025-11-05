from src.components.infra.template_manager import TemplateManager
from src.components.file_system.log_system import LogSystem
from src.components.infra.request_manager import RequestManager
from .models import Response

class RenderTemplate:
    
    def __init__(self,
        template_renderer: TemplateManager,
        log_system: LogSystem,
        request_manager: RequestManager
    ) -> None:
        self.template_renderer = template_renderer
        self.log_system = log_system
        self.request_manager = request_manager
    
    def execute(self, template: str) -> Response:
        try:
            template_return = self.template_renderer.render(template)
            self.log_system.write_text(f"👤 Pelo IP ({self.request_manager.get_user_ip()}): ✅ Template coletado.")
            return Response(success=True, message="✅ Template coletado.", data=template_return)
        except Exception as error:
            self.log_system.write_error(f"👤 Pelo IP ({self.request_manager.get_user_ip()}): ❌ Erro: {error}.")
            raise Exception("❌ Erro interno ao retornar template. Contate o administrador.")
