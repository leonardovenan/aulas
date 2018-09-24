# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

#aula sistemas distribuidos 24/09/2018

import threading

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
'''

def ola_mundo(numero1, numero2):
	print('numeros: %s %s' % (numero1, numero2))
	print('resultado = %d' % (int(numero1) + int(numero2)))
	return


threads = []

for i in range(5):
	t = threading.Thread(target=ola_mundo, args=(2, 1))
	threads.append(t)
	t.start()