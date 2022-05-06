from __future__ import print_function
from lib.stack import Stack

analisador = Stack()

#expr = 'x + (9 - ((y * 2) /3) * 1)'
expr = 'x + (9 - ((y * 2) /3)) * 1)'

tem_erro = False

#Percorre a expressao em busca de parenteses
for pos in range(len(expr)):
    if expr[pos] == '(':
        #Poe a posicao no abre da pilha
        analisador.push(pos)
    elif expr[pos] == ')':
        #se a pilha estiver vazia, temos erro
        if analisador.is_empty:
            print(f'ERRO: fecha parenteses da posicoa {pos} nao tem o abre correspondente')
            tem_erro = True
        else:
            #Tira a posicão do abre da pilha
            pos_abre = analisador.pop()
            print(f'Abre parenteses da posicao {pos_abre} corresponde ao fecha parenteses da poiscao {pos}')

if not tem_erro:
    print('*** PARÊNTESES CORRETAMENTE BALANCEADO')

while not analisador.is_empty:
    pos_abre = analisador.pop()
    print(f'ERRO: abre parenteses da posicao {pos_abre} nao tem o fecha parenteses correspondente ***')
    tem_erro = True

if not tem_erro:
    print('*** PARÊNTESES CORRETAMENTE BALANCEADO')