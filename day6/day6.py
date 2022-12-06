# Reading the input file
f = open('input.txt', 'r')
input_ml = f.read()


# Examples
example1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
example2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
example3 = "nppdvjthqldpwncqszvftbrmjlhg"
example4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
example5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

# Sliding window to find unique markers on the string
def sliding_window(seq, ws):
    # nº of sequences on the string = size of seq - window size +1
    for i in range(len(seq) - ws +1):
        marker = seq[i:i+ws]
        if len(marker) == len(set(marker)):
            return i+ws
        
# PART 1

# print(sliding_window(example1, 4))
# print(sliding_window(example2, 4))
# print(sliding_window(example3, 4))
# print(sliding_window(example4, 4))
# print(sliding_window(example5, 4))

print(f'Solution part 1: {sliding_window(input_ml, 4)}')

# PART 2

# print(sliding_window(example1, 14))
# print(sliding_window(example2, 14))
# print(sliding_window(example3, 14))
# print(sliding_window(example4, 14))
# print(sliding_window(example5, 14))

print(f'Solution part 2: {sliding_window(input_ml, 14)}')