from flask import session

class SessionManager:
    
    def save_in_session(self, key: str, value: str) -> None:
        session[key] = value
    
    def get_from_session(self, key: str) -> str:
        return session[key]
    
    def is_user_in_session(self) -> bool:
        if "user" in session:
            return True
        return False
    
    def have_user_module_access(self, module: str) -> bool:
        for module_allowed in session["session_modules"]:
            if module_allowed["module"] == module:
                return True
        return False
