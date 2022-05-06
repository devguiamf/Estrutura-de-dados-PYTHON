'''
    Classe que implementa a estrutura de dados PILHA
'''

class Stack:

        '''Método Construtor'''
        def __init__(self):
            self.__data = [] #inicializa uma lista vazia 

        ''' 

            Método para inserção 
            O nome do método de inserção em pilhas é padronizado: push()

        '''
        def push(self, val):
            #insere val no final (topo) da pilha
            self.__data.append(val)

        '''
            Método para remoção
            O nome também é pradonizado: pop()
        '''
        def pop(self):
            if self.is_empty: #Tentativa de retirada de uma pilha
                raise Exception('ERRO: é impossivel retirar de uma pilha vazia')
            # a pilha não esta vazia, a retirada pode ser feita
            return self.__data.pop()
        
        '''

            Método que consulta o valor no top da pilha, sem retira-lo de lá
            Nome padronizado: peek() 

        '''

        def peek(self):
            if self.is_empty:
                raise Exception('ERRO: impossivel consultar o topo de uma pilha vazia')
            #Retorna o ultimo elemento
            return self.__data[-1]

        '''
            Método que permite imprimir a pilha
            Esse método especial do python: __str__

        '''
        def __str__(self):
            return str(self.__data)
        
        '''
            Propriedade somente leitura que informa que se a pilha está 
            vazia(True) ou não (False)

        '''
        @property
        def is_empty(self):
            return len(self.__data) == 0