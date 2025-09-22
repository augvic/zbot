from flask import send_from_directory, render_template, session
from os import path

class BundleSender:
    
    def send_module(self, module: str):
        BASE_DIR = path.dirname(path.abspath(__file__))
        MODULES_DIR = path.abspath(path.join(BASE_DIR, "../storage/web/.javascript/app/modules"))
        return send_from_directory(MODULES_DIR, f"{module}.js")
    
    def send_index(self,):
        BASE_DIR = path.dirname(path.abspath(__file__))
        APP_DIR = path.abspath(path.join(BASE_DIR, "../storage/web/.javascript/app"))
        return send_from_directory(APP_DIR, "index.js")
    
class TemplateRenderer:
    
    def render(self, template: str) -> str:
        return render_template(template)
    

class SessionManager:
    
    def save_in_session(self, key: str, value: any) -> None:
        session[key] = value
    
    def get_from_session(self, key: str) -> any:
        return session[key]
    
    def is_user_in_session(self) -> bool:
        if "user" in session:
            return True
        return False
    
    def have_user_module_access(self, module: str) -> bool:
        for module_allowed in session["modules_allowed"]:
            if module_allowed["module"] == module:
                return True
        return False
