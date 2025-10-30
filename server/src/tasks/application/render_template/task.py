from src.components.infra.template_manager import TemplateManager
from src.components.file_system.log_system import LogSystem
from src.components.infra.session_manager import SessionManager
from .models import Response

class RenderTemplate:
    
    def __init__(self) -> None:
        self.template_renderer = TemplateManager()
        self.log_system = LogSystem("application/render_template")
        self.session_manager = SessionManager()
    
    def execute(self, template: str) -> Response:
        try:
            template_return = self.template_renderer.render(template)
            self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n✅ Template coletado.")
            return Response(success=True, message="✅ Template coletado.", data=template_return)
        except Exception as error:
            self.log_system.write_error(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n❌ Erro:\n{error}")
            raise Exception("❌ Erro interno ao retornar template. Contate o administrador.")
