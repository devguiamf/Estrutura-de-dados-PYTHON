from email.errors import InvalidMultipartContentTransferEncodingDefect
from lib.stack import Stack

#Cria a pilha
pilha = Stack()

print('Pilha esta vazia?', pilha.is_empty)

try:
    x = pilha.pop()
except:
    print('Aconteceu o erro de retirada da pulha vazia. Ignorando...')

pilha.push(12)
pilha.push(15)

try:
    x = pilha.peek()
except:
    print('Aconteceu o erro de retirada da pulha vazia. Ignorando...')

print('Pilha esta vazia?', pilha.is_empty)

print('X: ',x)

print(pilha)

from data.lista_nomes import nomes

inversor = Stack()

#Empilhar cada um dos nomes da pilha inversora
for nome in nomes:
    inversor.push(nome)

nomes_inverso = []

#A medida que desempilha do inversor, coloca os nome em nomes_inverso
while not inversor.is_empty:
    nomes_inverso.append(inversor.pop())

#Exibe os 100 primeiros nomes de nomes_inverso
print(nomes_inverso[:100])