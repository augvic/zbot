from src.tasks.verify_if_have_access.verify_if_have_access import VerifyIfHaveAccess
from src.tasks.create_registration.create_registration import CreateRegistration
from src.tasks.create_registration.models import NewRegistration
from src.tasks.delete_registration.delete_registration import DeleteRegistration
from src.tasks.get_registration.get_registration import GetRegistration
from src.tasks.update_registration.update_registration import UpdateRegistration
from src.tasks.update_registration.models import RegistrationData
from src.tasks.process_request.process_request import ProcessRequest
from tasks.verify_if_user_is_in_session_task import VerifyIfUserIsInSession
from tasks.register_route_task import RegisterRoute

from typing import cast
from werkzeug.datastructures import FileStorage

class Registrations:
    
    def __init__(self,
        verify_if_have_access_task: VerifyIfHaveAccess,
        create_registration_task: CreateRegistration,
        delete_registration_task: DeleteRegistration,
        get_registration_task: GetRegistration,
        update_registration_task: UpdateRegistration,
        process_request_task: ProcessRequest,
        verify_if_user_is_in_session_task: VerifyIfUserIsInSession,
        register_route_task: RegisterRoute
    ) -> None:
        self.verify_if_have_access_task = verify_if_have_access_task
        self.create_registration_task = create_registration_task
        self.process_request_task = process_request_task
        self.update_registration_task = update_registration_task
        self.get_registration_task = get_registration_task
        self.delete_registration_task = delete_registration_task
        self.verify_if_user_is_in_session_task = verify_if_user_is_in_session_task
        register_route_task.main("/registrations", ["POST"], self.include_registration)
        register_route_task.main("/registrations/<cnpj>", ["GET"], self.get_registration)
        register_route_task.main("/registrations/<cnpj>", ["DELETE"], self.delete_registration)
        register_route_task.main("/registrations", ["PUT"], self.update_registration)
    
    def include_registration(self) -> tuple[dict[str, bool | str], int]:
        try:
            response = self.verify_if_user_is_in_session_task.main()
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.verify_if_have_access_task.main("zRegRpa")
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.process_request_task.main(
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
            response = self.create_registration_task.main(
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
                return {"success": False, "message": f"{response.message}"}, 400
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
    
    def get_registration(self, cnpj: str) -> tuple[dict[str, str | bool | list[dict[str, str]]], int]:
        try:
            response = self.verify_if_user_is_in_session_task.main()
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response =  self.verify_if_have_access_task.main("zRegRpa")
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.get_registration_task.main(cnpj)
            if response.success:
                return {"success": True, "message": response.message, "data": response.data}, 200
            else:
                return {"success": False, "message": response.message, "data": response.data}, 400
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
    
    def delete_registration(self, cnpj: str) -> tuple[dict[str, str | bool | list[dict[str, str]]], int]:
        try:
            response = self.verify_if_user_is_in_session_task.main()
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response =  self.verify_if_have_access_task.main("zRegRpa")
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.delete_registration_task.main(cnpj)
            if response.success:
                return {"success": True, "message": response.message}, 200
            else:
                return {"success": False, "message": response.message}, 400
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
    
    def update_registration(self) -> tuple[dict[str, str | bool | list[dict[str, str]]], int]:
        try:
            response = self.verify_if_user_is_in_session_task.main()
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response =  self.verify_if_have_access_task.main("zRegRpa")
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.process_request_task.main(
                content_type="application/json",
                expected_data=[
                    "cnpj",
                    "opening",
                    "company_name",
                    "trade_name",
                    "legal_nature",
                    "legal_nature_id",
                    "registration_status",
                    "street",
                    "number",
                    "complement",
                    "neighborhood",
                    "pac",
                    "city",
                    "state",
                    "fone",
                    "email",
                    "tax_regime",
                    "comission_receipt",
                    "status",
                    "client_type",
                    "suggested_limit",
                    "seller",
                    "cpf",
                    "cpf_person"
                ],
                expected_files=[],
                optional_data=[],
                optional_files=[]
            )
            if not response.success:
                return {"success": False, "message": response.message}, 400
            response = self.update_registration_task.main(
                RegistrationData(
                    cnpj=cast(str, response.data.get("cnpj")),
                    opening=cast(str, response.data.get("opening")),
                    company_name=cast(str, response.data.get("company_name")),
                    trade_name=cast(str, response.data.get("trade_name")),
                    legal_nature=cast(str, response.data.get("legal_nature")),
                    legal_nature_id=cast(str, response.data.get("legal_nature_id")),
                    registration_status=cast(str, response.data.get("registration_status")),
                    street=cast(str, response.data.get("street")),
                    number=cast(str, response.data.get("number")),
                    complement=cast(str, response.data.get("complement")),
                    neighborhood=cast(str, response.data.get("neighborhood")),
                    pac=cast(str, response.data.get("pac")),
                    city=cast(str, response.data.get("city")),
                    state=cast(str, response.data.get("state")),
                    fone=cast(str, response.data.get("fone")),
                    email=cast(str, response.data.get("email")),
                    tax_regime=cast(str, response.data.get("tax_regime")),
                    comission_receipt=cast(str, response.data.get("comission_receipt")),
                    status=cast(str, response.data.get("status")),
                    client_type=cast(str, response.data.get("client_type")),
                    suggested_limit=cast(float, response.data.get("suggested_limit")),
                    seller=cast(str, response.data.get("seller")),
                    cpf=cast(str, response.data.get("cpf")),
                    cpf_person=cast(str, response.data.get("cpf_person"))
                )
            )
            if response.success:
                return {"success": True, "message": response.message}, 200
            else:
                return {"success": False, "message": response.message}, 400
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
