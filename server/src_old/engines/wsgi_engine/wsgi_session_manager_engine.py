from flask import session

from typing import Any

class WsgiSessionManagerEngine:
    
    def save_in_session(self, key: str, value: Any) -> None:
        try:
            session[key] = value
        except Exception as error:
            raise Exception(f"❌ Error in (WsgiEngineSessionManager) engine in (save_in_session) method: {error}")
    
    def get_session_user(self) -> Any:
        try:
            return session["user"]
        except Exception as error:
            raise Exception(f"❌ Error in (WsgiEngineSessionManager) engine in (get_session_user) method: {error}")
    
    def get_session_modules(self) -> Any:
        try:
            return session["session_modules"]
        except Exception as error:
            raise Exception(f"❌ Error in (WsgiEngineSessionManager) engine in (get_session_modules) method: {error}")
    
    def is_user_in_session(self) -> bool:
        try:
            if "user" in session:
                return True
            return False
        except Exception as error:
            raise Exception(f"❌ Error in (WsgiEngineSessionManager) engine in (is_user_in_session) method: {error}")
    
    def have_user_module_access(self, module: str) -> bool:
        try:
            for module_allowed in session["session_modules"]:
                if str(module_allowed["module"]).lower() == str(module).replace(".js", "").lower():
                    return True
            return False
        except Exception as error:
            raise Exception(f"❌ Error in (WsgiEngineSessionManager) engine in (have_user_module_access) method: {error}")
    
    def remove_from_session(self, key: str) -> None:
        try:
            session.pop(key)
        except Exception as error:
            raise Exception(f"❌ Error in (WsgiEngineSessionManager) engine in (remove_from_session) method: {error}")
    
    def clear_session(self) -> None:
        try:
            session.clear()
        except Exception as error:
            raise Exception(f"❌ Error in (WsgiEngineSessionManager) engine in (clear_session) method: {error}")
