class Pessoa:
    id = 0
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        self.id += 1
