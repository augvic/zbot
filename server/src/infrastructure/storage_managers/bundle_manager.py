from flask import send_from_directory
from os import path

class BundleManager:
    
    def send_module(self, module: str):
        BASE_DIR = path.dirname(path.abspath(__file__))
        MODULES_DIR = path.abspath(path.join(BASE_DIR, "../../storage/.web_output/modules"))
        return send_from_directory(MODULES_DIR, f"{module}")
    
    def send_page(self, page: str):
        BASE_DIR = path.dirname(path.abspath(__file__))
        PAGES_DIR = path.abspath(path.join(BASE_DIR, "../../storage/.web_output/pages"))
        return send_from_directory(PAGES_DIR, f"{page}")
