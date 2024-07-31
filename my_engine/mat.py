import copy


class Matrix():

    def __init__(self,  arr_of_arrs: list) -> None:

        self.matrix = arr_of_arrs
        self.w, self.h = len(self.matrix[0]), len(self.matrix)

    def transpose(self):
        res = EmptyMarix(self.h, self.w).matrix

        for j in range(self.w):
            for i in range(self.h):
                res[j][i] = self.matrix[i][j]
        
        return Matrix(res)

    def __add__(self, other):
        res = EmptyMarix(self.w, self.h).matrix

        if self.w == other.w and self.h == other.h:
            for i in range(self.h):
                for j in range(self.w):
                    res[i][j] = self.matrix[i][j] + other.matrix[i][j]

            return Matrix(res)
        else: return None

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            res = list()

            for i in range(self.h):
                row = list()
                for j in range(self.w):
                    row.append(self.matrix[i][j] * other)
                res.append(row)

            return Matrix(res)
        elif isinstance(other, Matrix):
            res = EmptyMarix(other.w, self.h).matrix

            if self.w == other.h:
                for j in range(self.h):
                    for i in range(other.w):
                        res[j][i] = sum(self.matrix[j][k] * other.matrix[k][i] for k in range(other.w))
                        # res[j][i] = sum(self.matrix[j][k] * other.matrix[k][i] if type(self.matrix[j][k]) == int and type(other.matrix[k][i]) == int else 0 for k in range(other.w))

                return Matrix(res) 
            else: raise NameError(f"matrix multiplication condition is not met: self.w != oher.h; {self.w} != {other.h}")
        
        else: raise TypeError(f"unsupported operand type(s) for *: 'Matrix' and {type(other)}")
        
    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            res = list()

            for i in range(self.h):
                row = list()
                for j in range(self.w):
                    row.append(self.matrix[i][j] * other)
                res.append(row)
            return Matrix(res)
        
        else: raise TypeError(f"unsupported operand type(s) for *: {type(other)} and 'Matrix'")

    def determinant_1s_vec(self, flag=True):
        if self.h == self.w:
            if flag: res = list()
            else: res = 0
        
            if self.h == 2:
                return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]

            for i in range(self.w):
                rework = Matrix(copy.deepcopy(self.matrix))
                rework.matrix = rework.matrix[1:]
                rework.h -= 1
                for row in rework.matrix:
                    del row[i]
                rework.w -= 1

                if flag: res.append(self.matrix[0][i] * (-1 if i % 2 else 1) * rework.determinant_1s_vec(False)) 
                else: res += self.matrix[0][i] * (-1 if i % 2 else 1) * rework.determinant_1s_vec(False)
            return res
        else:
            return None

    def to_arr(self):
        return self.matrix


class EmptyMarix(Matrix):

    def __init__(self, w, h):
        self.w, self.h = w, h
        self.matrix = [[0 for j in range(self.w)] for i in range(self.h)]


def normalize(arr, k=1):
    return list(map(lambda x: x / (k * (max(map(abs, arr)) + 1)), arr))


# m1 = Matrix([[1, 2, 3], [4, 5, 6]])
# m2 = Matrix([[1], [2], [3]])
# print((m1 * m2).to_arr())

# m1 = Matrix([[1, 2, 3],
#              [3, 4, 2],
#              [2, 2, 1]])
# print(m1.determinant_1s_vec())

# a = [1, 2, 3, 4]
# i = 2
# b = a[:-i] + a[(i + 1):]
# print(a, b)

# print((Matrix([[40, 0, 0, 0], [0, 40, 0, 0], [0, 0, 40, 0], [0, 0, 0, 1]]) * Matrix([[1.0, 1.0, -1.0, 1]]).transpose()).to_arr())

# class dot2:

#     def __init__(self, connections: list, id: int, *arr) -> None:
#         self.x, self.y = arr[0], arr[1]
#         self.id = id
#         self.nb = connections

#     def to(self):
#         return [self.x, self.y]

# class dot3():

#     def __init__(self, connections: list, id: int, *arr) -> None:
#         self.x, self.y, self.z = arr[0], arr[1], arr[2]
#         self.id = id
#         self.nb = connections

#     def to(self):
#         return [self.x, self.y, self.z]




# pygame.init()
# WIDTH, HEIGHT = 1040, 960 
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# scene1 = pygame.Surface((WIDTH, HEIGHT))
# flag = True


# def proccess(f):
#     res = []
#     for d in f:
#         xy = refract(d)
#         real_xy = [int(WIDTH / 2 + xy[0]), int(HEIGHT / 2 - xy[1])]
#         res.append(real_xy)
#     return res


# def refract(vec3):
#     k = vec3[2] * 2
#     y = (k * vec3[1] / vec3[2] + k) 
#     x = (k * vec3[0] / vec3[2] + k)
#     vec2 = [x, y]
#     return vec2


# fig = [[10, 10, 50], [10, 10, 100], [60, 10, 100], [60, 10, 50],
#        [10, 60, 50], [10, 60, 100], [60, 60, 100], [60, 60, 50]]

# clock = pygame.time.Clock()

# while flag:

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             flag = False
#     scene1.fill((0, 0, 0))
    
#     keys = pygame.key.get_pressed()

#     if keys[pygame.K_RIGHT]:
#         for i in range(len(fig)):
#             fig[i][1] += 5
#     elif keys[pygame.K_LEFT]:
#         for i in range(len(fig)):
#             fig[i][1] -= 5

        

#     for dot in proccess(fig):
#         gfxdraw.pixel(scene1, dot[0], dot[1], (255, 255, 255))
    
#     screen.blit(scene1, (0, 0))
#     pygame.display.flip()

#     clock.tick(30)

# pygame.quit()