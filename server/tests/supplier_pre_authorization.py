from src.modules.supplier_handler.supplier_handler import SupplierHandler

supplier = SupplierHandler()
supplier.login()
response = supplier.order_pre_autorization(
    cnpj_client="02006342000144",
    cnpj_positivo="81243735001977",
    order="1007285817",
    payment_deadline="30/60/90/120/150",
    value=1779.78
)
if response.success:
    print(f"✅ Sucesso ao pré-autorizar: {response.message}")
else:
    print(f"❌ Erro ao pré-autorizar: {response.message}")
