from src.engines.engines import Engines

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class DeleteRegistrationTask:
    
    def __init__(self, engines: Engines) -> None:
        self.engines = engines
    
    def main(self, cnpj: str) -> Response:
        try:
            registration_exists = self.engines.database_engine.registrations_client.read(cnpj)
            if registration_exists == None:
                return Response(success=False, message=f"❌ Cadastro ({cnpj}) não existe.", data=[])
            self.engines.database_engine.registrations_client.delete(cnpj)
            return Response(success=True, message=f"✅ Cadastro ({cnpj}) removido.", data=[])
        except Exception as error:
            raise Exception(f"❌ Error in (DeleteRegistrationTask) in (main) method: {error}")
