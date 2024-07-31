from objParser import Container
from mat import Matrix, normalize
from math import sin, cos


class obj3D():

    def __init__(self, filepath) -> None:
        container = Container(filepath)
        self.name = container.name
        self.vertexes = container.vertexes
        self.faces = container.faces


        def search_normalies(self):
            result = []
            normalize_Vcords = [list(map(lambda x: x / i[-1], i))[:-1] for i in self.vertexes]
            for f in self.faces:
                face = [normalize_Vcords[f[0] - 1], normalize_Vcords[f[1] - 1], normalize_Vcords[f[2] - 1]]
                x0, y0, z0 = face[0]
                x1, y1, z1 = face[1]
                x2, y2, z2 = face[2]
                normal = Matrix([[Matrix([[1, 0, 0]]), Matrix([[0, 1, 0]]), Matrix([[0, 0, 1]])],
                                [x1 - x0, y1 - y0, z1 - z0],
                                [x2 - x0, y2 - y0, z2 - z0]]).determinant_1s_vec()
                coordinates = (normal[0] + normal[1] + normal[2]).to_arr()[0] + [0]
                result.append(normalize(coordinates, 0.01)) # normalize coords in range [-1; 1]
            return result


        self.normalies = search_normalies(self)
    
    def scale(self, n):
        Ms = Matrix([[n, 0, 0, 0],
                    [0, n, 0, 0],
                    [0, 0, n, 0],
                    [0, 0, 0, 1]])
        
        result = list() #
        for v in self.vertexes: #
            result.append(Matrix([v]) * Ms) # can be a decorator or a function
        self.vertexes = list(map(lambda x: x.to_arr()[0], result)) #

        result = list()
        for n in self.normalies:
            result.append(Matrix([n]) * Ms)
        self.normalies = list(map(lambda x: normalize(x.to_arr()[0], 0.01), result))
    
    def move(self, pos: tuple):
        tx, ty, tz = pos
        Mm = Matrix([[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                    [tx, ty, tz, 1]])
        
        result = list()
        for v in self.vertexes:
            result.append(Matrix([v]) * Mm)
        self.vertexes = list(map(lambda x: x.to_arr()[0], result))

        result = list()
        for n in self.normalies:
            result.append(Matrix([n]) * Mm)
        self.normalies = list(map(lambda x: x.to_arr()[0], result))

    def Xrotate(self, a):
        Rx = Matrix([[1, 0, 0, 0],
                    [0, cos(a), sin(a), 0],
                    [0, -sin(a), cos(a), 0],
                    [0, 0, 0, 1]])
        
        result = list()
        for v in self.vertexes:
            result.append(Matrix([v]) * Rx)
        self.vertexes = list(map(lambda x: x.to_arr()[0], result))

        result = list()
        for n in self.normalies:
            result.append(Matrix([n]) * Rx)
        self.normalies = list(map(lambda x: x.to_arr()[0], result))

    def Yrotate(self, a):
        Ry = Matrix([[cos(a), 0, -sin(a), 0],
                    [0, 1, 0, 0],
                    [sin(a), 0, cos(a), 0],
                    [0, 0, 0, 1]])
        
        result = list()
        for v in self.vertexes:
            result.append(Matrix([v]) * Ry)
        self.vertexes = list(map(lambda x: x.to_arr()[0], result))

        result = list()
        for n in self.normalies:
            result.append(Matrix([n]) * Ry)
        self.normalies = list(map(lambda x: x.to_arr()[0], result))

    def Zrotate(self, a):
        Rz = Matrix([[cos(a), sin(a), 0, 0],
                    [-sin(a), cos(a), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])
        
        result = list()
        for v in self.vertexes:
            result.append(Matrix([v]) * Rz)
        self.vertexes = list(map(lambda x: x.to_arr()[0], result))

        result = list()
        for n in self.normalies:
            result.append(Matrix([n]) * Rz)
        self.normalies = list(map(lambda x: x.to_arr()[0], result))


class Camera():
    def __init__(self, arr=[0, 0, 1]) -> None:
        self.view = arr + [0]
    
    def check(self, other):
        scalar = sum(self.view[i] * other[i] for i in range(4))
        self_abs = (sum(map(lambda x: x ** 2, self.view)) ** 0.5)
        other_abs = (sum(map(lambda x: x ** 2, other)) ** 0.5)
        return scalar / (self_abs * other_abs + 1)

    
    # def __init__(self, arr=[0, 0, 1]) -> None:
    #     self.view = Matrix([arr + [0]])
    
    # def check(self, other):
    #     scalar = sum((self.view * other.transpose()).to_arr()[0])
    #     self_abs = (sum(map(lambda x: x ** 2, self.view.to_arr()[0])) ** 0.5)
    #     other_abs = (sum(map(lambda x: x ** 2, other.to_arr()[0])) ** 0.5)
    #     return acos(scalar / (self_abs * other_abs))