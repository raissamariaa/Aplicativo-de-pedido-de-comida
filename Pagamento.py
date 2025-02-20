class Pagamento:
    def __init__(self, id, pedido, metodo_pagamento):
        self.id = id
        self.pedido = pedido
        self.metodo_pagamento = metodo_pagamento
        self.status = "pendente"

    def processar_pagamento(self):
        self.status = "concluído"
        print(f"Pagamento do pedido {self.pedido.id} processado com sucesso.")

    def verificar_status(self):
        print(f"Status do pagamento: {self.status}")
