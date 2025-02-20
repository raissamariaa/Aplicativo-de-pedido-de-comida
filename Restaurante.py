class Restaurante:
    def __init__(self, id, nome, endereco, cnpj, horario_funcionamento):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.cnpj = cnpj
        self.horario_funcionamento = horario_funcionamento
        self.pratos = []

    def cadastrar_perfil(self):
        print(f"Restaurante {self.nome} cadastrado com sucesso.")

    def gerenciar_pratos(self, prato):
        self.pratos.append(prato)
        prato.cadastrar_prato()

    def aceitar_pedido(self):
        print(f"Pedido aceito pelo restaurante {self.nome}.")

    def recusar_pedido(self):
        print(f"Pedido recusado pelo restaurante {self.nome}.")
