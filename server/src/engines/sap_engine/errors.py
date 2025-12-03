class SapGuiErrors(Exception):
    
    def __init__(self, *args: str):
        super().__init__(*args)

class GuaranteeError(SapGuiErrors):
    
    def __init__(self):
        super().__init__("Erro ao salvar documento, está sem garantia.")

class IdNotFound(SapGuiErrors):
    
    def __init__(self, id: str):
        super().__init__(f"Field ID: {id} not located.")

class NotLogged(SapGuiErrors):
    
    def __init__(self):
        super().__init__("Please, log into SAP.")

class TransactionDennied(SapGuiErrors):
    
    def __init__(self, transacao: str):
        super().__init__(f"No access to {transacao}.")

class WindowBusy(SapGuiErrors):
    
    def __init__(self):
        super().__init__("All windows are busy. Go back to home to free a window.")

class WithoutSession(SapGuiErrors):
    
    def __init__(self):
        super().__init__("Create a SAP connection first.")
