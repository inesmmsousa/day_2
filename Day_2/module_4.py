'''
Created on 06/02/2018

@author: Utilizador
'''

import utils
import time

def count_down(valor):
    for i in range(valor, 0, -1):
        print(i)
        time.sleep(1)
    print('final')


if __name__ == '__main__':
    
    while True:
        valor = input('introduza um valor inteiro: ')
        valor = utils.is_number(valor)
        if valor != None and valor > 0: break
    
    # call count_down    
    count_down(valor)
    
    pass