class Pedido:
    def __init__(self, id, cliente, restaurante):
        self.id = id
        self.cliente = cliente
        self.restaurante = restaurante
        self.itens = []
        self.status = "preparação"
        self.total = 0.0

    def adicionar_item(self, prato):
        self.itens.append(prato)
        self.calcular_total()

    def remover_item(self, prato):
        self.itens.remove(prato)
        self.calcular_total()

    def calcular_total(self):
        self.total = sum(prato.preco for prato in self.itens)

    def aplicar_cupom_desconto(self, desconto):
        self.total -= desconto
        print(f"Desconto aplicado. Total agora é: {self.total}")

    def atualizar_status(self, novo_status):
        self.status = novo_status
        print(f"Status do pedido atualizado para: {self.status}")

