class Container():

    def __init__(self, filename) -> None:
        self.name = ""
        self.vertexes, self.normalies = list(), list()
        self.faces, self.norm_ind = list(), list()

        f = open(filename)
        for line in f.readlines():
            if line.startswith("o "):
                self.name = line[:-1].split(' ', 1)[1:]
            elif line.startswith("v "):
                self.vertexes.append(list(map(float, line[:-1].split()[1:]))+[1])
            elif line.startswith("f "):
                data = [list(map(int, i.split('/'))) for i in line[:-1].split()[1:]]
                self.faces.append(list(map(lambda x: x[0], data)))


# cb1 = Container("C:/Users/nsusc/Desktop/theGame/cube.obj")
# print(cb1.faces)
# print(cb1.vertexes)
# print(cb1.norm_ind)

"""Simple test to generate new class obj
    without explicit declaration"""
# class A():
#     def __init__(self, color: tuple) -> None:
#         self.color = color


# objects = []

# for i in range(4):
#     if not i % 2:
#         objects.append(A((255, 23, 2)))

# print(objects)