import random
from numpy.random import randint
from math import floor

#ALGORITIMOS DE ORDENAÇÃO

#BUBBLE SORT
print('Algoritimo de ordenação BUBBLE SORT')
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


#SELECTION SORT
print('Algoritimo de ordenação SELECTION SORT')
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


#INSERCTION SORT
print('Algoritimo de ordenação INSERCTION SORT')
def inserction_sort(lista):
    for posicao in range(0, len(lista)):
        elementoAtual = lista[posicao]

        while posicao > 0 and lista[posicao - 1] > elementoAtual:
            lista[posicao] = lista[posicao - 1]
            posicao -= 1

        lista[posicao] = elementoAtual

c = list(range(21))
random.shuffle(c)
print('Lista gerada aleatoriamente\n', c)
inserction_sort(c)
print('Lista ordenada\n', c)


#MERGE SORT
print('Algoritimo de ordenação MERGE SORT')
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

d = list(range(21))
random.shuffle(d)
print('Lista gerada aleatoriamente\n', d)
merge_sort(d)
print('Lista ordenada\n', d)


#QUICK SORT
print('Algoritimo de ordenação QUICK SORT')
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

e = list(range(21))
random.shuffle(e)
print('Lista gerada aleatoriamente\n', e)
quick_sort(e, 0, len(e) - 1)
print('Lista ordenada\n', e)


#HEAP SORT
print('Algoritimo de ordenação HEAP SORT')
def max_heap(lista, n, parente_index):
    maior = parente_index
    esquerda = 2*parente_index + 1
    direita = 2*parente_index +2

    if esquerda < n and lista[esquerda] > lista[maior]:
        maior = esquerda
    if direita < n and lista[direita] > lista[maior]:
        maior = direita

    if maior != parente_index:
        lista[maior], lista[parente_index] = lista[parente_index], lista[maior]
        max_heap(lista, n, maior)

def heap_sort(lista):
    n = len(lista)
    for i in range(n // 2 - 1, -1, -1):
        max_heap(lista, n, i)

    for i in range(n-1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        max_heap(lista, i, 0)




f = list(range(21))
random.shuffle(f)
print('Lista gerada aleatoriamente\n', f)
heap_sort(f)
print('Lista ordenada\n', f)


#BUCKET SORT
print('Algoritimo de ordenação BUCKET SORT')
def bucket_sort(lista):
    if not lista: # se a lista é vazia, retorna ela mesma
        return lista

    # passos 1 e 2, cria os buckets e distribui os elementos neles
    baldes = distribuicao(lista)

    # passo 3, ordena os buckets
    for balde in baldes:
        insertion_sort(balde)

    # passo 4, junta os buckets
    return juntando(baldes)

def distribuicao(lista):
    # passo 1, cria os buckets
    min_valor = min(lista)
    max_valor = max(lista)
    qtd_baldes = floor((max_valor - min_valor) / len(lista)) + 1
    baldes = [ [] for _ in range(qtd_baldes) ]

    # passo 2, distribui os elementos nos buckets
    for num in lista:
        baldes[floor((num - min_valor) / len(lista))].append(num)
    return baldes

def insertion_sort(balde):
    # ordena um único bucket, usando insertion sort
    for i in range(1, len(balde)):
        up = balde[i]
        j = i - 1
        while j >= 0 and balde[j] > up:
            balde[j + 1] = balde[j]
            j -= 1
        balde[j + 1] = up

def juntando(baldes):
    # passo 4, junta os buckets
    lista = []
    for balde in baldes:
        lista.extend(balde)
    return lista


g = list(range(21))
random.shuffle(g)
print('Lista gerada aleatoriamente\n', g)
print('Lista ordenada\n', bucket_sort(g))



#ALGORITIMOS DE BUSCA

#BUSCA LINEAR
def busca_linear(arranjo, item):
    if item in arranjo:
        try:
            return arranjo.index(item)

        except ValueError:
            return "não existe"
    else:
        return "não existe"

#PESQUISA DE UM ELEMENTO PRESENTE

lista_busca_linear = list(range(1, 21))

print("O elemento {} está no indice {} do arranjo!\n".format(15, busca_linear(lista_busca_linear, 15)))

#PESQUISA DE UM ELEMENTO PRESENTE

print("O elemento {} {} no arranjo!\n".format(200, busca_linear(lista_busca_linear, 200)))



#BUSCA BINÁRIA
def busca_binaria(lista, item, inicio, fim):
    #if fim is None:
        #fim = len(lista)-1
    if inicio <= fim:
        m = (inicio + fim) // 2
        if lista[m] == item:
            return m
        if item < lista[m]:
            return busca_binaria(lista, item, inicio, m-1)
        else:
            return busca_binaria(lista, inicio, m+1, fim)
    return None


lista_busca_binaria = list(range(21))
print('O elemento da busca binária é ', busca_binaria(lista_busca_binaria, 10, 0, len(lista_busca_binaria)-1))
