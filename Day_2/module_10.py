'''
Created on 06/02/2018

@author: Utilizador
'''


if __name__ == '__main__':
    
    text = input('some text: ')
    dict = {}
    for word in text.split():  ### other variant split(','). split('\t'), split('space')
        
        if word in dict: dict[word] += 1
        else: dict[word] = 1
        
    print(dict)