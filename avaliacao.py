class Avaliacao:
    def __init__(self, id, cliente, restaurante, entregador, nota, comentario):
        self.id = id
        self.cliente = cliente
        self.restaurante = restaurante
        self.entregador = entregador
        self.nota = nota
        self.comentario = comentario

    def deixar_avaliacao(self):
        print(f"Avaliação deixada: {self.nota} estrelas para o restaurante {self.restaurante.nome}.")