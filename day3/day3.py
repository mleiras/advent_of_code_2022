# Reading the input file:

f = open('input.txt', 'r')
input_ml = f.read()

exemplo = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

# data = exemplo.splitlines()
data = input_ml.splitlines()

import string

# Creation of dictionary with all the letters and priorities associated

dicion = {}

for i, letter in enumerate(string.ascii_lowercase):
    dicion[letter] = i+1
for i, letter in enumerate(string.ascii_uppercase):
    dicion[letter] = i+27

# Separation of compartments:
def process(data):
    lista = []
    tam = int(len(data)/2)
    first = data[:tam]
    last = data[tam:]
    return first, last

# Find same type shared between compartments

def find_same(first, second, third = None):
    if third is not None:
        a = list(set(first)&set(second)&set(third))
    else:
        a = list(set(first)&set(second))
    a = ''.join(a)
    return a

# Calculate sum of the priorities of repeated item types
def find_sum(data):
    soma = 0
    for each in data:
        first, last = process(each)
        same_type = find_same(first, last)
        soma += dicion[same_type]
    return soma

# Calculate sum of the priorities of repeated item types between 3-elves groups
def find_sum_2(data):
    soma = 0
    lista = []
    for i in range(0, len(data), 3):
        lista.append(data[i:i+3])
    for each in lista:
        same_type = find_same(each[0], each[1], each[2])
        soma += dicion[same_type]
    return soma


print(f'Solution part 1: {find_sum(data)}')
print(f'Solution part 2: {find_sum_2(data)}')