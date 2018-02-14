'''
Created on 06/02/2018

@author: Utilizador
'''

import utils
import sys

if __name__ == '__main__':
    
  
    len_vect = 0
    max = None
    min = None
    soma = 0
    
    while True:
        number = input('float number? ')
        number = utils.vect_float(number)
        if (number != None):
            if (number == 0.0): break
            len_vect += 1
            if (max == None or max < number): max = number
            if (min == None or min > number): min = number
            soma += number
        
    if (len_vect == 0):
        print('no value in vector')
        sys.exit(0)
    
    print('max: {}    Min{}    Average: {}'.format(max,min,soma/len(vect))