from flask import render_template

class TemplateManager:
    
    def render(self, template: str) -> str:
        try:
            return render_template(template)
        except Exception as error:
            raise Exception(f"Error in (TemplateManager) module in (render) method: {error}")
