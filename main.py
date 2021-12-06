from list import List

list = List(10)

print('Inserindo valores na frente da lista')

list.inserirNaFrente(1)
print(list.acessarAtual().value)
list.inserirNaFrente(2)
print(list.acessarAtual().value)
list.inserirNaFrente(3)
print(list.acessarAtual().value)

print('Inserindo valores no fim da lista')
list.inserirNoFim(10)
print(list.acessarAtual().value)
list.inserirNoFim(11)
print(list.acessarAtual().value)
list.inserirNoFim(12)
print(list.acessarAtual().value)

print('Inserindo valor antes do atual')
list.inserirAntesDoAtual(20)
print(list.acessarAtual().value)

print('Inserindo valor depois do atual')
list.inserirApósAtual(21)
print(list.acessarAtual().value)

print('Verificando se lista está vazia')
print(list.vazia())

print('Verificando se lista está cheia')
print(list.cheia())

