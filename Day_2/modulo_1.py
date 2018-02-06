'''
Created on 06/02/2018

@author: Utilizador
'''

def is_number(valor):
    
    try:
        return int(valor)
    except:
        return None




if __name__ == '__main__':
    
    while True:
        valor_1 = input('first number?')
        valor_1 = is_number(valor_1)
        if (is_number(valor_1) != None): break
    
    while True:
        valor_2 = input('second number?')
        valor_2 = is_number(valor_2)
        if (is_number(valor_2) != None): break

    if (valor_1 == valor_2): print('iguais')
    elif (valor_1 > valor_2): print('maior: {}'. format(valor_1))
    else: print('maior: {}'.format(valor_2)) 
    
    
    pass