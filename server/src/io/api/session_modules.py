from src.tasks.auth.verify_if_user_is_in_session.task import VerifyIfUserIsInSession
from src.tasks.auth.get_session_modules.task import GetSessionModules
from src.components.infra.wsgi_application import WsgiApplication

class SessionModules:
    
    def __init__(self) -> None:
        self.verify_if_user_is_in_session_task = VerifyIfUserIsInSession()
        self.get_session_modules_task = GetSessionModules()
        
    def register(self, app: WsgiApplication) -> None:
        try:
            @app.route("/session-modules", methods=["GET"])
            def get_session_modules() -> tuple[dict[str, str | bool | list[str]], int]:
                try:
                    response = self.verify_if_user_is_in_session_task.execute()
                    if not response.success:
                        return {"success": False, "message": response.message}, 401
                    response = self.get_session_modules_task.execute()
                    return {"success": True, "message": response.message, "data": response.data}, 200
                except Exception as error:
                    return {"success": False, "message": f"{error}"}, 500
        except Exception as error:
            print(f"❌ Error in (SessionModules) route: {error}.")