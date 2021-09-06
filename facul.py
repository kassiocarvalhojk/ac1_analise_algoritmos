import random
import time

#ALGORITIMOS DE ORDENAÇÃO

#BUBBLE SORT

print('Algoritimo de ordenação BUBBLE SORT')
inicio_BUBBLE = time.time()
def bubble_sort(lista):
    for ultimo in range(len(lista), 0, -1):
        for atual in range(0,ultimo -1):
            if lista[atual] > lista[atual + 1]:
                lista[atual], lista[atual + 1] = lista[atual + 1], lista[atual]


a = list(range(101))
random.shuffle(a)
print('Lista gerada aleatoriamente\n', a)
bubble_sort(a)
print('Lista ordenada\n', a)
final_BUBBLE = time.time()
print('Tempo de execução do BUBBLE SORT: ', round(final_BUBBLE - inicio_BUBBLE,5),'segundos\n')



print('Algoritimo de ordenação SELECTION SORT')
inicio_SELECTION = time.time()
def selection_sort(lista):
    for item in range(0, len(lista)):
        menorValor = item
        for direita in range(item + 1, len(lista)):
            if lista[direita] < lista[menorValor]:
                menorValor = direita
        lista[item], lista[menorValor] = lista[menorValor], lista[item]


b = list(range(101))
random.shuffle(b)
print('Lista gerada aleatoriamente\n', b)
selection_sort(b)
print('Lista ordenada\n', b)
final_SELECTION = time.time()
print('Tempo de execução do SELECTION SORT: ', round(final_SELECTION - inicio_SELECTION, 5),'segundos\n')

#INSERCTION SORT
print('Algoritimo de ordenação INSERCTION SORT')
inicio_INSERCTION = time.time()
def inserction_sort(lista):
    for posicao in range(0, len(lista)):
        elementoAtual = lista[posicao]
        while posicao > 0 and lista[posicao - 1] > elementoAtual:
            lista[posicao] = lista[elementoAtual]
        posicao -= 1


c = list(range(101))
random.shuffle(c)
print('Lista gerada aleatoriamente\n', c)
selection_sort(c)
print('Lista ordenada\n', c)
final_INSERCTION = time.time()
print('Tempo de execução do INSERCTION SORT: ', round(final_INSERCTION - inicio_INSERCTION, 5),'segundos')


#MERGE SORT
print('Algoritimo de ordenação MERGE SORT')
inicio_MERGE = time.time()
def merge_sort(lista):
    metade(lista, 0, len(lista)-1)

def metade(lista, inicio, fim):
    if inicio >= fim:
        return

    meio = (inicio + fim) // 2
    metade(lista, inicio, meio)
    metade(lista, meio + 1, fim)

    merge(lista, inicio, fim)
def merge(lista, inicio, fim):
    lista[inicio: fim + 1] = sorted(lista[inicio: fim + 1])


d = list(range(101))
random.shuffle(d)
print('Lista gerada aleatoriamente\n', d)
merge_sort(d)
print('Lista ordenada\n', d)
final_MERGE = time.time()
print('Tempo de execução do MERGE SORT: ', round(final_MERGE - inicio_MERGE, 5),'segundos')

#QUICK SORT
print('Algoritimo de ordenação QUICK SORT')
inicio_QUICK = time.time()
def quick_sort(lista, esquerda, direita):
    if esquerda < direita:
        particao_posicao = particao(lista, esquerda, direita)
        quick_sort(lista, esquerda, particao_posicao - 1)
        quick_sort(lista, particao_posicao + 1, direita)

def particao(lista, esquerda, direita):
    i = esquerda
    j = direita - 1
    pivo = lista[direita]
    
    while i < j:
        while i < direita and lista[i] < pivo:
            i += 1
        while j > esquerda and lista[j] >= pivo:
            j -= 1
        if i < j:
            lista[i], lista[j] = lista[j], lista[i]
    if lista[i] > pivo:
        lista[i], lista[direita] = lista[direita], lista[i]
         
    return i

e = list(range(101))
random.shuffle(e)
print('Lista gerada aleatoriamente\n', e)
quick_sort(e, 0, len(e) - 1)
print('Lista ordenada\n', e)
final_QUICK = time.time()
print('Tempo de execução do QUICK SORT: ', round(final_QUICK - inicio_QUICK, 5),'segundos')



#ALGORITIMOS DE BUSCA

#BUSCA LINEAR
def busca_linear(arranjo, item):
    if item in arranjo:
        try:
            return arranjo.index(item)

        except ValueError:
            return "Não existe"
    else:
        return "Não existe"

#PESQUISA DE UM ELEMENTO PRESENTE

lista = list(range(1, 101))

print("O elemento {} está no indice {} do arranjo!".format(55, busca_linear(lista, 55)))

#PESQUISA DE UM ELEMENTO PRESENTE

print("O elemento {} {} no arranjo!".format(200, busca_linear(lista, 200)))
