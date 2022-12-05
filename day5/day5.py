# Reading the input file
f = open('input.txt', 'r')
input_ml = f.read()

example = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

import re

# Separation of stacks from directions:

# data = example.split('\n\n')
data = input_ml.split('\n\n')

stacks = data[0]
directions = [dic.split() for dic in data[1].splitlines()] #list of directions

# Nº of existing stacks
total = int(stacks.split('  ')[-1]) #last line is the number of stacks


def create_dict(lines):
    '''
    Creation of a dictionary with nº of existing stacks with list of cranes each (initial positions)
    '''
    dicionario = {num+1: [] for num in range(total)} #num+1 is the number of each stack

    lista = [] # lists of cranes

    for line in lines.splitlines()[:-1]: #remove last line (the numbers of stacks)
        l = re.split('    |   | |\n',line) #remove spaces
        lista.append(l) #append each line to list of cranes

    for line in lista: 
        for i, column in enumerate(line):
            if column == '': #ignoring empty spaces (space without crane)
                pass
            else:
                dicionario[i+1].append(column) #adding the crane (letter) to each correspondente stack
    return dicionario


def moving_stacks_1(dic):
    '''
    Moving stacks (updating the dictionary) based on the list of directions
    -- Moving crane one by one 
    '''
    for each in directions:
        num = int(each[1]) #number of cranes to be moved
        from_crane = int(each[3]) # nº of origin stack 
        to_crane = int(each[5]) # nº of destiny stack

        # PART 1:
        for i in range(num):
            a = dic[from_crane].pop(0) #removing one crane
            dic[to_crane].insert(0, a) # adding crane to destiny
    return dic


def moving_stacks_2(dic):
    '''
    Moving stacks (updating the dictionary) based on the list of directions
    -- Moving multiple cranes 
    '''
    for each in directions:
        num = int(each[1]) #number of cranes to be moved
        from_crane = int(each[3]) # nº of origin stack 
        to_crane = int(each[5]) # nº of destiny stack
        
        # PART 2:
        a = dic[from_crane][:num] #cranes to be moved
        dic[to_crane] = a+dic[to_crane] #adding cranes to destiny all at once
        dic[from_crane] = dic[from_crane][num:] #removing all the cranes at once
    
    return dic


def get_solution(dic):
    '''
    Get key string from the first item (item that is on top) of each stack
    '''
    solution = ''
    for k, value in dic.items():
        letter = ''.join(value[0])
        letter = re.sub("\[|\]","", letter)
        solution += letter

    return solution


d1 = create_dict(stacks)
moving_stacks_1(d1)
print(f'Part 1 solution: {get_solution(d1)}')
# SVFDLGLWV

d2 = create_dict(stacks)
moving_stacks_2(d2)
print(f'Part 2 solution: {get_solution(d2)}')
# DCVTCVPCL