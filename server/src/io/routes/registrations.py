from src.tasks.verify_if_have_access import VerifyIfHaveAccess
from src.tasks.include_new_registration import IncludeNewRegistration
from src.tasks.process_request import ProcessRequest

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
            if not self.verify_if_have_access_task.execute("zRegRpa"):
                return {"success": False, "message": "Sem autorização."}, 401
            request_processed = self.process_request_task.execute(
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
                not_expected_data=[
                    "suggested_limit"
                ],
                not_expected_files=[
                    "bank_doc"
                ]
            )
            if not request_processed.success:
                return {"success": False, "message": f"Erro: {request_processed.message}"}, 415
            return self.include_new_registration_task.execute(
                NewRegistration(
                    cnpj=cast(str, request_processed.data["cnpj"]),
                    seller=cast(str, request_processed.data["seller"]),
                    email=cast(str, request_processed.data["email"]),
                    cpf=cast(str, request_processed.data["cpf"]),
                    cpf_person=cast(str, request_processed.data["cpf_person"]),
                    tax_regime=cast(str, request_processed.data["tax_regime"]),
                    article_association_doc=cast(FileStorage, request_processed.files["article_association_doc"]),
                    bank_doc=cast(FileStorage, request_processed.files["bank_doc"]),
                    suggested_limit=cast(str, request_processed.data["suggested_limit"]),
                    client_type=cast(str, request_processed.data["client_type"])
                )
            )
