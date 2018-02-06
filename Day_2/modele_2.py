'''
Created on 06/02/2018

@author: Utilizador
'''




import utils

if __name__ == '__main__':

    while True:
        valor = input('introduza um valor inteiro: ')
        valor = utils.is_number(valor)
        if valor != None: break
        
    if (valor % 2 == 0): print('even')
    else: print('odd')
    
    pass