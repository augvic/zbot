from flask import Flask, request
from src.tasks.verify_if_have_access import VerifyIfHaveAccess
from src.tasks.include_new_registration import IncludeNewRegistration

class Registrations:
    
    def __init__(self, app: Flask) -> None:
        self.verify_if_have_access_task = VerifyIfHaveAccess()
        self.include_new_registration_task = IncludeNewRegistration()
        
        @app.route("/registrations", methods=["POST"])
        def include_registration() -> tuple[str, int] | dict[str, str | bool]:
            # if not self.verify_if_have_access_task.execute("zRegRpa"):
            #     return "Sem autorização.", 401
            data = request.form.to_dict()
            article_association_doc = request.files.get("article_association_doc")
            bank_doc = request.files.get("bank_doc")
            return self.include_new_registration_task.execute(
                cnpj=data["cnpj"],
                seller=data["seller"],
                email=data["email"],
                cpf=data["cpf"],
                cpf_person=data["cpf_person"],
                tax_regime=data["tax_regime"],
                article_association_doc=article_association_doc,
                bank_doc=bank_doc,
                suggested_limit=data["suggested_limit"],
                client_type=data["client_type"]
            )
