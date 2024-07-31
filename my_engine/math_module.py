class Matrix():

    def __init__(self, array_twoD, w=None, h=None):
        self.matrix = array_twoD

        if w and h:
            self.w, self.h = w, h
        else:
            self.w, self.h = len(array_twoD[0]), len(array_twoD)

    def __getitem__(self, key):

        if isinstance(key, slice):
            return Matrix(self.matrix[key.start:key.stop:key.step])
            
        elif isinstance(key, tuple):

            if type(key[0]) == slice and type(key[1]) == slice:
                result = []
                for row in self.matrix[key[0].start:key[0].stop:key[0].step]:
                    result.append(row[key[1].start:key[1].stop:key[1].step])
                print(self.matrix)
                return Matrix(result)
            
            elif type(key[0]) == int and type(key[1]) == int:
                if key[0] < self.h and key[1] < self.w:
                    return self.matrix[key[0]][key[1]]
                else:
                    raise IndexError("Matrix index out of range")
                
            else:
                raise TypeError(f"Martix indexes must be slice and slice, or int and int, not {type(key[0])} and {type(key[1])}")
        else:
            raise TypeError(f"Martix index must be sequence or slices, not {type(key)}")

    def __setitem__(self, key, value):
        if key[0] < self.h and key[1] < self.w:
            self.matrix[key[0]][key[1]] = value
        else:
            raise IndexError("list assignment index out of range")

    def __mul__(self, other):
        if isinstance(other, Matrix):
            result = EmptyMatrix(other.w, self.h)

            if self.w == other.h:
                for j in range(self.h):
                    for i in range(other.w):
                        print(sum(self[j, k] * other[k, i] for k in range(other.w)))
                        result[j, i] = sum(self[j, k] * other[k, i] for k in range(other.w))

                return result
            else:
                raise NameError(f"matrix multiplication condition is not met: self.w != oher.h; {self.w} != {other.h}")
        
        else:
            raise TypeError(f"unsupported operand type(s) for *: Matrix and {type(other)}")

    def __rmul__(self, other):
        pass # fix the rotation glitch

    def toarray(self):
        return self.matrix


class EmptyMatrix(Matrix):

    def __init__(self, w, h):
        super().__init__([[0 for __ in range(w)] for _ in range(h)], w, h)


print((Matrix([[1.0, 1.0, -1.0, 1]]) * Matrix([[40, 0, 0, 0], [0, 40, 0, 0], [0, 0, 40, 0], [0, 0, 0, 1]])).toarray())


# a = [1, 2, 3]
# m1 = Matrix([[1, 2, 3], [4, 5, 6]])
# m2 = Matrix([[1], [2], [3]])
# print((m1[:1] * m2).toarray())
