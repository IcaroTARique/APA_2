#!/usr/bin/python3.5
#PARA RODAR O PROGRAMA  ./mergeSort.py
import sys

def mergeSort(lista, tam):
    if len(lista) > 1:
        meio = int(len(lista)/2)
        print('\033[36m'+"MEIO",meio, '\033[0;0m')

        listaDaEsquerda = lista[:meio]
        print ('\033[31m'+'---> Lista da Esquerda'+'\033[0;0m', listaDaEsquerda)
        listaDaDireita = lista[meio:]
        print('\033[32m'+'--->  Lista da Direita'+'\033[0;0m', listaDaDireita)

        mergeSort(listaDaEsquerda,meio)
        mergeSort(listaDaDireita,meio)
        Merge(lista, listaDaEsquerda, listaDaDireita)

def Merge(lista, listaEsquerda,listaDireita):
        print('\033[41m'+'      INICIANDO O MERGE'+'\033[0;0m')
        i = 0
        j = 0
        k = 0

        while i < len(listaEsquerda) and j < len(listaDireita):

            if listaEsquerda[i] < listaDireita[j]:
                lista[k]=listaEsquerda[i]
                i += 1
            else:
                lista[k]=listaDireita[j]
                j += 1
            k += 1

        while i < len(listaEsquerda):

            lista[k]=listaEsquerda[i]
            i += 1
            k += 1

        while j < len(listaDireita):
            lista[k]=listaDireita[j]
            j += 1
            k += 1
        print(lista)
        print('\033[41m'+'      FIM DO MERGE'+'\033[0;0m')


#MAIN
#lista = [2,5,6,3,1,4,7,8]
#lista = [54,26,93,17,77,31,44,55,20]
#lista = ["a", "k", "b", "f", "z", "g", "d", "o"]
lista = []
#nome = 'num.1000.1.in'
nome = sys.argv[1]
arq = open(nome, 'r')
#lista = ["a", "k", "b", "f", "z", "g", "d", "o"]
i = 0
for line in arq:
    convertido = int(line)
    lista.append(convertido)
    i = i + 1
arq.close()
mergeSort(lista, len(lista))
print(lista)

print(lista)
print(len(lista))
mergeSort(lista, len(lista))
print('\033[1m',lista,'\033[0;0m')