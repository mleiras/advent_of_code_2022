
def create_graph():
    return {}


def add_node(graph, node):
    if node not in graph:
        graph[node] = {}
    

def add_edge(graph, u, w = None):
    add_node(graph, u)
    graph[u] = w


def creating_graph(data):

    graph = create_graph()

    current = graph
    past = current
    past2 = current

    for i in data:
        if i[0] == '$':
            if 'cd' in i:
                cd = i[5:]+' (dir)'
                if '..' in cd:
                    current = past
                    past = past2
                    continue
                add_node(current, cd)
                past2 = past
                past = current
                current = current[cd]
            if 'ls' in i:
                continue
        else:
            if 'dir' in i:
                continue
            else:
                size, name = i.split()
                add_edge(current, name, size)
    return graph

directories = {}

def get_dir(graph): 
    count = 0
    for key, value in graph.items():
        if '(dir)' in key:
            soma = get_dir(value)
            count += soma
            if key  in directories:
                key = key+str(soma)
            directories[key] = soma
        else:
            def file_count(file):
                size = int(file)
                return size
            
            count += file_count(value)

    return count


def find_in_dict(dictionary):
    soma = 0
    for key, value in dictionary.items():
        if value <= 100000:
            soma += value
    return soma



# Reading the input file
f = open('input.txt', 'r')
input_ml = f.read()

f = open('example.txt', 'r')
example = f.read()

f = open('example2.txt', 'r')
example2 = f.read()

data = example.splitlines()
# data = example2.splitlines()
data = input_ml.splitlines()


g = creating_graph(data)

# To visualize the graph:
# import pprint
# pprint.pprint(g)

get_dir(g)

print(f'Solution Part 1 is: {find_in_dict(directories)}')


## PART 2

space = 70000000
space_needed = 30000000
space_used = list(directories.values())[-1]
current_space = space - space_used
delete_space = space_needed-current_space

def find_space(dictionary):
    smallest = space_used
    for key, value in dictionary.items():
        if value <= smallest and value >= delete_space:
            smallest = value
    return smallest

print(f'Solution Part 2 is: {find_space(directories)}')
