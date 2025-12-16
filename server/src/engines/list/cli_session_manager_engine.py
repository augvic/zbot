from typing import Any

class CliSessionManagerEngine:

    def __init__(self) -> None:
        self.session = {}
    
    def save_in_session(self, key: str, value: Any) -> None:
        try:
            self.session[key] = value
        except Exception as error:
            raise Exception(f"❌ Error in (CliSessionEngine) in (save_in_session) method: {error}")
    
    def get_session_user(self) -> Any:
        try:
            return self.session["user"]
        except Exception as error:
            raise Exception(f"❌ Error in (CliSessionEngine) in (get_session_user) method: {error}")
    
    def get_session_modules(self) -> Any:
        try:
            return self.session["session_modules"]
        except Exception as error:
            raise Exception(f"❌ Error in (CliSessionEngine) in (get_session_modules) method: {error}")
    
    def is_user_in_session(self) -> bool:
        try:
            if "user" in self.session:
                return True
            return False
        except Exception as error:
            raise Exception(f"❌ Error in (CliSessionEngine) in (is_user_in_session) method: {error}")
    
    def have_user_module_access(self, module: str) -> bool:
        try:
            for module_allowed in self.session["session_modules"]:
                if str(module_allowed["module"]).lower() == str(module).replace(".js", "").lower():
                    return True
            return False
        except Exception as error:
            raise Exception(f"❌ Error in (CliSessionEngine) in (have_user_module_access) method: {error}")
    
    def remove_from_session(self, key: str) -> None:
        try:
            self.session.pop(key)
        except Exception as error:
            raise Exception(f"❌ Error in (CliSessionEngine) in (remove_from_session) method: {error}")
    
    def clear_session(self) -> None:
        try:
            self.session.clear()
        except Exception as error:
            raise Exception(f"❌ Error in (CliSessionEngine) in (clear_session) method: {error}")
