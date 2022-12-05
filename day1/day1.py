# Reading the input file:

f = open('input.txt', 'r')
input_ml = f.read()


example = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


# data = example.splitlines()
data = input_ml.splitlines()

# Creating dictionary with calories for each elf:

lista = {0: 0}
elf = 0

for i, x in enumerate(data):
    if x == '':
        elf += 1 # new elf
        lista[elf] = 0 
    else:
        lista[elf] = lista[elf]+int(x) # adding the calories for each elf

top1, top2, top3 = 0,0,0

# Finding the top 3 elves carrying the most calories

for chave,valor in lista.items():
    if valor > top1:
        top3 = top2
        top2 = top1
        top1 = valor
    elif valor >= top2:
        top3 = top2
        top2 = valor
    elif valor >= top3:
        top3 = valor

sum = top1 + top2 + top3 

print(f'Solution part 1: {top1}')
print(f'Solution part 1: {sum}')