class Forest:
    def __init__(self, data):
        self.surface = []
        self.lines = 0
        self.columns = 0

        self.read_surface(data)


    def read_surface(self, data):
        for i, line in enumerate(data):
            self.surface.append([])
            for col in line:
                self.surface[i].append(int(col))

        self.lines = len(self.surface)
        self.columns = len(self.surface[0])


    def print_mat(self, m):
        for lin in m:
            for col in str(lin):
                print(col, end='')
            print()


    def visible_top(self, lin, col):
        l1 = lin - 1
        while l1 >= 0:
            if self.surface[l1][col] >= self.surface[lin][col]:
                return False
            else:
                l1 -= 1
        return True

    def visible_down(self, lin, col):
        l1 = lin + 1
        while l1 <= self.lines-1:
            if self.surface[l1][col] >= self.surface[lin][col]:
                return False
            else:
                l1 += 1
        return True
        
    def visible_left(self, lin, col):
        c1 = col - 1
        while c1 >= 0:
            if self.surface[lin][c1] >= self.surface[lin][col]:
                return False
            else:
                c1 -= 1
        return True

    def visible_right(self, lin, col):
        c1 = col + 1
        while c1 <= self.columns-1:
            if self.surface[lin][c1] >= self.surface[lin][col]:
                return False
            else:
                c1 += 1
        return True


    def visible_trees(self):
        soma = 0
        for i in range(self.lines):
            for c in range(self.columns):
                if self.visible_top(i,c) or self.visible_down(i,c) or self.visible_left(i,c) or self.visible_right(i,c):
                    soma += 1
        return soma


    def trees_top(self, lin, col):
        trees = 0
        l1 = lin - 1
        while l1 >= 0:
            if self.surface[l1][col] >= self.surface[lin][col]:
                trees += 1
                break
            else:
                l1 -= 1
                trees += 1
        return trees

    def trees_down(self, lin, col):
        trees = 0
        l1 = lin + 1
        while l1 <= self.lines-1:
            if self.surface[l1][col] >= self.surface[lin][col]:
                trees += 1
                break
            else:
                l1 += 1
                trees += 1
        return trees

        
    def trees_left(self, lin, col):
        trees = 0
        c1 = col - 1
        while c1 >= 0:
            if self.surface[lin][c1] >= self.surface[lin][col]:
                trees += 1
                break
            else:
                c1 -= 1
                trees += 1
        return trees

    def trees_right(self, lin, col):
        trees = 0
        c1 = col + 1
        while c1 <= self.columns-1:
            if self.surface[lin][c1] >= self.surface[lin][col]:
                trees += 1
                break
            else:
                c1 += 1
                trees += 1
        return trees


    def scenic_score(self):
        score = 0
        for i in range(self.lines):
            for c in range(self.columns):
                t, d, l, r = (self.trees_top(i,c), self.trees_down(i,c), self.trees_left(i,c), self.trees_right(i,c))
                score_temp = t*d*l*r
                if score_temp > score:
                    score = score_temp  
        return score



# Reading the input file
f = open('input.txt', 'r')
input_ml = f.read()

f = open('example.txt', 'r')
example = f.read()

# data = example.splitlines()
data = input_ml.splitlines()


forest = Forest(data)

print(f'Solution Part 1: {forest.visible_trees()}')

print(f'Solution Part 2: {forest.scenic_score()}')
