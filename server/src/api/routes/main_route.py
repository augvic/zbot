from src.engines.engines import Engines

class MainRoute:
    
    def __init__(self, engines: Engines) -> None:
        self.engines = engines
        self.engines.wsgi_engine.register_route("/", ["GET"], self.render_application)
        
    def render_application(self) -> str | tuple[dict[str, bool | str], int]:
        try:
            return self.engines.wsgi_engine.render_template("main.html")
        except Exception as error:
            self.engines.log_engine.write_error("api/main_route", f"❌ Error in (MainRoute) in (render_application) method: {error}")
            return {"success": False, "message": "❌ Erro interno ao renderizar aplicação. Contate o administrador."}, 500   
