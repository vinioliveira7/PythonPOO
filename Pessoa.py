class Pessoa:
    id = 0
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        Pessoa.id += 1
