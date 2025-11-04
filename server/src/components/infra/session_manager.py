from flask import session
from typing import Any

class SessionManager:
    
    def save_in_session(self, key: str, value: Any) -> None:
        try:
            session[key] = value
        except Exception as error:
            raise Exception(f"Error in (SessionManager) component in (save_in_session) method: {error}.")
    
    def get_from_session(self, key: str) -> Any:
        try:
            return session[key]
        except Exception as error:
            raise Exception(f"Error in (SessionManager) component in (get_from_session) method: {error}.")
    
    def is_user_in_session(self) -> bool:
        try:
            if "user" in session:
                return True
            return False
        except Exception as error:
            raise Exception(f"Error in (SessionManager) component in (is_user_in_session) method: {error}.")
    
    def have_user_module_access(self, module: str) -> bool:
        try:
            for module_allowed in session["session_modules"]:
                if str(module_allowed["module"]).lower() == str(module).replace(".js", "").lower():
                    return True
            return False
        except Exception as error:
            raise Exception(f"Error in (SessionManager) component in (have_user_module_access) method: {error}.")
    
    def remove_from_session(self, key: str) -> None:
        try:
            session.pop(key)
        except Exception as error:
            raise Exception(f"Error in (SessionManager) component in (remove_from_session) method: {error}.")
    
    def clear_session(self) -> None:
        try:
            session.clear()
        except Exception as error:
            raise Exception(f"Error in (SessionManager) component in (clear_session) method: {error}.")
