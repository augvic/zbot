from flask import Blueprint
from flask.views import MethodView
from src.tasks.render_template import RenderTemplate

main = Blueprint("main", __name__)

class Main(MethodView):
    
    def get(self) -> str:
        task = RenderTemplate()
        return task.execute("main.html")

main.add_url_rule("/", view_func=Main.as_view("main"), methods=["GET"])
