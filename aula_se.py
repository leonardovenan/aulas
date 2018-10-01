# -*- coding: utf-8 -*-
"""
Created on Mon Oct 01 17:20:59 2018

@author: Leonardo
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor
Este é um arquivo de script temporário.
"""

#aula sistemas distribuidos 24/09/2018

import threading
import time

'''
def seu_coracao():
    print ('<3')
    return 
threads = []
for i in range(5):
    t = threading.Thread(target=seu_coracao)
    threads.append(t)
    t.start()
def ola_mundo(numero1, numero2):
	print('numeros: %s %s' % (numero1, numero2))
	print('resultado = %d' % (int(numero1) + int(numero2)))
	return
t = threading.Thread(target=ola_mundo, args=(2, 3))
t.start()
def ola_mundo(numero1, numero2):
	print('numeros: %s %s' % (numero1, numero2))
	print('resultado = %d' % (int(numero1) + int(numero2)))
	return
threads = []
for i in range(5):
	t = threading.Thread(target=ola_mundo, args=(2, 1))
	threads.append(t)
	t.start()


def funcao():
	print(threading.currentThread().getName(), ' iniciando')
	time.sleep(2)
	print(threading.currentThread().getName(), ' encerrando')
	return


t = threading.Thread(target=funcao) # usa o nome padrao da thread
t.start()
    


def ola_mundo(numero1, numero2):
	print('numeros: %s %s' % (numero1, numero2))
	print('resultado = %d' % (int(numero1) + int(numero2)))
	return


threads = []

for i in range(5):
	t = threading.Thread(target=ola_mundo, args=(2, 1))
	threads.append(t)
	t.start()    
'''

def funcao1():
	print(threading.currentThread().getName(), ' iniciando')
	time.sleep(2)
	print(threading.currentThread().getName(), ' encerrando')
	return


def funcao2():
	print(threading.currentThread().getName(), ' iniciando')
	time.sleep(3)
	print(threading.currentThread().getName(), ' encerrando')
	return


t1 = threading.Thread(name='thread1', target=funcao1) # define um nome para a thread
t2 = threading.Thread(name='thread2', target=funcao2) # define um nome para a thread
t3 = threading.Thread(target=funcao1) # usa o nome padrao da thread

t1.start()
t2.start()
t3.start()