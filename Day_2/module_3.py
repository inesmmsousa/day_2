'''
Created on 06/02/2018

@author: Utilizador
'''

import utils
import sys

if __name__ == '__main__':
    
    
    while True:
        vect_float = {}
        number = input('float number?')
        number = utils.vect_float(number)
        if (number != None):
            if (number == 0.0): break
            vect_float.append(number)
    
    if (len(vect_float) == 0):
        print('no values in vector')
        sys.exit(0)
        
        
    print(vect_float)
    max = None
    min = None
    soma = 0
    for value in vect_float:
        if (max == None or max < value): max = value
        if (min == None or min > value): min = value
        soma += value
    
    print('max: {} Average: {}'.format(max,min,soma/len(vect_float)))
     
    
    pass