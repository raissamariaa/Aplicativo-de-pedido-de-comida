from typing import List

class Usuario:
    usuarios_registrados = []

    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha
        Usuario.usuarios_registrados.append(self)

    def autenticar(self, email: str, senha: str) -> bool:
        return self.email == email and self.senha == senha

    def logout(self):
        print(f"{self.nome} fez logout.")

    @staticmethod
    def registrar_usuario(nome: str, email: str, senha: str, tipo: str, endereco: str = "", cnpj: str = "", horario_funcionamento: str = ""):
        if tipo == "cliente":
            return Cliente(nome, email, senha)
        elif tipo == "restaurante":
            return Restaurante(nome, email, senha, endereco, cnpj, horario_funcionamento)
        elif tipo == "entregador":
            return Entregador(nome, email, senha)
        else:
            raise ValueError("Tipo de usuário inválido")


