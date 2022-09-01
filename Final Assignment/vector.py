
class Vector(object):
    def __init__(self, list):
        if len(list) == 0:
            self.coords = (0, 0)
        else:
            self.coords = list

    def __len__(self):
        return len(self.coords)

    def __repr__(self):
        return 'Vector: ' + str(self.coords) + ''

    def __getitem__(self, key):
        return self.coords[key]

    def __add__(self, other):
        if len(self.coords) != len(other.coords):
            return None

        new_components = []
        for i in range(len(self.coords)):
            new_components.append(self.coords[i] + other.coords[i])
        return Vector(list(new_components))

    def __mul__(self, other):
        if type(other) == Vector:
            if len(self.coords) != len(other.coords):
                return None

            dot_product = 0
            for i in range(len(self.coords)):
                dot_product += self.coords[i] * other.coords[i]
            return dot_product

    def __abs__(self):
        result = (sum(comp ** 2 for comp in self))**0.5
        return round(result, 5)

    def __eq__(self, other):
        if type(other) != Vector:
            return False
        return self.coords == other.coords


########end of code###################################
#*******************TESTS*******************

# 1. Initialize a vector

# v = Vector([1, 2])
# v1 = Vector([5, 2, 9, 11])
# v2 = Vector([100, 5, 99, 1, 1000, 234])
# print(v)
# print(v1)
# print(v2)

# # 2. Query vector dimension
# print(len(v))
# print(len(v1))

# # 3. print Vector, prints 'Vector:[coordinates]'
# print(v)
# print(v1)

# # 4. access vector coords
# v = Vector([1, 2])
# print(v[0])
# print(v[1])
# v1 = Vector([5, 2, 9, 11])
# print(v1[0])
# print(v1[1])
# print(v1[2])
# print(v1[3])

# 5. add 2 vectors using the + operator
# v1 = Vector([1, 2])
# v2 = Vector([5, 9])
# v3 = Vector([5, 2, 9])
# v4 = Vector([6, 2, 8])
# v5 = v1+v2
# print(v5)
# print(v3+v4)
# print(v1+v3)
# print(v1)
# print(v2)

# # 6. dot product of 2 vectors using * operator
# v1 = Vector([1, 2])
# v2 = Vector([5, 9])
# v3 = Vector([5, 2, 9])
# v4 = Vector([6, 2, 8])
# print(v1*v2)
# print(v3*v4)
# print(v3)
# print(v1*v4)

# # 7. get the norm of the vector using abs(v)
# v1 = Vector([1, 2])
# v3 = Vector([5, 2, 9, 11])
# print(abs(v1))
# print(abs(v3))

# 8. check if vectors are equal using ==
# v1 = Vector([1, 2])
# v2 = Vector([3, 4])
# v3 = Vector([3, 4])
# v4 = Vector([5, 2, 9, 11])
# v5 = Vector([5, 2])
# print(v1 == v2)
# print(v2 == v3)
# print(v4 == v5)



