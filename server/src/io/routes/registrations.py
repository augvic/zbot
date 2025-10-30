from src.tasks.auth.verify_if_have_access.task import VerifyIfHaveAccess
from src.tasks.post_data.include_new_registration.task import IncludeNewRegistration
from src.tasks.application.process_request.process_request import ProcessRequest

from ..models import NewRegistration

from flask import Flask
from typing import cast
from werkzeug.datastructures import FileStorage

class Registrations:
    
    def __init__(self, app: Flask) -> None:
        self.verify_if_have_access_task = VerifyIfHaveAccess()
        self.include_new_registration_task = IncludeNewRegistration()
        self.process_request_task = ProcessRequest()
        
        @app.route("/registrations", methods=["POST"])
        def include_registration() -> tuple[dict[str, bool | str], int] | dict[str, str | bool]:
            try:
                if not self.verify_if_have_access_task.execute("zRegRpa"):
                    return {"success": False, "message": "Sem autorização."}, 401
                response = self.process_request_task.execute(
                    content_type="multipart/form-data",
                    expected_data=[
                        "cnpj",
                        "seller",
                        "email",
                        "cpf",
                        "cpf_person",
                        "tax_regime",
                        "client_type",
                    ],
                    expected_files=[
                        "article_association_doc",
                    ],
                    optional=[
                        "suggested_limit",
                        "bank_doc"
                    ]
                )
                if not response.success:
                    return {"success": False, "message": f"{response.message}"}, 415
                response = self.include_new_registration_task.execute(
                    NewRegistration(
                        cnpj=cast(str, response.data.get("cnpj")),
                        seller=cast(str, response.data.get("seller")),
                        email=cast(str, response.data.get("email")),
                        cpf=cast(str, response.data.get("cpf")),
                        cpf_person=cast(str, response.data.get("cpf_person")),
                        tax_regime=cast(str, response.data.get("tax_regime")),
                        article_association_doc=cast(FileStorage, response.files.get("article_association_doc")),
                        bank_doc=response.files.get("bank_doc"),
                        suggested_limit=response.data.get("suggested_limit"),
                        client_type=cast(str, response.data.get("client_type"))
                    )
                )
                return {"success": True, "message": f"{response.message}"}
            except Exception as error:
                return {"success": False, "message": f"{error}"}
