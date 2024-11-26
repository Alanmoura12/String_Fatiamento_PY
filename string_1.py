nome = "João Pedro"
idade = 27
profissao = "Programador"
linguagem = "Python"
saldo = 45.846

dados = {"nome": " João Pedro", "idade": 28}

print("Nome: %s Idade: %d"%(nome, idade))

print("Nome: {} Idade: {}".format (nome,idade))

print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"nome: {nome} Idade: {idade} saldo: {saldo :10.2f}")# com 10 espaços e com 2 casas após a virgula

print(f"nome: {nome} Idade: {idade} saldo: {saldo :.3f}")