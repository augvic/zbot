from flask import send_from_directory, render_template, session
from os import path

class BundleManager:
    
    def send_module(self, module: str):
        BASE_DIR = path.dirname(path.abspath(__file__))
        MODULES_DIR = path.abspath(path.join(BASE_DIR, "../../../.javascript/io/modules"))
        return send_from_directory(MODULES_DIR, f"{module}")
    
    def send_page(self, page: str):
        BASE_DIR = path.dirname(path.abspath(__file__))
        PAGES_DIR = path.abspath(path.join(BASE_DIR, "../../../.javascript/io/pages"))
        return send_from_directory(PAGES_DIR, f"{page}")
    
    def send_component(self, component: str):
        BASE_DIR = path.dirname(path.abspath(__file__))
        PAGES_DIR = path.abspath(path.join(BASE_DIR, "../../../.javascript/io/components"))
        return send_from_directory(PAGES_DIR, f"{component}")

    def send_task(self, task: str):
        BASE_DIR = path.dirname(path.abspath(__file__))
        PAGES_DIR = path.abspath(path.join(BASE_DIR, "../../../.javascript/tasks"))
        return send_from_directory(PAGES_DIR, f"{task}")

class TemplateManager:
    
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
        for module_allowed in session["session_modules"]:
            if module_allowed["module"] == module:
                return True
        return False
