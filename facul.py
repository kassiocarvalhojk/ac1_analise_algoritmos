import random
import time

print('Algoritimo de ordenação BUBBLE SORT')
inicio = time.time()
def bubble_sort(lista):
    for ultimo in range(len(lista), 0, -1):
        for atual in range(0,ultimo -1):
            if lista[atual] > lista[atual + 1]:
                lista[atual], lista[atual + 1] = lista[atual + 1], lista[atual]


a = list(range(21))
random.shuffle(a)
print('Lista gerada aleatoriamente\n', a)
bubble_sort(a)
print('Lista ordenada\n', a)
final = time.time()
print('Tempo de execução do BUBBLE SORT: ', round(final - inicio,4),'segundos\n')



print('Algoritimo de ordenação SELECTION SORT')
inicio = time.time()
def selection_sort(lista):
    for item in range(0, len(lista)):
        menorValor = item
        for direita in range(item + 1, len(lista)):
            if lista[direita] < lista[menorValor]:
                menorValor = direita
        lista[item], lista[menorValor] = lista[menorValor], lista[item]


b = list(range(21))
random.shuffle(b)
print('Lista gerada aleatoriamente\n', b)
selection_sort(b)
print('Lista ordenada\n', b)
final = time.time()
print('Tempo de execução do SELECTION SORT: ', round(final - inicio, 4),'segundos\n')


print('Algoritimo de ordenação INSERCTION SORT')
inicio = time.time()
def inserction_sort(lista):
    for posicao in range(0, len(lista)):
        elementoAtual = lista[posicao]
        while posicao > 0 and lista[posicao - 1] > elementoAtual:
            lista[posicao] = lista[elementoAtual]
        posicao -= 1


c = list(range(21))
random.shuffle(c)
print('Lista gerada aleatoriamente\n', c)
selection_sort(c)
print('Lista ordenada\n', c)
final = time.time()
print('Tempo de execução do INSERCTION SORT: ', round(final - inicio, 4),'segundos')