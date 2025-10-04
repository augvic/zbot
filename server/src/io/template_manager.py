from flask import render_template

class TemplateManager:
    
    def render(self, template: str) -> str:
        return render_template(template)
