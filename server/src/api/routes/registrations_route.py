from src.engines.engines import Engines
from src.tasks.tasks import Tasks

from typing import cast
from werkzeug.datastructures import FileStorage

class RegistrationsRoute:
    
    def __init__(self, engines: Engines, tasks: Tasks) -> None:
        self.tasks = tasks
        self.engines = engines
        self.engines.wsgi_engine.register_route("/registrations", ["POST"], self.include_registration)
        self.engines.wsgi_engine.register_route("/registrations/<cnpj>", ["GET"], self.get_registration)
        self.engines.wsgi_engine.register_route("/registrations/<cnpj>", ["DELETE"], self.delete_registration)
        self.engines.wsgi_engine.register_route("/registrations", ["PUT"], self.update_registration)
    
    def include_registration(self) -> tuple[dict[str, bool | str], int]:
        try:
            if not self.engines.wsgi_engine.session_manager.is_user_in_session():
                return {"success": False, "message": "❌ Usuário não está na sessão."}, 401
            if not self.engines.wsgi_engine.session_manager.have_user_module_access("zRegRpa"):
                return {"success": False, "message": "❌ Sem autorização."}, 401
            response = self.engines.wsgi_engine.process_request(
                content_type="multipart/form-data",
                expected_data=[
                    "cnpj",
                    "seller",
                    "email",
                    "cpf",
                    "cpf_person",
                    "tax_regime",
                    "client_type",
                    "suggested_limit"
                ],
                expected_files=[
                    "article_association_doc",
                    "bank_doc"
                ]
            )
            if not response.success:
                return {"success": False, "message": f"{response.message}"}, 400
            response = self.tasks.create_registration_task.main(
                cnpj=cast(str, response.data.get("cnpj")),
                seller=cast(str, response.data.get("seller")),
                email=cast(str, response.data.get("email")),
                cpf=cast(str, response.data.get("cpf")),
                cpf_person=cast(str, response.data.get("cpf_person")),
                tax_regime=cast(str, response.data.get("tax_regime")),
                article_association_doc=cast(FileStorage, response.files.get("article_association_doc")),
                bank_doc=response.files.get("bank_doc"),
                suggested_limit=cast(float, response.data.get("suggested_limit")),
                client_type=cast(str, response.data.get("client_type"))
            )
            if response.success:
                return {"success": True, "message": f"{response.message}"}, 200
            else:
                return {"success": False, "message": f"{response.message}"}, 400
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
    
    def get_registration(self, cnpj: str) -> tuple[dict[str, str | bool | list[dict[str, str]]], int]:
        try:
            if not self.engines.wsgi_engine.session_manager.is_user_in_session():
                return {"success": False, "message": "❌ Usuário não está na sessão."}, 401
            if not self.engines.wsgi_engine.session_manager.have_user_module_access("zRegRpa"):
                return {"success": False, "message": "❌ Sem autorização."}, 401
            response = self.tasks.get_registration_task.main(cnpj)
            if response.success:
                return {"success": True, "message": response.message, "data": response.data}, 200
            else:
                return {"success": False, "message": response.message, "data": response.data}, 400
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
    
    def delete_registration(self, cnpj: str) -> tuple[dict[str, str | bool | list[dict[str, str]]], int]:
        try:
            if not self.engines.wsgi_engine.session_manager.is_user_in_session():
                return {"success": False, "message": "❌ Usuário não está na sessão."}, 401
            if not self.engines.wsgi_engine.session_manager.have_user_module_access("zRegRpa"):
                return {"success": False, "message": "❌ Sem autorização."}, 401
            response = self.tasks.delete_registration_task.main(cnpj)
            if response.success:
                return {"success": True, "message": response.message}, 200
            else:
                return {"success": False, "message": response.message}, 400
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
    
    def update_registration(self) -> tuple[dict[str, str | bool | list[dict[str, str]]], int]:
        try:
            if not self.engines.wsgi_engine.session_manager.is_user_in_session():
                return {"success": False, "message": "❌ Usuário não está na sessão."}, 401
            if not self.engines.wsgi_engine.session_manager.have_user_module_access("zRegRpa"):
                return {"success": False, "message": "❌ Sem autorização."}, 401
            response = self.engines.wsgi_engine.process_request(
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
                expected_files=[]
            )
            if not response.success:
                return {"success": False, "message": response.message}, 400
            response = self.tasks.update_registration_task.main(
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
                cpf_person=cast(str, response.data.get("cpf_person")),
                bank_doc=cast(FileStorage, response.data.get("bank_doc")),
                article_association_doc=cast(FileStorage, response.data.get("article_association_doc"))
            )
            if response.success:
                return {"success": True, "message": response.message}, 200
            else:
                return {"success": False, "message": response.message}, 400
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
