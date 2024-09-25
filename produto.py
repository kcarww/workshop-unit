# pylint: disable=C0115,E0401,C0116,C0103,C0303,C0304,C0114
from dataclasses import dataclass

@dataclass
class Produto:
    codigo: int
    nome: str
    preco: float
    quantidade: int
    disponivel: bool = True

    def __post_init__(self):
        self.validar_codigo(self.codigo)
        self.validar_nome(self.nome)
        self.validar_preco(self.preco)
        self.validar_quantidade(self.quantidade)

    def __str__(self):
        return f'{self.codigo} - {self.nome} - R$ {self.preco:.2f} - {self.quantidade} unidades'

    def __repr__(self):
        return str(self)
    
    def desativar(self):
        self.disponivel = False
    
    def ativar(self):
        self.disponivel = True

    # Validações
    def validar_codigo(self, codigo: int):
        if not isinstance(codigo, int) or codigo <= 0:
            raise ValueError("O código deve ser um número inteiro positivo.")

    def validar_nome(self, nome: str):
        if not isinstance(nome, str) or len(nome) == 0:
            raise ValueError("O nome deve ser uma string não vazia.")

    def validar_preco(self, preco: float):
        if not isinstance(preco, float) or preco <= 0:
            raise ValueError("O preço deve ser um número decimal positivo.")

    def validar_quantidade(self, quantidade: int):
        if not isinstance(quantidade, int) or quantidade < 0:
            raise ValueError("A quantidade deve ser um número inteiro não negativo.")
        
    
