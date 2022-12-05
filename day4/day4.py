# Reading the input file:

f = open('input.txt', 'r')
input_ml = f.read()

example="""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


data = input_ml.splitlines()
# data = example.splitlines()


# Calculate the sum of pairs with overlapping sections
def find_sum(part = 1):
    soma = 0

    for i in data:
        elves = i.replace('-', ',').split(',')
        elf1 = list(range(int(elves[0]), int(elves[1])+1))
        elf2 = list(range(int(elves[2]), int(elves[3])+1))

        # PART 1 (count if one fully contain the other)
        if part == 1:
            if all(x in elf1 for x in elf2) or all(x in elf2 for x in elf1):
                soma += 1

        # PART 2 (count if one contains at least one section from the other)
        elif part == 2:
            if any(x in elf1 for x in elf2) or any(x in elf2 for x in elf1):
                soma += 1

    return soma


print(f'Solution part 1: {find_sum()}')
print(f'Solution part 2: {find_sum(part = 2)}')