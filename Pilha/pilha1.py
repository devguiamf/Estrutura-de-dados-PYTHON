'''
    ESTRUTURA DE DADOS PILHA (STACK)
        é uma estrutura de daddos linear em que tanto a operação de inserção (PUSH) quanto a operação retirada(POP) acontecem no final (ou topo).
        Como consequencia o funcionamento da pilha pode ser definido como LIFO(Last in, First out): O Ultimo a entrar e o primeiro a sair.
'''

# Usando uma pilha rudimentar para inverter um texto

texto = 'PINDAMONHAGABA'

# Em python, é possivel fazer com que uma lista se comporte como uma pilha 

Pilha = []

#Colocando cada uma das letras do texto no final da pilha
for letra in texto:
    Pilha.append(letra)



inverso = ''

#Enquanto houver elemento na pilha
while len(Pilha) > 0:
    retirando = Pilha.pop()
    inverso += retirando

print("Original: ", texto)

print("Inverso:  ", inverso)