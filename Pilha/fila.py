from lib.queue import Queue

fila = Queue()

fila.enqueue('Mariovaldo')
fila.enqueue('Berlamin')
fila.enqueue('Valdisney')

# Imprime a fila
print(fila)

#atende o primeiro da fila
atendido = fila.dequeue()
print('Atendido: ', atendido)

#Verifica quem será o proximo a ser atendido
proximo = fila.peek()
print('Proximo: ', proximo)

#imprime a fila
print(fila)

