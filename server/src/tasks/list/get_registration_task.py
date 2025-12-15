from src.engines.engines import Engines

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class GetRegistrationTask:
    
    def __init__(self, engines: Engines) -> None:
        self.engines = engines
    
    def main(self, cnpj: str) -> Response:
        try:
            if cnpj == "all":
                registrations = self.engines.database_engine.registrations_client.read_all()    
            else:
                registrations = self.engines.database_engine.registrations_client.read(cnpj)
            if isinstance(registrations, list):
                registrations_serialized = self.engines.serializer_engine.serialize_sqla_list(registrations)
            elif not registrations:
                return Response(success=False, message=f"❌ Cadastro ({cnpj}) não existe.", data=[])
            else:
                registrations_serialized = [self.engines.serializer_engine.serialize_sqla(registrations)]
            return Response(success=True, message="✅ Cadastro(s) coletado(s) com sucesso.", data=registrations_serialized)
        except Exception as error:
            raise Exception(f"❌ Error in (GetRegistrationTask) in (main) method: {error}")
