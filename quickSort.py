#!/usr/bin/python3.5
#PARA RODAR O PROGRAMA  ./quickSort.py ArquivoDeEntrada.in
#PARA RODAR O PROGRAMA VENDO OS PASSOS ./quickSort.py ArquivoDeEntrada.in | more
import sys

def quickSort(lista,inicio,fim):

    if inicio < fim:

        meio = partido(lista,inicio, fim)
        print('\033[31m'+' | INDICE DO MEIO | '+'\033[0;0m', meio,'\033[31m'+ ' | VALOR DA LISTA NO INDICE | '
        +'\033[0;0m', lista[meio], '\033[31m'+' |''\033[0;0m')
        quickSort(lista, inicio, meio-1)
        quickSort(lista, meio+1, fim)

def partido(lista,primeiro,ultimo):
   pivo = lista[primeiro]

   esquerda = primeiro+1
   direita = ultimo

   done = False
   while not done:

       while esquerda <= direita and lista[esquerda] <= pivo:
           esquerda = esquerda + 1

       while lista[direita] >= pivo and direita >= esquerda:
           direita = direita -1

       if direita < esquerda:
           done = True
       else:
           aux = lista[esquerda]
           lista[esquerda] = lista[direita]
           lista[direita] = aux

   aux = lista[primeiro]
   lista[primeiro] = lista[direita]
   lista[direita] = aux


   return direita



### MAIN ###

#ista = [2,5,6,3,1,4]
#lista = [54,26,93,17,77,31,44,55,20]
#lista = ["a", "k", "b", "f", "z", "g", "d", "o"]
lista = []
nome = sys.argv[1]
arq = open(nome, 'r')
i = 0
for line in arq:
    convertido = int(line)
    lista.append(convertido)
    i = i + 1
arq.close()

print(lista)
quickSort(lista, 0, len(lista)-1)
print(lista)

