from src.tasks.auth.verify_if_have_access.task import VerifyIfHaveAccess
from src.tasks.post_data.include_new_registration.task import IncludeNewRegistration
from src.tasks.post_data.include_new_registration.models import NewRegistration
from src.tasks.application.process_request.task import ProcessRequest
from src.tasks.application.route_registry import RouteRegistryTask
from typing import cast
from werkzeug.datastructures import FileStorage

class Registrations:
    
    def __init__(self,
        verify_if_have_access_task: VerifyIfHaveAccess,
        include_new_registration_task: IncludeNewRegistration,
        process_request_task: ProcessRequest,
        route_registry_task: RouteRegistryTask
    ) -> None:
        self.verify_if_have_access_task = verify_if_have_access_task
        self.include_new_registration_task = include_new_registration_task
        self.process_request_task = process_request_task
        self.route_registry_task = route_registry_task
    
    def include_registration(self) -> tuple[dict[str, bool | str], int]:
        try:
            response = self.verify_if_have_access_task.execute("zRegRpa")
            if not response.success:
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
                optional_data=[
                    "suggested_limit",
                ],
                optional_files=[
                    "bank_doc"
                ]
            )
            if not response.success:
                return {"success": False, "message": f"{response.message}"}, 400
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
            if response.success:
                return {"success": True, "message": f"{response.message}"}, 200
            else:
                return {"success": True, "message": f"{response.message}"}, 400
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
