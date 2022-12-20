import json
import os
from Pessoa import Pessoa
PATH = "BDPessoas.json"
 
def people_register():
    nome = input("Digite nome: ")
    idade = int(input("Digite idade: "))
    pessoa = Pessoa(nome, idade)

    return vars(pessoa)


bd = []

size = os.path.getsize(PATH)
if size == 0:
    pass
else:
    with open(PATH, 'r') as arquivo:
        pessoas = json.load(arquivo)

        for i in range(0, len(pessoas)):
            bd.append(vars(Pessoa(**pessoas[i])))


while True:
    
    opcao = int(input("deseja cadastrar um usuário? "))
    if opcao == 1:
        bd.append(people_register())
        print(bd)

        
    else:
        with open(PATH, 'w') as arquivo:
            json.dump(bd, arquivo, ensure_ascii=False, indent=2)
        break
    