class GoDeepErrors(Exception):
    
    def __init__(self, *args: str):
        super().__init__(*args)

class OrderNotExistsError(GoDeepErrors):
    
    def __init__(self, order: str):
        super().__init__(f"Pedido {order} não foi inserido no site ainda.")
