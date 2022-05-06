"""
    ESTRUTURA DE DADOS FILA (QUEUE)
        é uma estrutura de dados em Linear em que tanto a operação de inserção (emqueue) acontece no final da estrutura, quanto a operação retirada(dequeue) acontecem no começo.
        Como consequencia o funcionamento da FILA pode ser definido como FIFO(First in, First out): O Primeiro a entrar e o primeiro a sair.
"""

from logging import exception


class Queue:
    """ Método contrutor """
    def __init__(self):
        #inicializando uma lista vazia
        self.__data = []
    
    """
       Metodo para incersão
       Nome padrao = enqueue
    """
    def enqueue(self,val):
        self.__data.append(val)
    
    """
        Metodo para remoção
        Nome padrao: dequeue()
    
    """

    def dequeue(self):
        if self.is_empty:
            raise Exception('ERRO: impossivel remover de uma fila vazia')
        
        #remove o primeiro elemento da fila
        return self.__data.pop(0)
    
    """
        Método que consulta o valor no inicio da fila, sem retira-lo de lá
        Nome padronizado: peek() 
    """

    def peek(self):
        if self.is_empty:
            raise Exception('ERRO: impossivel consultar o inicio da fila vazia')
        #Retorna o ultimo elemento
        return self.__data[0]

    """
        Método que permite imprimir a Fila
        Esse método especial do python: __str__
    """

    def __str__(self):
        return str(self.__data)
    

    """
        Propriedade somente leitura que informa que se a pilha está 
        vazia(True) ou não (False)    """

    @property
    def is_empty(self):
        return len(self.__data) == 0
